"""Small reviewed corrective SFT; prepare only, all model work stays in cloud."""
import ast
import base64
from collections import Counter
from copy import deepcopy
from datetime import datetime, timezone
import gzip
import hashlib
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
MARKER='Supplied evidence (reviewed PDF adaptations):\n'
CASES=[
 ('dp17-maker-taker',
  'A limit order executes immediately against resting liquidity. Can that execution be taker activity?',
  'Yes. An immediately executable limit can consume resting liquidity and act as a taker; the limit constrains price, not maker status.',
  'Can the order-type label alone establish that an execution adds liquidity?',
  'No. Maker/taker classification depends on execution behavior and venue rules, not merely the limit-order label.',
  'maker/taker execution classification'),
 ('risk-budget',
  'Holding currency notional fixed, can a wider percentage stop increase the planned loss assuming exact execution and equal costs?',
  'Yes. For a fixed notional in a linear position, a wider percentage stop increases the planned price loss. The notional remains fixed in this scenario; execution and costs can change realized loss.',
  'Two linear positions have equal fixed notional and different percentage stop distances. Does changing stop distance automatically change that fixed notional?',
  'No. The notional is fixed by the question. Changing the stop distance changes planned loss under the stated execution assumptions, rather than automatically resizing the position.',
  'fixed notional and risk-at-stop'),
 ('dp05-upper-wick-context',
  'May a small body near the low with a long upper wick receive different conventional names after different preceding trends?',
  'Yes. After a decline the geometry may be discussed as an inverted hammer; after an advance, as a shooting star. Shape alone does not establish the next direction.',
  'Is prior trend irrelevant when distinguishing a shooting star from an inverted hammer?',
  'No. Prior context matters: the shooting star is discussed after an advance and the inverted hammer after a decline.',
  'upper-wick candle naming and prior-trend context'),
 ('dp05-rsi-definition',
  'Should RSI implementations specify initialization as well as lookback?',
  'Yes. Initialization, averaging, price series, interval and zero-loss handling are part of the specification, along with lookback.',
  'Does stating only RSI14 completely specify the numerical implementation?',
  'No. The label leaves the series, interval, averaging, initialization and zero-loss handling unspecified.',
  'RSI input and smoothing conventions'),
 ('dp03-permission-models',
  'Can public read access and restricted validation authority be separate choices?',
  'Yes. Read access and validation authority are separate properties; public reading does not establish open validation.',
  'Does knowing who can read a ledger establish who may validate it?',
  'No. Reading and validation authority are separate properties; the validation rules must be specified.',
  'ledger reading versus validation permissions'),
 ('dp16-signature-binding',
  'Does verification check a signature against the particular message and public key?',
  'Yes. Verification is bound to the signed message and public key; the exact signed fields matter.',
  'May approval for one signed message be assumed to cover a modified message?',
  'No. Verification of one message is not general authorization for another message or content outside the signed scope.',
  'message-bound signature verification'),
]

def declarative(row):
    parts=row['messages'][1]['content'].split(MARKER)
    if len(parts)==2:
        records=json.loads(parts[1])
        for e in records:
            e.pop('question',None)
            e['text']=re.sub(r'^(?:Yes|No)\.\s*','',e.pop('answer'))
        row['messages'][1]['content']=parts[0]+MARKER+json.dumps(records)
    return row

