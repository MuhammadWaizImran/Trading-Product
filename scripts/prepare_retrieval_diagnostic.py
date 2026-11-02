"""Freeze an automatic retrieval diagnostic; local preparation only, no ML fitting."""
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from workbench.core import Library


CASES = [
    ('candles', 'Which four prices are encoded by one candlestick, and does its shape alone guarantee the next move?', ['ta-candle'], 'Open, high, low, close over an interval; no guarantee. Cite supporting retrieved evidence.'),
    ('trend', 'What sequence of swing highs and lows characterizes an uptrend?', ['ta-uptrend'], 'Higher highs and higher lows, descriptive not a forecast.'),
    ('stop-fill', 'Does a stop trigger price guarantee the eventual execution price?', ['stop-order'], 'No. Trigger and actual execution differ; slippage/gaps matter.'),
    ('rsi', 'Can an RSI reading above 70, by itself, prove an immediate price reversal?', ['rsi-extreme'], 'No, extremes can persist; no invented certainty.'),
    ('wallet-owners', 'Why can holder addresses differ from the number of independent token owners?', ['dp07-holder-count','corr-address-entity-two-way','dp03-addresses-not-users'], 'Multiple addresses per entity and shared custodial addresses; no owner count inferred.'),
    ('verified-contract', 'Is verified contract source code proof that a token has no security or economic risks?', ['dp07-contract-verification'], 'No; verification/source availability is not audit, correctness or investment safety.'),
    ('receipt-token', 'Why does a depositor receive a receipt token in the guide\'s lending example?', ['dp07-receipt'], 'Represents a claim/accounting for a deposit, not automatic extra profit.'),
    ('oracle', 'Why can a weather-triggered smart contract still depend on trusted external information?', ['dp01-oracle'], 'External data/oracle trust remains; chain execution does not establish weather truth.'),
    ('reserves', 'Does correct blockchain consensus prove a stablecoin has adequate redeemable reserves?', ['dp03-ledger-consensus','dp03-security-not-value','dp03-stablecoin-backing'], 'No; state agreement is distinct from backing, valuation and redemption.'),
    ('dated-report', 'May historical coin market capitalizations in the report be presented as today\'s figures?', ['dp03-historical-market-numbers'], 'No; date and scope are essential, fresh data needed.'),
    ('data-license', 'Does the liquidity paper\'s open-access license also grant free access to its underlying order-book dataset?', ['paper-data-rights'], 'No; article license and dataset access/rights differ.'),
    ('limit-order', 'What is the execution trade-off of a limit order?', ['limit-order'], 'Price constraint versus no guarantee of fill or timing.'),
    ('unknown-definition', 'A paper I have not supplied defines NOBI. What exactly does its negative sign mean?', [], 'Do not assume the retrieved paper is the unspecified paper. Ask for its identity or equation; conditional examples clearly labelled are acceptable.'),
    ('current-unlock', 'Which coin has the largest token unlock tomorrow, and what is its exact USD value?', [], 'No current dated schedule or prices in evidence. Abstain; do not invent coin, date, amount or citation support.'),
    ('missing-chart', 'Inspect my chart and identify the exact candlestick pattern. I have not attached a chart or OHLC values.', [], 'Cannot classify missing visual/data; ask for chart or OHLC. No invented pattern.'),
    ('guaranteed-profit', 'Which coin is guaranteed to double next week according to these PDFs?', [], 'No supported guarantee or coin selection; abstain from prediction.'),
]


def main():
    library = Library()
    packets = []
    for case_id, question, expected, rubric in CASES:
        results = library.search(question)
        evidence = [{k:r[k] for k in ('id','source','pages','answer','sha256')} for r in results]
        packets.append({'id':case_id,'question':question,'expected_any_ids':expected,'rubric':rubric,
                        'retrieved':evidence,'retrieval_hit':bool(set(expected)&{r['id'] for r in results}) if expected else None})
    out = ROOT/'notebooks/pdf_retrieval_eval_004'
    out.mkdir(exist_ok=True)
    frozen = json.dumps(packets,indent=2,ensure_ascii=True)
    (out/'packets.json').write_text(frozen,encoding='utf8')
    report = {'diagnostic':'development only, not untouched test', 'case_count':len(packets),
              'corpus':'only reviewed train.jsonl, no validation or test answers',
              'corpus_sha256':hashlib.sha256((ROOT/'data/pdf_sft_batch_006/train.jsonl').read_bytes()).hexdigest(),
              'retriever_sha256':hashlib.sha256((ROOT/'workbench/core.py').read_bytes()).hexdigest(),
              'packet_sha256':hashlib.sha256(frozen.encode()).hexdigest(),
              'supported_case_hits':sum(r['retrieval_hit'] is True for r in packets),
              'supported_cases':sum(r['retrieval_hit'] is not None for r in packets),
              'cases':[{k:r[k] for k in ('id','expected_any_ids','retrieval_hit')} for r in packets]}
    (ROOT/'research/RETRIEVAL_004_PRECHECK.json').write_text(json.dumps(report,indent=2),encoding='utf8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
