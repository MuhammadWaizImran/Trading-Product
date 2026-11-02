"""Cloud environment diagnostic only: no downloads of model weights or fitting."""
import concurrent.futures
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import subprocess
import urllib.request

assert platform.system() == 'Linux' and Path('/kaggle/working').is_dir()

def check(url):
    try:
        with urllib.request.urlopen(url, timeout=12) as response:
            return {'url': url, 'status': response.status}
    except Exception as exc:
        return {'url': url, 'error': str(exc)}

result = {'python': platform.python_version(), 'runtime': os.getenv('KAGGLE_KERNEL_RUN_TYPE'),
          'packages': {}}
for name in ['torch', 'transformers', 'peft', 'accelerate', 'bitsandbytes']:
    try:
        result['packages'][name] = importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:
        result['packages'][name] = None
try:
    r = subprocess.run(['nvidia-smi', '--query-gpu=name,memory.total', '--format=csv,noheader'],
                       capture_output=True, text=True, timeout=15)
    result['gpu'] = {'returncode': r.returncode, 'stdout': r.stdout, 'stderr': r.stderr}
except Exception as exc:
    result['gpu'] = {'error': str(exc)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    result['network'] = list(pool.map(check, [
        'https://pypi.org/simple/transformers/',
        'https://huggingface.co/api/models/Qwen/Qwen3-8B',
        'https://www.kaggle.com']))
Path('/kaggle/working/cloud_check.json').write_text(json.dumps(result, indent=2))
print(json.dumps(result, indent=2))
