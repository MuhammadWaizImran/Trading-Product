"""Controlled adapter-coverage experiment; preparation only, no local model execution."""
import ast, base64, gzip, hashlib, json, random
from copy import deepcopy
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def main():
    prior=ROOT/'data/pdf_sft_batch_015'
    data=ROOT/'data/pdf_sft_batch_017'; out=ROOT/'notebooks/pdf_sft_017'
    assert not data.exists() and not out.exists()
    m=json.loads((prior/'manifest.json').read_text())
    payload={}; raw_splits={}
    for split in ['train','validation','test']:
        raw=(prior/f'{split}.jsonl').read_bytes()
        assert hashlib.sha256(raw).hexdigest()==m['splits'][split]
        raw_splits[split]=raw
        payload[split]=[json.loads(s) for s in raw.decode().splitlines()]
    marker='Supplied evidence (reviewed PDF adaptations):\n'
    bank={}
    for row in payload['train']:
        for e in json.loads(row['messages'][1]['content'].split(marker)[1]):bank[e['id']]=e
    rng=random.Random(217);added=[]
    for row in payload['train']:
        target=json.loads(row['messages'][2]['content'])
        if target['status']!='supported':continue
        question,raw=row['messages'][1]['content'].split(marker)
        evidence=json.loads(raw)
        assert len(evidence)==1 and evidence[0]['id']==target['evidence_id']
        choices=[e for k,e in bank.items() if k!=target['evidence_id']]
        mixed=rng.sample(choices,3)+evidence;rng.shuffle(mixed)
        x=deepcopy(row);x['id']='r017-mixed-'+row['id']
        x['messages'][1]['content']=question+marker+json.dumps(mixed)
        x['evidence_ids']=[e['id'] for e in mixed]
        x['provenance']['adaptation']+=' Run017 mixed-evidence version of existing reviewed exercise; target unchanged, distractors from existing training bank only.'
        added.append(x)
    payload['train']+=added
    for split in raw_splits:
        raw_splits[split]=''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in payload[split]).encode()
    m.update(batch='017',created_utc=datetime.now(timezone.utc).isoformat(),
        previous_training_data_sha256=m['splits']['train'],
        counts={k:len(payload[k]) for k in raw_splits},
        splits={k:hashlib.sha256(v).hexdigest() for k,v in raw_splits.items()},
        training_sources=dict(Counter(r['provenance']['source_id'] for r in payload['train'])),
        method='Fresh pinned Qwen3-8B all-linear rank8 QLoRA LR1e-5 two epochs;108 retained examples plus mixed-evidence versions of supported training rows. No test targets moved into training.',
        hypothesis='Single-passage training versus multi-passage evaluation mismatch contributes to distractor sensitivity observed in016. Practice selecting evidence and applying question premises.',
        comparison='Same prompt and50 exposed development tests, same-run base comparator. Check leverage, payoff, RSI, VWAP, citation support and regressions.',
        limitation='No new PDF review; correlated augmented examples, not independent new knowledge. Training token budget grows with augmentation. No independent acceptance or profitability evidence.')
    payload['manifest']=m
    payload['attribution']=(prior/'ATTRIBUTION.txt').read_text(encoding='utf8')+'\nRun017: mixed-evidence augmentation from existing training passages only; private permission unchanged.\n'
    source=(ROOT/'notebooks/pdf_sft_015/train.py').read_text(encoding='utf8')
    node=next(n for n in ast.parse(source).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PAYLOAD' for t in n.targets))
    packed=base64.b64encode(gzip.compress(json.dumps(payload,ensure_ascii=False).encode(),mtime=0)).decode()
    lines=source.splitlines(keepends=True)
    lines[node.lineno-1:node.end_lineno]=['PAYLOAD = json.loads(gzip.decompress(base64.b64decode('+repr(packed)+')))\n']
    source=''.join(lines).replace('pdf_sft_015','pdf_sft_017')
    ast.parse(source)
    data.mkdir();out.mkdir()
    for split,raw in raw_splits.items():(data/f'{split}.jsonl').write_bytes(raw)
    (data/'manifest.json').write_text(json.dumps(m,indent=2),encoding='utf8')
    (data/'ATTRIBUTION.txt').write_text(payload['attribution'],encoding='utf8')
    (out/'train.py').write_text(source,encoding='utf8')
    meta=json.loads((ROOT/'notebooks/pdf_sft_015/kernel-metadata.json').read_text())
    meta.update(id='waizimran/crypto-qwen3-pdf-sft-017',title='Crypto Qwen3 PDF SFT 017')
    (out/'kernel-metadata.json').write_text(json.dumps(meta,indent=2))
    print(json.dumps(dict(counts=m['counts'],training_sources=m['training_sources'],target_modules=m['target_modules']),indent=2))
if __name__=='__main__':main()
