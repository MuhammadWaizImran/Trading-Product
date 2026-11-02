"""Record the completed cloud run and manual continuation commands; no ML."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
checkpoint = '''# Latest checkpoint — 23 September 2026

**Run 007 completed on Kaggle; the full model and product remain unfinished.** All downloaded artifact checks passed, including identical answers after adapter reload. Fitting took 22.6 minutes on a Tesla T4. Read [the results and quality decision](PDF_SFT_007_RESULTS.md).

The 136 training records cover selected material from eight PDFs, not the complete library. Twenty paired development answers were reviewed: source identification and citation-support errors remain, and there is no clear reliable advantage over the base model. The adapter is saved for diagnosis and is not promoted.

Private diagnostic 005 was submitted to compare base and adapter007 on the same 16 frozen retrieval cases (32 answers). It performs cloud inference only, with no fitting. Its URL is https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-adapter-diagnostic-005 . Submission is not completion; check its live status. Do not duplicate the job.

Another 60 training and 32 development-evaluation records across DP05, DP10, DP17 and DP16 are reviewed and staged, but unfitted. See [coverage](PDF_COVERAGE_LEDGER.md) and [acceptance criteria](PDF_MODEL_ACCEPTANCE_PROTOCOL.md). Remaining work includes unresolved PDF coverage, stronger training examples based on diagnosed failures, independent assessment, and separate market/paper-trading validation. There is no defensible completion date for the whole product yet.

---

'''
for name in ['CURRENT_PROGRESS.md', 'MANUAL_TRAINING_HANDOVER.md']:
    path = ROOT/'research'/name
    old = path.read_text(encoding='utf8')
    old = old.replace('# Active checkpoint - 23 September 2026', '# Historical checkpoint before run 007 completed')
    path.write_text(checkpoint + 'Earlier instructions/status below are historical where inconsistent.\n\n' + old, encoding='utf8')
manual = ROOT/'research/MANUAL_TRAINING_HANDOVER.md'
commands = '''## Continue diagnostic 005 manually

Run from the project PowerShell terminal. These commands contact Kaggle; they do not fit locally.

```powershell
$env:PYTHONUTF8='1'
tmp/kaggle_client/Scripts/kaggle.exe kernels status waizimran/crypto-qwen3-pdf-adapter-diagnostic-005
```

When the status is COMPLETE:

```powershell
tmp/kaggle_client/Scripts/kaggle.exe kernels output waizimran/crypto-qwen3-pdf-adapter-diagnostic-005 -p results/pdf_adapter_005_v1
```

Read `pdf_adapter_005/status.json`, `protocol.json`, `base.json` and `adapter007.json` inside the download. Require complete status, 16 distinct matching case IDs per answer file, and no truncated answers. Compare every answer with its retrieved passages and the frozen rubric in `notebooks/pdf_adapter_eval_005/review_protocol.json` and `packets.json`. An existing citation ID can still be unsupported. In particular, negative NOBI cannot identify an unspecified paper, and a sell limit specifies a minimum acceptable sale price. Record errors and base/adapter differences in a new results report before choosing the next training design. Do not count this exposed diagnostic as an independent test.

If the job fails, preserve the log, diagnose the exact failure and create a versioned repair. Do not launch local inference or training. Keep any new Kaggle notebook private. Do not repeat successful jobs just because earlier handover sections mention them.

The run007 audit and coverage update have already passed. To repeat the nonfitting checks if files change:

```powershell
python scripts/audit_pdf_run.py --batch 007 --results results/pdf_sft_007_v1/pdf_sft_007
python scripts/validate_staged_curriculum.py --completed-batch 007 --active-batch none
```

'''
manual.write_text(checkpoint + commands + manual.read_text(encoding='utf8')[len(checkpoint):], encoding='utf8')
readme = ROOT/'README.md'
s = readme.read_text(encoding='utf8').replace('**Latest: private cloud run 007 is submitted/running; see [current progress](research/CURRENT_PROGRESS.md) and [run plan](research/PDF_SFT_007_PLAN.md).**', '**Latest: cloud run 007 completed and its saved adapter passed integrity/reload checks. Quality review found unresolved errors; diagnostic 005 is submitted. See [current progress](research/CURRENT_PROGRESS.md) and [run results](research/PDF_SFT_007_RESULTS.md).**').replace('Six limited Qwen3-8B', 'Seven limited Qwen3-8B')
readme.write_text(s, encoding='utf8')
metadata = ROOT/'notebooks/pdf_adapter_eval_005/kernel-metadata.json'
m = json.loads(metadata.read_text())
m['id'] = 'waizimran/crypto-qwen3-pdf-adapter-diagnostic-005'
metadata.write_text(json.dumps(m, indent=2), encoding='utf8')
(ROOT/'notebooks/pdf_adapter_eval_005/submission.json').write_text(json.dumps({'version':1, 'actual_kernel':'waizimran/crypto-qwen3-pdf-adapter-diagnostic-005', 'note':'Kaggle assigned slug from title; local metadata corrected after successful initial push. No second push.'}, indent=2), encoding='utf8')
print('Recorded completed run007, submitted diagnostic005 and manual continuation steps.')
