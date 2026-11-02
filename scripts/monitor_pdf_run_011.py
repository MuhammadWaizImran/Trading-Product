"""Bounded, read-only Kaggle monitoring and local artifact audit; no ML execution."""
import datetime
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT/'tmp/kaggle_client/Scripts/kaggle.exe'
JOB = 'waizimran/crypto-qwen3-pdf-sft-011'
STATE = ROOT/'research/PDF_SFT_011_MONITOR.json'
DEST = ROOT/'results/pdf_sft_011_v1'

def save(stage, **details):
    data = dict(stage=stage, utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                pid=os.getpid(), job=JOB, local_model_execution=False,
                automatic_successor_training=False, **details)
    temp = STATE.with_suffix('.tmp')
    temp.write_text(json.dumps(data, indent=2), encoding='utf8')
    temp.replace(STATE)

def run(args, timeout=90):
    env = dict(os.environ, PYTHONUTF8='1')
    return subprocess.run(args, cwd=ROOT, env=env, capture_output=True,
                          text=True, encoding='utf8', errors='replace', timeout=timeout)

def main():
    deadline = time.monotonic() + 6*60*60
    failures = 0
    save('monitor_started', poll_seconds=120, maximum_hours=6)
    while time.monotonic() < deadline:
        try:
            result = run([str(CLI), 'kernels', 'status', JOB])
            output = result.stdout + result.stderr
            if result.returncode:
                raise RuntimeError(output[-2000:])
            if 'has status "complete"' in output or 'has status "error"' in output:
                # Never overwrite an existing completed download.
                dest = DEST if not DEST.exists() else ROOT/'results'/('pdf_sft_011_monitor_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
                save('downloading', cloud_status=output.strip(), destination=str(dest))
                downloaded = run([str(CLI), 'kernels', 'output', JOB, '-p', str(dest)], timeout=900)
                if downloaded.returncode:
                    raise RuntimeError((downloaded.stdout+downloaded.stderr)[-2000:])
                state_file = dest/'pdf_sft_011/status.json'
                cloud = json.loads(state_file.read_text(encoding='utf8')) if state_file.exists() else {}
                audit_rc = None
                if cloud.get('stage') == 'completed_training_human_evaluation_pending':
                    audit = run([sys.executable, str(ROOT/'scripts/audit_pdf_run.py'), '--batch', '011', '--results', str(dest/'pdf_sft_011')], timeout=120)
                    (dest/'artifact_audit_log.txt').write_text(audit.stdout+audit.stderr, encoding='utf8')
                    audit_rc = audit.returncode
                save('downloaded_review_required', destination=str(dest), cloud_status=cloud,
                     artifact_audit_exit_code=audit_rc, semantic_review='Required; automated audit cannot establish answer quality.')
                return
            failures = 0
            save('waiting_for_cloud', cloud_status=output.strip(), poll_seconds=120)
        except Exception as exc:
            failures += 1
            save('monitor_error', error=str(exc), consecutive_failures=failures)
            if failures >= 3:
                return
        time.sleep(120)
    save('monitor_timeout', message='Six-hour monitor limit reached; cloud job was not stopped. Check Kaggle manually.')

if __name__ == '__main__':
    main()
