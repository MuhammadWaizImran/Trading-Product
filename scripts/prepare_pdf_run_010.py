"""Prepare a bounded grounding-repair experiment. No local model execution."""
import ast
import base64
import gzip
from collections import Counter
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SYSTEM = ('Answer the question using only the supplied evidence and any explicitly supplied verified tool output. '
          'First check whether the evidence supports the requested conclusion. If it does not, state what relevant evidence is missing; do not answer from memory or cite an unrelated passage. '
          'When supported, answer directly in at most three short sentences and cite the supporting evidence ID in square brackets. '
          'Make Yes or No agree with the question and explanation. Do not invent tool calls, calculator results, measurements or source details. '
          'Mention tools only when an actual tool result is supplied and relevant. Preserve uncertainty and distinguish possibility from certainty.')

# Manually reviewed against the previously reviewed PDF adaptations. These are
# original teaching exercises, not source quotations or broad010 test targets.
CASES = [
 ('ta-candle', 'Does the body connect opening and closing prices?', 'Yes. The real body spans the opening and closing prices.',
  'Does the body always span the complete high-to-low interval?', 'No. The body spans open to close; wicks extend to the high and low.',
  'the candlestick body definition'),
 ('dp16-receive-offline', 'Is payment broadcasting to a verified known address possible while its signing device is disconnected?',
  'Yes. The sender can broadcast to that address while the receiving signing device is offline; confirmation and later spending are separate.',
  'Must the receiving signing device sign a new message before someone can send to its already known valid address?',
  'No. The sender can broadcast without the receiving signing device being online; later authorizing spending is a separate step.',
  'receiving-address and offline-signing behavior'),
 ('dp03-permission-models', 'Can unrestricted reading coexist with validation restricted to approved parties?',
  'Yes. Read access and validation authority are separate properties.',
  'Does publishing the source code establish that anyone may validate?',
  'No. Source-code openness and validation authority are separate properties.', 'the ledger access and validation rules'),
 ('dp16-signature-binding', 'Should a verifier check the actual signed message and public key?',
  'Yes. Signature verification is bound to the signed message and public key; the signed fields matter.',
  'Does verifying one message authorize changes to fields outside that signed scope?',
  'No. Validity for one message does not authorize another message or content outside the signed scope.', 'signature scope and verification'),
 ('dp17-vwap-convention', 'Should two VWAP implementations document their reset anchors before comparison?',
  'Yes. The interval or reset anchor, included price observations and volume units must be specified.',
  'Is resting quote depth interchangeable with executed trade volume when defining trade-volume VWAP?',
  'No. A resting-order-book average differs from trade-volume VWAP.', 'the VWAP definition and input conventions'),
 ('dp05-rsi-definition', 'Can differing smoothing initialization affect reproducibility of RSI?',
  'Yes. Initialization is part of the required specification alongside the price series, interval, lookback and averaging method.',
  'Does choosing a fourteen-period lookback specify every RSI implementation choice?',
  'No. The series, interval, averaging, initialization and zero-loss handling also need specification.', 'the RSI implementation conventions'),
 ('dp07-transaction-actions', 'Can a single contract transaction include more than one operation?',
  'Yes. One transaction can perform multiple operations and emit transfers describing parts of them.',
  'Is every emitted transfer necessarily a separate investment decision?',
  'No. Transfers may describe parts of operations within one transaction; event counts alone do not establish independent decisions.', 'transaction operations and transfer-event semantics'),
 ('dp07-exchange-holder', 'Can one exchange address hold assets on behalf of multiple customers?',
  'Yes. An exchange address can custody assets for many customers and support operational transfers.',
  'Does an exchange address balance necessarily measure one investor\'s conviction?',
  'No. Custodial aggregation and operational transfers can explain the balance.', 'exchange custody and entity attribution'),
 ('dp17-spread-depth', 'Can a large order consume more than one quoted price level?',
  'Yes. Available quantities and deeper levels affect execution, alongside fees and book changes.',
  'Does a narrow best-quote spread alone establish low execution costs for any order size?',
  'No. Depth, quantities, fees and changing orders must also be considered for the intended size.', 'order-book depth and execution constraints'),
 ('dp05-adx-direction', 'Can a declining trend have rising ADX?',
  'Yes. ADX describes strength rather than direction; rising ADX can occur in a declining trend.',
  'Does ADX rising by itself establish upward price direction?',
  'No. ADX describes trend strength; direction requires separate information.', 'ADX strength versus direction'),
 ('dp05-relative-volume', 'Should reported relative volume name its venue and comparison window?',
  'Yes. Venue, asset, units, interval and reference window must be stated.',
  'Does above-baseline reported volume establish why participants traded?',
  'No. Increased reported activity does not reveal trader intent or guarantee continuation.', 'volume measurement and interpretive limits'),
 ('risk-budget', 'Are position notional and planned loss at the stop different quantities?',
  'Yes. Notional is the amount exposed; risk-at-stop is the planned loss assuming the stop executes as modeled.',
  'If two equal notionals use different stop distances, must their modeled stop losses match?',
  'No. With notional held equal, different stop distances can produce different planned losses; execution and costs still matter.', 'notional versus stop-loss risk'),
]

