"""Prepare only: answerability repair using reviewed PDF passages; no local ML."""
import ast, base64, gzip, hashlib, json
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MARKER='Supplied evidence (reviewed PDF adaptations):\n'
CASES=[
 ('ta-candle','Does one candle alone establish the next price move?', 'No. One candle describes an interval and does not establish the next move.'),
 ('dp05-rsi-definition','Is an RSI lookback alone a complete implementation specification?', 'No. Series, interval, averaging, initialization and zero-loss handling must also be specified.'),
 ('dp16-receive-offline','Must the recipient power up a signing device solely to let someone broadcast to a verified valid address?', 'No. Broadcasting to a known valid address does not require the receiving signing device to be online.'),
 ('dp07-transaction-actions','Do four transfer events necessarily represent four independent investment decisions?', 'No. A single contract transaction can produce multiple transfer events as parts of its operations.'),
 ('dp03-permission-models','Does public source code by itself establish open validation rights?', 'No. Source-code openness and validation authority are separate properties.'),
 ('dp07-exchange-holder','Can a custodial exchange balance automatically be interpreted as one investor holding it?', 'No. An exchange address can custody assets for many customers.'),
 ('dp16-signature-binding','Does signing one message grant blanket approval for later modified messages?', 'No. Verification is bound to the signed message and public key.'),
 ('dp17-spread-depth','Are best quotes alone sufficient to establish the cost of filling a large order?', 'No. Available quantities, deeper levels, fees and changes in the book also affect execution.'),
 ('dp17-vwap-convention','Does a VWAP label alone identify its included trades and reset anchor?', 'No. The included observations and interval or reset anchor must be stated.'),
 ('dp05-adx-direction','Does a rising ADX necessarily mean price is rising?', 'No. ADX describes strength, and a declining price trend can have rising ADX.'),
 ('dp05-relative-volume','Does unusually high reported volume by itself establish investor intent?', 'No. Increased reported activity does not establish trader intent or guarantee continuation.'),
 ('risk-budget','Is the planned loss budget identical to the amount exposed to price movement?', 'No. Planned loss at the stop and position notional are different quantities.'),
 ('dp17-maker-taker','Does the word limit guarantee an order adds liquidity?', 'No. An immediately executable limit order can consume liquidity; execution behavior matters.'),
 ('dp05-upper-wick-context','Can upper-wick geometry alone establish the next market direction?', 'No. Prior context matters for conventional naming and the shape alone is not a directional forecast.'),
]