def main():
    data=ROOT/'data/pdf_sft_batch_011';out=ROOT/'notebooks/pdf_sft_011'
    assert not data.exists() and not out.exists(), 'Frozen experiment exists'
    prior=ROOT/'data/pdf_sft_batch_010'
    manifest=json.loads((prior/'manifest.json').read_text())
    old={}
    for split in ['train','validation','test']:
        raw=(prior/f'{split}.jsonl').read_bytes()
        assert hashlib.sha256(raw).hexdigest()==manifest['splits'][split]
        old[split]=[json.loads(s) for s in raw.decode().splitlines()]
    byid={r['id']:r for r in old['train']};bank={}
    for r in old['train']:
        parts=r['messages'][1]['content'].split(MARKER)
        if len(parts)==2:
            for e in json.loads(parts[1]):bank[e['id']]=e
    # Only the48 explicitly authored and reviewed r010 contrast exercises.
    # Do not claim the230 older mixed-evidence examples are verified clean.
    payload={'train':[declarative(deepcopy(r)) for r in old['train'] if r['id'].startswith('r010-')]}
    assert len(payload['train'])==48
    for split in ['validation','test']:
        payload[split]=[declarative(deepcopy(r)) for r in old[split]]
    system=payload['train'][0]['messages'][0]['content']
    for n,(rid,yq,ya,nq,na,missing) in enumerate(CASES,1):
        for polarity,q,a in [('yes',yq,ya),('no',nq,na)]:
            for mode in ['supported','irrelevant']:
                eid=rid if mode=='supported' else 'dp16-receive-offline'
                e=deepcopy(bank[eid]);e.pop('question',None);e['text']=re.sub(r'^(?:Yes|No)\.\s*','',e.pop('answer'))
                prov=deepcopy(byid[eid]['provenance'])
                prov['adaptation']+=' Original reviewed SFT011 application; question premises are supplied assumptions. Declarative evidence preserves prior reviewed facts.'
                row=dict(id=f'r011-{n:02d}-{polarity}-{mode}',provenance=prov,evidence_ids=[eid],messages=[
                    dict(role='system',content=system),
                    dict(role='user',content=q+'\n\n'+MARKER+json.dumps([e])),
                    dict(role='assistant',content=a+f' [{eid}]' if mode=='supported' else f'The supplied passage does not establish this. Please provide relevant evidence about {missing}.')])
                payload['train'].append(row)
    texts={s:''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in payload[s]) for s in ['train','validation','test']}
    m=deepcopy(manifest)
    m.update(batch='011',created_utc=datetime.now(timezone.utc).isoformat(),
        counts={s:len(payload[s]) for s in texts},splits={s:hashlib.sha256(t.encode()).hexdigest() for s,t in texts.items()},
        previous_training_data_sha256=manifest['splits']['train'],
        training_sources=dict(Counter(r['provenance']['source_id'] for r in payload['train'])),
        method='Fresh base rank8 QLoRA, one epoch LR2e-5.72 manually reviewed contrast exercises:48 from010 plus24 new applications. Declarative evidence; same conditional prompt. No continuation from failed adapter010.',
        scope='Small grounding-repair experiment on selected material; intentionally reduced breadth, not whole-library training.',
        evaluation='42 validation and50 test cases retained from010 with declarative evidence. Exposed concept-overlapping development checks; no independent acceptance.',
        decision_rule='Require correction of polarity, unrelated-source and arithmetic errors with no severe regressions against identically formatted/prompted base. Loss alone cannot promote. No final acceptance without independent evaluation.',
        limitation='Curriculum filtering and evidence format both change; this is an engineering repair, not isolation of individual causal factors.')
    payload['manifest']=m
    payload['attribution']=(prior/'ATTRIBUTION.txt').read_text(encoding='utf8')+'\nSFT011:72 reviewed correction examples; user-attested private training permission. No added document coverage or redistribution rights.\n'
    source=(ROOT/'notebooks/pdf_sft_010/train.py').read_text(encoding='utf8')
    node=next(n for n in ast.parse(source).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PAYLOAD' for t in n.targets))
    packed=base64.b64encode(gzip.compress(json.dumps(payload,ensure_ascii=False).encode(),mtime=0)).decode()
    lines=source.splitlines(keepends=True);lines[node.lineno-1:node.end_lineno]=['PAYLOAD = json.loads(gzip.decompress(base64.b64decode('+repr(packed)+')))\n']
    source=''.join(lines).replace('pdf_sft_010','pdf_sft_011');ast.parse(source)
    data.mkdir();out.mkdir()
    for s,t in texts.items():(data/f'{s}.jsonl').write_bytes(t.encode())
    (data/'manifest.json').write_text(json.dumps(m,indent=2),encoding='utf8')
    (data/'ATTRIBUTION.txt').write_text(payload['attribution'],encoding='utf8')
    (out/'train.py').write_text(source,encoding='utf8')
    meta=json.loads((ROOT/'notebooks/pdf_sft_010/kernel-metadata.json').read_text())
    meta.update(id='waizimran/crypto-qwen3-pdf-sft-011',title='Crypto Qwen3 PDF SFT 011')
    (out/'kernel-metadata.json').write_text(json.dumps(meta,indent=2))
    print(json.dumps(m,indent=2))
if __name__=='__main__':main()