def main():
    prior = ROOT/'data/pdf_sft_batch_009'
    dest = ROOT/'data/pdf_sft_batch_010'
    out = ROOT/'notebooks/pdf_sft_010'
    assert not dest.exists() and not out.exists(), 'Frozen experiment must not be overwritten'
    old = json.loads((prior/'manifest.json').read_text())
    payload = {}
    for split in ('train', 'validation', 'test'):
        raw = (prior/f'{split}.jsonl').read_bytes()
        assert hashlib.sha256(raw).hexdigest() == old['splits'][split]
        payload[split] = [json.loads(line) for line in raw.decode().splitlines()]
        for row in payload[split]: row['messages'][0]['content'] = SYSTEM
    bank = {}; provenance = {}
    for row in payload['train']:
        parts = row['messages'][1]['content'].split('Supplied evidence (reviewed PDF adaptations):\n')
        if len(parts) == 2:
            for e in json.loads(parts[1]):
                if e['id'] in bank: assert bank[e['id']] == e
                bank[e['id']] = e
        if row['id'] in bank: provenance[row['id']] = row['provenance']
    def add(split, identifier, rid, question, answer):
        p = deepcopy(provenance[rid])
        p['adaptation'] += ' Run010 original grounding exercise using this reviewed passage; no additional document coverage.'
        payload[split].append(dict(id=identifier, provenance=p, evidence_ids=[rid], messages=[
            dict(role='system', content=SYSTEM),
            dict(role='user', content=question+'\n\nSupplied evidence (reviewed PDF adaptations):\n'+json.dumps([bank[rid]])),
            dict(role='assistant', content=answer)]))
    for n, (rid, yesq, yesa, noq, noa, missing) in enumerate(CASES, 1):
        other = CASES[(n+4) % len(CASES)][0]
        for label, q, a in [('yes', yesq, yesa), ('no', noq, noa)]:
            add('train', f'r010-{n:02d}-{label}', rid, q, a+f' [{rid}]')
            add('train', f'r010-{n:02d}-{label}-irrelevant', other, q,
                f'The supplied passage does not establish this. Please provide evidence about {missing}.')
    # Fresh development formulations, concept-overlapping; never final acceptance.
    probes = [
      ('ta-candle', 'For a bar opening at 42 and closing at 39, do those two prices bound its body?', 'Yes. Its body spans 39 to 42.', 'candlestick body definitions'),
      ('dp16-receive-offline', 'A recipient keeps its signing hardware in storage. May a sender broadcast to the recipient\'s verified existing address without turning that hardware on?', 'Yes. Broadcasting to the known valid address does not require the receiving signing device to be online; confirmation and spending are separate.', 'offline receiving behavior'),
      ('dp03-permission-models', 'A project opens its explorer to everyone but approves each validator. Are the read and validation policies different?', 'Yes. Public read access and restricted validation are separate properties.', 'ledger access policies'),
      ('dp17-vwap-convention', 'A dashboard omits its VWAP anchor and included observations. Is its calculation fully specified?', 'No. The interval or reset anchor, included observations and units must be stated.', 'VWAP input conventions'),
      ('dp07-transaction-actions', 'A deposit wraps an asset and issues a protocol receipt in one transaction. Can multiple transfer events belong to these operations?', 'Yes. A single transaction can perform multiple operations whose transfer events need not be separate investment decisions.', 'transaction-event semantics'),
      ('dp05-adx-direction', 'An analyst treats ADX as a direct label for upward versus downward movement. Is that the distinction measured by ADX?', 'No. ADX describes trend strength rather than upward or downward direction.', 'ADX interpretation'),
    ]
    for n, (rid, q, a, missing) in enumerate(probes, 1):
        split = 'validation' if n % 2 else 'test'
        add(split, f'r010-probe-{n}-supported', rid, q, a+f' [{rid}]')
        other = 'dp07-exchange-holder' if rid != 'dp07-exchange-holder' else 'ta-candle'
        add(split, f'r010-probe-{n}-irrelevant', other, q, f'The supplied passage does not establish this. Please provide evidence about {missing}.')
    texts = {s: ''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in payload[s]) for s in ('train','validation','test')}
    m = deepcopy(old)
    m.update(batch='010', created_utc=datetime.now(timezone.utc).isoformat(),
      counts={s:len(payload[s]) for s in texts}, splits={s:hashlib.sha256(t.encode()).hexdigest() for s,t in texts.items()},
      previous_training_data_sha256=old['splits']['train'],
      training_sources=dict(Counter(r['provenance']['source_id'] for r in payload['train'])),
      method='Fresh rank8 QLoRA, 1 epoch, LR2e-5. 48 reviewed relevance/polarity contrast examples plus230 replay examples. Conditional tool instructions applied identically to base and adapter.',
      scope='278 records from selected reviewed material in ten PDFs; no new PDF/page coverage.',
      evaluation='Carried-forward exposed development cases plus12 fresh concept-overlapping development probes (6 validation,6 test). Broad010 failures informed curriculum; broad010 is now exposed development evidence. No independent acceptance claim.',
      decision_rule='Compare identically prompted base/adapted/reloaded outputs. Require all6 new test probes correct, relevant citations, no invented tools or contradictory polarity, and no severe regression on old cases. No promotion without independent acceptance. If base also passes, do not claim adapter advantage.',
      system_prompt_sha256=hashlib.sha256(SYSTEM.encode()).hexdigest(),
      automatic_successor_training=False)
    payload['manifest'] = m
    payload['attribution'] = (prior/'ATTRIBUTION.txt').read_text(encoding='utf8')+'\nRun010: user-attested private training permission; reviewed adaptations and original grounding exercises. No redistribution rights asserted.\n'
    source = (ROOT/'notebooks/pdf_sft_009/train.py').read_text(encoding='utf8')
    node = next(n for n in ast.parse(source).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PAYLOAD' for t in n.targets))
    lines = source.splitlines(keepends=True)
    packed = base64.b64encode(gzip.compress(json.dumps(payload,ensure_ascii=False).encode(),mtime=0)).decode()
    lines[node.lineno-1:node.end_lineno] = ['import base64, gzip\nPAYLOAD = json.loads(gzip.decompress(base64.b64decode('+repr(packed)+')))\n']
    source = ''.join(lines).replace('pdf_sft_009','pdf_sft_010')
    ast.parse(source)
    dest.mkdir(); out.mkdir()
    for s,t in texts.items(): (dest/f'{s}.jsonl').write_bytes(t.encode())
    (dest/'manifest.json').write_text(json.dumps(m,indent=2),encoding='utf8')
    (dest/'ATTRIBUTION.txt').write_text(payload['attribution'],encoding='utf8')
    (out/'train.py').write_text(source,encoding='utf8')
    meta=json.loads((ROOT/'notebooks/pdf_sft_009/kernel-metadata.json').read_text())
    meta.update(id='waizimran/crypto-qwen3-pdf-sft-010',title='Crypto Qwen3 PDF SFT 010')
    (out/'kernel-metadata.json').write_text(json.dumps(meta,indent=2))
    print(json.dumps(m,indent=2))

if __name__ == '__main__': main()
