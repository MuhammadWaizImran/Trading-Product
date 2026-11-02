"""Controlled adapter-coverage experiment; preparation only, no local model execution."""
import ast, base64, gzip, hashlib, json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def main():
    prior=ROOT/'data/pdf_sft_batch_014'
    data=ROOT/'data/pdf_sft_batch_015'; out=ROOT/'notebooks/pdf_sft_015'
    assert not data.exists() and not out.exists()
    m=json.loads((prior/'manifest.json').read_text())
    payload={}; raw_splits={}
    for split in ['train','validation','test']:
        raw=(prior/f'{split}.jsonl').read_bytes()
        assert hashlib.sha256(raw).hexdigest()==m['splits'][split]
        raw_splits[split]=raw
        payload[split]=[json.loads(s) for s in raw.decode().splitlines()]
    m.update(batch='015',created_utc=datetime.now(timezone.utc).isoformat(),
        previous_training_data_sha256=m['splits']['train'],
        training_sources=dict(Counter(r['provenance']['source_id'] for r in payload['train'])),
        method='Fresh pinned Qwen3-8B all-linear QLoRA rank8 alpha16 dropout0.05 two epochs. Only fitting change versus014: LR2e-5 to1e-5. Identical108 examples, prompt and splits.', learning_rate=1e-5,
        target_modules='all-linear',
        hypothesis='Smaller updates may reduce014 repetition and polarity regression while retaining improvements. Unproven; stop repeating this recipe if major failures persist.',
        comparison='Compare with014 and same-run base on the same50 exposed development cases. Reject if severe arithmetic, false attribution or polarity regressions persist; independent acceptance still required.',
        limitation='No new PDF coverage, no independent acceptance, no profitable-trading claim. Single-seed learning-rate ablation on exposed development cases.')
    payload['manifest']=m
    payload['attribution']=(prior/'ATTRIBUTION.txt').read_text(encoding='utf8')+'\nRun015: identical reviewed examples and private permission basis; learning-rate experiment only.\n'
    source=(ROOT/'notebooks/pdf_sft_014/train.py').read_text(encoding='utf8')
    node=next(n for n in ast.parse(source).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PAYLOAD' for t in n.targets))
    packed=base64.b64encode(gzip.compress(json.dumps(payload,ensure_ascii=False).encode(),mtime=0)).decode()
    lines=source.splitlines(keepends=True)
    lines[node.lineno-1:node.end_lineno]=['PAYLOAD = json.loads(gzip.decompress(base64.b64decode('+repr(packed)+')))\n']
    source=''.join(lines).replace('pdf_sft_014','pdf_sft_015')
    assert source.count('learning_rate=2e-5,')==1
    source=source.replace('learning_rate=2e-5,','learning_rate=1e-5,')
    ast.parse(source)
    data.mkdir();out.mkdir()
    for split,raw in raw_splits.items():(data/f'{split}.jsonl').write_bytes(raw)
    (data/'manifest.json').write_text(json.dumps(m,indent=2),encoding='utf8')
    (data/'ATTRIBUTION.txt').write_text(payload['attribution'],encoding='utf8')
    (out/'train.py').write_text(source,encoding='utf8')
    meta=json.loads((ROOT/'notebooks/pdf_sft_014/kernel-metadata.json').read_text())
    meta.update(id='waizimran/crypto-qwen3-pdf-sft-015',title='Crypto Qwen3 PDF SFT 015')
    (out/'kernel-metadata.json').write_text(json.dumps(meta,indent=2))
    print(json.dumps(dict(counts=m['counts'],training_sources=m['training_sources'],target_modules=m['target_modules']),indent=2))
if __name__=='__main__':main()
