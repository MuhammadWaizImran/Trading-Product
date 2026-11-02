"""Freeze 100 grouped evidence-assessment cases; cloud inference only."""
import ast
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'notebooks/pdf_broad_eval_010'
assert not OUT.exists(), 'Frozen experiment exists'
bank={}
for line in (ROOT/'data/pdf_sft_batch_009/train.jsonl').read_text(encoding='utf8').splitlines():
    row=json.loads(line)
    parts=row['messages'][1]['content'].split('Supplied evidence (reviewed PDF adaptations):\n')
    if len(parts)==2:
        for e in json.loads(parts[1]):
            if e['id'] in bank: assert bank[e['id']]==e
            bank[e['id']]=e
# New application wording; concepts/evidence overlap the training curriculum.
# Four related conditions per concept are not independent observations.
seeds=[
('ta-candle','A candle opens at 18, closes at 16, reaches 21 and falls to 15. Which prices bound its real body, and does it establish the next direction?','Body 16 to18; wicks extend to15 and21; no next-direction guarantee.'),
('dp05-adx-direction','ADX increases while successive closes fall. Is this necessarily an indicator malfunction?','No; strength and direction are separate.'),
('ta-range','A coin has traded sideways for twelve bars. Does the range alone identify which boundary will break first?','No direction established.'),
('dp05-upper-wick-context','Two identical long-upper-wick candles appear, one after an advance and another after a decline. Must their conventional names be identical?','No; shooting-star versus inverted-hammer contexts differ; no forecast certainty.'),
('dp17-bollinger-squeeze','Bands become narrower for eight bars. Can the team label the next breakout bullish from that fact alone?','No; dispersion is reduced, direction/timing unknown.'),
('risk-budget','Two positions each expose 600 dollars but have different stop distances. Must their planned stop losses be equal?','No; notional and planned loss differ; costs/execution matter.'),
('risk-invalidation','An analyst moves a stop inside the setup invalidation solely to display 5R. Has the underlying trade become more reliable?','No; changing stop changes setup and stop-hit likelihood, not proof of improvement.'),
('paper-costs','A simulation earns 0.3 percent per round trip and omits spread and fees. Can this be presented as achievable net performance?','No; net performance requires execution costs and assumptions.'),
('dp05-relative-volume','An exchange reports twice its usual token volume. Does this prove twice as many real investors arrived?','No; activity needs units/window/venue; not investor counts or intent.'),
('dp17-maker-taker','A buy limit immediately crosses the available ask. Must it receive a maker fee because it is a limit order?','No; immediate execution can take liquidity; fees depend on venue rules.'),
('dp17-stop-no-guarantee','A stop is triggered during an exchange outage. Can the simulator book an immediate fill exactly at its trigger as guaranteed?','No; outages/liquidity/venue rules can prevent timely fill.'),
('dp17-spread-depth','Two venues show the same best bid and ask, but one has little quantity available. Must a large purchase have the same average execution price?','No; spread alone does not capture depth or price impact.'),
('book-definition','A snapshot shows large buy orders. Must those orders still be there when our later trade arrives?','No; resting orders can change or cancel.'),
('book-absolute','Two books have signed imbalances +0.6 and -0.6. After taking absolute values can we still distinguish their heavier sides?','No; absolute value removes sign, both become0.6.'),
('dp17-vwap-convention','Two dashboards both label a line VWAP but reset at different times. Is equal naming enough to expect equal values?','No; anchor, inputs, units and method must match.'),
('dp05-rsi-definition','Two implementations both use RSI14 but initialize smoothing differently. Is the period label enough to guarantee reproducible values?','No; series/timeframe/averaging/initialization and edge cases matter.'),
('rsi-extreme','RSI remains at 78 during a rising market. Is an immediate reversal mechanically required?','No; extremes can persist.'),
('dp07-exchange-holder','An exchange wallet receives tokens from thousands of users. Does its balance demonstrate one wealthy investor buying?','No; custodial aggregation and operational flows differ from investor conviction.'),
('dp07-receipt','A lending deposit produces a receipt token. Should the receipt automatically be recorded as a separate speculative purchase?','No; it represents the protocol position; accounting depends on protocol.'),
('dp07-transaction-actions','One contract call emits four transfers. Does this establish four independent investment decisions?','No; one transaction can contain multiple operations/events.'),
('dp03-stablecoin-backing','A token webpage says fully backed but supplies no reserve or redemption evidence. Does the slogan establish safe redemption at par?','No; reserves/custody/liabilities/redemption/liquidity evidence needed.'),
('dp03-permission-models','A ledger is publicly readable but only approved entities validate. Does public reading make validation permissionless?','No; read access and validation authority are distinct.'),
('dp16-signature-binding','A signature verifies message A. Can the app reuse that verification as approval of an altered message B?','No; verification binds the specific message and key.'),
('dp16-receive-offline','A signing device is powered off. Can a sender still broadcast to its already known valid receiving address?','Yes; receiving broadcast does not require signing device online; confirmation/spending separate.'),
('dp17-selection-bias','Researchers try 300 indicator combinations and report the best historical result. Does agreement among its indicators prove independent confirmation?','No; multiple testing and correlated inputs; frozen unseen evaluation with costs needed.')]
cases=[]; rubrics=[]
for index,(rid,question,answer) in enumerate(seeds,1):
    evidence=bank[rid]
    other=bank['dp16-receive-offline'] if rid!='dp16-receive-offline' else bank['dp05-adx-direction']
    for mode in ['supported','irrelevant','missing','unidentified']:
        cid=f'b010-{index:02d}-{mode}'
        selected=[evidence] if mode in ('supported','unidentified') else [other] if mode=='irrelevant' else []
        q=question if mode!='unidentified' else 'In a report I have not identified or supplied, what conclusion does its author give about this case? '+question
        cases.append(dict(id=cid,question=q,retrieved=selected,scope='source_specific' if mode=='unidentified' else 'general',source_id=None,category=rid,condition=mode))
        rubrics.append(dict(id=cid,category=rid,condition=mode,
            expected=answer if mode=='supported' else 'Do not infer or cite the answer from unrelated/absent evidence. Request the relevant passage.' if mode in ('irrelevant','missing') else 'Request document identity; do not attribute the supplied passage to the unnamed report.',
            required_citation=rid if mode=='supported' else None,source=evidence['source'],pages=evidence['pages']))
