# Part 2 — first experiment completed; progression gate failed

Executed 20 September 2026 on the available local CPU, not a cloud GPU. Numerical training/evaluation took about 3.75 seconds excluding Python startup and data download. Large local training was unnecessary. A self-contained Colab/Kaggle notebook is prepared but has **not** been executed on either platform. Provider documentation was checked; personal account eligibility, runtime allocation and quota were not verified.

## What actually ran

- Downloaded and checksum-verified 192 official monthly Binance archives.
- Audited 5,844 daily BTCUSDT/ETHUSDT candles, 2018–2025. Coverage, ordering, duplicate dates, OHLC consistency and timestamp units passed.
- Compared logistic regression and a constrained histogram-boosted tree on separate 2022 and 2023 validation periods. Logistic regression had the lower Brier score in both and was selected before test evaluation.
- Trained the selected model on 4,258 eligible pre-2024 rows, with labels ending before the split.
- Tested on 1,460 asset-days covering 730 daily entry dates, from 2024-01-01 through the last exit on 2025-12-31. This omits the final 2025 entry that would require a 2026 exit.
- Generated per-assessment probabilities, simulated portfolio returns, model checkpoint, archive manifest, code/data/protocol hashes and an interactive equity chart.

The exact rules are in EVALUATION_PROTOCOL.md. There were no test-period parameter searches. The numerical model estimates direction; it does not evaluate projects, read news or discover new coins.

## Main result

| Measure | Result |
|---|---:|
| Selected model | Logistic regression |
| Model Brier score; lower is better | 0.249760 |
| Constant training-prevalence Brier score | 0.249854 |
| Model direction accuracy | 48.77% |
| Constant baseline accuracy | 51.23% |
| Active one-day positions across both assets | 43 |
| Average invested exposure | 2.95% |
| Net return, 15 basis points per side | +0.73% |
| Maximum drawdown | 11.99% |
| Net return, 30 basis points per side | −5.56% |
| 2024 net return | −7.00% |
| 2025 net return | +8.31% |
| Numerical evaluation gate | FAIL |

The tiny probability-score improvement is not persuasive evidence of an edge. Lower Brier error and lower classification accuracy can coexist because Brier measures the full probabilities, whereas accuracy applies a threshold. With only 43 active asset-days, no cost-robust return and a losing test year, the model fails four of seven predeclared gates. Its paired block-bootstrap interval for excess mean daily return over the frozen trend baseline includes zero (approximately −0.072% to +0.177% per day).

Per-asset results also lack consistency: BTC sleeve −1.08%, ETH sleeve +1.29%, each measured as a standalone fully allocated sleeve when active. In causal trend regimes, mean return per asset-day was slightly positive in bear-trend observations and slightly negative in bull-trend observations. These tiny, sparse subgroup estimates should not be promoted as findings.

## A material benchmark weakness, made explicit

The frozen protocol closes and reopens every active one-day position, including consecutive days. Under that convention the trend strategy loses 40.48%, while buy-and-hold gains 69.28%. This makes the daily trend baseline unrealistically expensive relative to a trader who simply holds while the trend stays positive.

After seeing the test results, I ran a **separately labeled execution diagnostic**, without changing the model, features, threshold or original pass/fail result. Both model and trend now carry positions while their signal stays on, pay only at transitions and final liquidation, and use independent sleeves starting at 50% each (no daily cross-asset rebalancing).

| Carry-position diagnostic | Net return | Maximum drawdown |
|---|---:|---:|
| Model | +0.41% | 12.21% |
| Simple 20/60-day trend | +87.17% | 38.72% |
| Buy-and-hold | +69.28% | 42.41% |

At doubled assumed costs the model loses 5.58%. This diagnostic reinforces the no-go result. The trend's larger return comes with much greater exposure and drawdown; it is not a risk-matched comparison or a recommendation. Its success on two surviving coins is not proof that it generalizes. The diagnostic was conceived after test inspection and cannot be called an untouched confirmation experiment.

## Strengths and limitations

The implementation can refuse weak numerical signals and produces a reproducible evidence trail. Tests check feature invariance to future prices, execution lag, missing candles, impossible prices, transaction costs and drawdown from initial capital. All seven passed. Checksums authenticate downloaded files against the publisher's checksum; they do not independently validate that the exchange's data is truthful.

There is no demonstrated trading skill. BTC and ETH are selected survivors; there is no point-in-time market-wide universe. Costs are assumptions rather than reconstructed spreads/depth. Daily data cannot establish intraday fills or capacity. USDT risk, venue interruptions, data revisions and taxes are not modeled. A fixed model can age. No LLM factuality, retrieval quality, news latency or prospective paper decisions have been evaluated.

## Decision and concrete next experiment

**Do not start Part 3 live research agents.** This follows the user's performance gate, not a need for permission or an inability to afford GPU training. Free CPU resources can run this scale of experiment; the bottleneck is credible evidence and data coverage.

The next defensible experiment would predict forward return and downside risk, use trade-transition costs from the start, and compare risk-matched trend/cash baselines. It needs a historically eligible universe that includes failed/delisted assets and point-in-time liquidity. Register that new design first. Use only development data for selection and a newly locked 2026 holdout or prospective period for confirmation; do not keep optimizing against the now-exposed 2024–2025 test.

Before broad discovery, resolve archive redistribution rights and source-specific permissions, audit historical listing/supply/unlock availability and add independent venue checks. Before an explanation model ships, evaluate an original, rights-cleared set of evidence/answer cases for factual support, citations, contradictions and abstention. No additional budget is inherently necessary for these small experiments, but complete historical news, order-book depth and perpetual free hosting have not been established as available for free.

The nearest working free version delivered now is an offline research-and-evaluation workbench, with charts and reproducible simulations. It is not yet the requested end-to-end market research product. No live orders, live agents, commercial deployment or prospective performance are claimed.
