"""Generate private, self-contained cloud notebook. No ML imports or execution."""
import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT/'data/pdf_sft_batch_001'
OUT = ROOT/'notebooks/pdf_sft_001'
payload = {'manifest': json.loads((DATA/'manifest.json').read_text(encoding='utf-8')),
           'attribution': (DATA/'ATTRIBUTION.txt').read_text(encoding='utf-8')}
for split in ('train', 'validation', 'test'):
    path = DATA/f'{split}.jsonl'
    assert hashlib.sha256(path.read_bytes()).hexdigest() == payload['manifest']['splits'][split]
    payload[split] = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines()]
source = (ROOT/'scripts/pdf_cloud_trainer.py').read_text(encoding='utf-8')
marker = 'PAYLOAD = None  # EMBED_PDF_PAYLOAD'
assert source.count(marker) == 1
source = source.replace(marker, 'PAYLOAD = json.loads('+repr(json.dumps(payload, ensure_ascii=False))+')')
ast.parse(source)
notebook = {'nbformat': 4, 'nbformat_minor': 5,
    'metadata': {'kernelspec': {'name': 'python3', 'display_name': 'Python 3', 'language': 'python'},
                 'language_info': {'name': 'python'}, 'accelerator': 'GPU'},
    'cells': [
        {'cell_type':'markdown', 'id':'scope', 'metadata': {}, 'source':
         '# Private Qwen3-8B PDF-derived first batch\n'
         '24 training / 4 validation / 4 test examples derived from four supplied PDFs. '
         'Not the full library. Permissions attested by the user; provenance embedded. '
         'Select a hosted GPU and enable internet. Never execute on a laptop. '
         'This small first batch does not establish expertise or profitability.\n'},
        {'cell_type':'code', 'id':'cloud-training', 'metadata': {}, 'execution_count':None,
         'outputs':[], 'source':source}]}
OUT.mkdir(parents=True, exist_ok=True)
(OUT/'pdf_sft_001.ipynb').write_text(json.dumps(notebook, ensure_ascii=False, indent=2), encoding='utf-8')
metadata = dict(id='waizimran/crypto-qwen3-pdf-sft-001', title='Crypto Qwen3 PDF SFT 001',
                code_file='pdf_sft_001.ipynb', language='python', kernel_type='notebook',
                is_private=True, enable_gpu=True, enable_internet=True,
                dataset_sources=[], competition_sources=[], kernel_sources=[])
(OUT/'kernel-metadata.json').write_text(json.dumps(metadata, indent=2), encoding='utf-8')
print(json.dumps({'notebook': str(OUT/'pdf_sft_001.ipynb'), 'syntax': 'PASS',
                  'training_executed': False, 'submitted_to_cloud': False}))