assert len(cases)==100 and len({c['id'] for c in cases})==100
prior=ROOT/'notebooks/pdf_concise_eval_009'
source=(prior/'evaluate.py').read_text(encoding='utf8')
node=next(n for n in ast.parse(source).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='cases' for t in n.targets))
lines=source.splitlines(keepends=True); lines[node.lineno-1:node.end_lineno]=['cases = json.loads('+repr(json.dumps(cases))+')\n']
source=''.join(lines).replace('pdf_concise_009','pdf_broad_010')
source=source.replace("for mode in ['original_tools','concise_tools']:","for mode in ['concise_tools']:")
source=source.replace('Compares explicit calculator context for base and adapter009 on 13 development cases.','Compares base and adapter009 on 100 grouped evidence cases, no fitting.')
ast.parse(source)
assert all('rubric' not in c and 'expected' not in c for c in cases)
candidate=json.loads((ROOT/'research/model_candidate_2026_09_28.json').read_text())
assert candidate['system_prompt'] in source
meta=json.loads((prior/'kernel-metadata.json').read_text())
meta.update(id='waizimran/crypto-qwen3-pdf-broad-check-010',title='Crypto Qwen3 PDF Broad Check 010')
assert meta['is_private'] and meta['enable_gpu']
protocol=dict(created='2026-09-28',cases=100,concept_groups=25,conditions=['supported','irrelevant','missing','unidentified'],models=['base','adapter009'],responses=200,
    training_executed=False,independent_final_assessment=False,
    limitations='25 application families with four correlated conditions each. Evidence and concepts overlap training. Missing/unidentified requests route deterministically; supplied relevant/irrelevant passages do not assess retrieval. No numerical tool-selection, chart vision, all-library coverage or market prediction assessed.',
    decision='Read all outputs. Score25 supported and25 irrelevant model-invoked cases separately per model; report50 routed cases separately. Require correct supported conclusions/citations and no confident answers from irrelevant evidence. Any severe unsupported claim blocks promotion. Compare base versus adapter before further fitting. This grouped stress assessment cannot substitute for100 independent application questions.',
    code_sha256=hashlib.sha256(source.encode()).hexdigest(),cases_sha256=hashlib.sha256(json.dumps(cases,sort_keys=True).encode()).hexdigest(),
    rubric_sha256=hashlib.sha256(json.dumps(rubrics,sort_keys=True).encode()).hexdigest())
OUT.mkdir()
for name,content in [('evaluate.py',source),('kernel-metadata.json',json.dumps(meta,indent=2)),('review_protocol.json',json.dumps(protocol,indent=2))]: (OUT/name).write_text(content,encoding='utf8')
# Rubrics kept outside uploaded notebook directory and inference context.
(ROOT/'research/PDF_BROAD_010_RUBRICS.json').write_text(json.dumps(rubrics,indent=2),encoding='utf8')
print('Frozen100 cases across25 groups; rubrics excluded from cloud inference; no local fitting.')