def main():
    prior=ROOT/'data/pdf_sft_batch_012'
    data=ROOT/'data/pdf_sft_batch_013'; out=ROOT/'notebooks/pdf_sft_013'
    assert not data.exists() and not out.exists()
    manifest=json.loads((prior/'manifest.json').read_text())
    payload={}
    for split in ['train','validation','test']:
        raw=(prior/f'{split}.jsonl').read_bytes()
        assert hashlib.sha256(raw).hexdigest()==manifest['splits'][split]
        payload[split]=[json.loads(s) for s in raw.decode().splitlines()]
    bank={}; templates={}
    for row in payload['train']:
        for e in json.loads(row['messages'][1]['content'].split(MARKER)[1]):
            bank[e['id']]=e
            if row['provenance']['source_id']==e['source'] and row['provenance']['pdf_pages']==e['pages']:
                templates[e['id']]=row
    old=json.loads(next(s for s in (ROOT/'data/pdf_sft_batch_010/train.jsonl').read_text(encoding='utf8').splitlines() if json.loads(s)['id']=='dp10-leverage-definition'))
    e=next(e for e in json.loads(old['messages'][1]['content'].split(MARKER)[1]) if e['id']=='dp10-leverage-definition')
    e['text']=e.pop('answer');e.pop('question');bank[e['id']]=e;templates[e['id']]=old
    system=payload['train'][0]['messages'][0]['content']+(
        ' The status describes whether the ANSWER is supported, not whether the question proposition is true. '
        'A justified No or explanation of a limitation is supported. Apply a supplied rule to explicit question premises; '
        'the passage need not repeat the same scenario. An unspecified outside report is not identified by a similar supplied passage.')
    for rows in payload.values():
        for row in rows:row['messages'][0]['content']=system
    def add(eid,question,answer,status='supported'):
        row=deepcopy(templates[eid]); row['id']=f'r013-{len(payload["train"])-71:03d}'
        row['evidence_ids']=[eid]
        row['provenance']['adaptation']+=' Run013 original application of this reviewed passage; development repair, not an independent test.'
        row['messages']=[dict(role='system',content=system),
            dict(role='user',content=question+'\n\n'+MARKER+json.dumps([bank[eid]],ensure_ascii=False)),
            dict(role='assistant',content=json.dumps(dict(status=status,answer=answer,evidence_id=eid if status=='supported' else None)))]
        payload['train'].append(row)
    for eid,q,a in CASES:
        add(eid,q,a)
        add(eid,'I am asking about a separate unnamed report that I have not supplied or linked to the passage. Does that report endorse the rule described here?',
            'The separate report is unidentified and unavailable. Please provide its identity and relevant text; this passage cannot establish what that report endorses.','insufficient')
    for equity,borrowed in [(120,240),(300,1200),(80,560),(500,0)]:
        exposure=equity+borrowed
        add('dp10-leverage-definition',f'For a simplified financed purchase, equity is {equity} USD and borrowing is {borrowed} USD. What is total-exposure leverage? Use these amounts, not the illustrative ratio in the passage.',
            f'Total exposure is {equity} + {borrowed} = {exposure} USD. Exposure divided by equity is {exposure}/{equity} = {exposure/equity:g} times. This is a simplified financed purchase, not a general derivatives-margin rule.')
    for equity,pct in [(2400,0.5),(6000,2)]:
        add('risk-budget',f'A {equity} USD account has a stated {pct}% planned loss budget. What is that budget in USD, and does it specify position notional?',
            f'The budget is {equity} x {pct}/100 = {equity*pct/100:g} USD. It does not specify notional without stop distance and cost assumptions.')
    for p1,v1,p2,v2 in [(10,2,16,1),(20,3,28,1)]:
        add('dp17-vwap-convention',f'The complete included trade set is {v1} units at {p1} USD and {v2} units at {p2} USD. Calculate trade-level VWAP from these supplied trades.',
            f'VWAP = ({p1} x {v1} + {p2} x {v2})/({v1} + {v2}) = {(p1*v1+p2*v2)/(v1+v2):g} USD per unit.')
    assert len(payload['train'])==108
    texts={s:''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in payload[s]) for s in payload}
    manifest.update(batch='013',created_utc=datetime.now(timezone.utc).isoformat(),
        previous_training_data_sha256=manifest['splits']['train'],
        counts={s:len(payload[s]) for s in texts},splits={s:hashlib.sha256(t.encode()).hexdigest() for s,t in texts.items()},
        method='Fresh pinned Qwen3-8B rank8 QLoRA LR2e-5 two epochs. Retain72 structured exercises; add14 supported negative conclusions,14 unidentified-source abstentions,8 worked numeric applications.',
        decision_rule='Reject unsupported attribution, wrong arithmetic, unnecessary abstention and invalid JSON; compare equally prompted base. No promotion without independent acceptance.',
        limitation='Exposed development repair. Prompt clarification and dataset change together; no isolated causal attribution. Seven training PDFs in selected passages only; DP10 reviewed leverage passage restored from prior corpus, no new library review.',
        system_prompt_sha256=hashlib.sha256(system.encode()).hexdigest())
    payload['manifest']=manifest
    payload['attribution']=(prior/'ATTRIBUTION.txt').read_text(encoding='utf8')+'\nRun013 adds original applications of reviewed passages, including DP10 p143 corrected leverage definition. User-attested private training permission only.\n'
    source=(ROOT/'notebooks/pdf_sft_012/train.py').read_text(encoding='utf8')
    n=next(n for n in ast.parse(source).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PAYLOAD' for t in n.targets))
    packed=base64.b64encode(gzip.compress(json.dumps(payload,ensure_ascii=False).encode(),mtime=0)).decode()
    lines=source.splitlines(keepends=True); lines[n.lineno-1:n.end_lineno]=['PAYLOAD = json.loads(gzip.decompress(base64.b64decode('+repr(packed)+')))\n']
    source=''.join(lines).replace('pdf_sft_012','pdf_sft_013'); ast.parse(source)
    data.mkdir(); out.mkdir()
    for s,t in texts.items():(data/f'{s}.jsonl').write_bytes(t.encode())
    (data/'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf8')
    (data/'ATTRIBUTION.txt').write_text(payload['attribution'],encoding='utf8')
    (out/'train.py').write_text(source,encoding='utf8')
    meta=json.loads((ROOT/'notebooks/pdf_sft_012/kernel-metadata.json').read_text());meta.update(id='waizimran/crypto-qwen3-pdf-sft-013',title='Crypto Qwen3 PDF SFT 013')
    (out/'kernel-metadata.json').write_text(json.dumps(meta,indent=2))
    print(manifest['counts'])
if __name__=='__main__':main()
