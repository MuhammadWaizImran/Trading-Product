# Part 1 — model and resource decisions

Research checked 20 September 2026 (UTC). This is a crypto-only research project, initially private and paper-only. No real-order integration is authorized or planned. Recommendations below are engineering judgments, not demonstrated trading performance.

## Recommendation

Build two separate capabilities: a small numerical model that can be tested against future prices, and a source-grounded explanation layer. Start with **regularized logistic regression versus scikit-learn histogram gradient boosting** on daily market features. Keep the simpler model unless the tree model improves chronological validation. Use **Qwen/Qwen3-4B-Instruct-2507**, without fine-tuning, as the provisional explanation candidate. It must pass factuality tests before use; deterministic reports are the free fallback.

Use **Binance public historical candles for a private backtesting experiment**, with checksums and explicit limitations. Use **Ethereum documentation and EIPs** for the initial reusable knowledge collection. Mastering Bitcoin is a useful additional source with attribution/share-alike handling. Do not ingest an indiscriminate PDF collection. Several seemingly convenient free sources have unsuitable reuse terms.

The initial experiment is deliberately narrow: BTCUSDT and ETHUSDT, daily observations, a 24-hour forecast and simulated long/cash positions. Bearish forecasts mean avoid exposure, not short sell. These two established assets are a feasibility test, not evidence that the product can discover profitable small coins. The eventual discovery universe needs historical listings and delistings, point-in-time fundamentals and liquidity.

## What each model contributes

| Candidate | Useful role | Limitation | Free feasibility and decision |
|---|---|---|---|
| Cash, buy-and-hold, 20/60-day trend rule | Honest benchmarks; show whether ML adds value | No project/news analysis | No training; mandatory comparisons |
| Regularized logistic regression | Estimate probability of next-period positive return from a few market features | Misses nonlinear relationships; probability is not expected profit | Very small CPU training; selected baseline and possible final numerical model |
| Histogram gradient boosting | Learn nonlinear interactions between momentum, volatility and volume | Can memorize regimes; feature importance is not causality | Small CPU training; selected challenger, capped complexity |
| LightGBM/XGBoost | Similar tabular prediction with extensive optimization controls | Another dependency and larger search space; no automatic forecasting advantage | Feasible on free CPU, defer unless first implementation has a specific limitation |
| Chronos-2 | Pretrained time-series forecast challenger | General forecasting benchmarks do not establish net crypto returns; pretraining overlap complicates historical evaluation | Open model with Apache-2.0 license; try zero-shot later, no large pretraining |
| LSTM/temporal transformer | Sequence modeling if abundant stable data supports it | More tuning and compute; market shifts and correlated samples remain | Small experiments possible on free GPU, not justified first |
| Qwen3-4B-Instruct-2507 + retrieval | Turn verified facts into understandable explanations with links | Can invent facts, arithmetic and citations; cannot provide live knowledge without data | Apache-2.0, 4B parameters; inference candidate, not a price model; no initial fine-tuning |
| Large hosted LLM, vision chart reader, reinforcement learning | Potential richer synthesis, image understanding or execution research | Recurring API costs, hidden provenance, chart leakage, unrealistic simulators | Excluded from zero-budget foundation; no evidence they solve the initial decision better |

Primary documentation: [logistic regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html), [histogram boosting](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html), [scikit-learn BSD license](https://github.com/scikit-learn/scikit-learn/blob/main/COPYING), [LightGBM features](https://github.com/lightgbm-org/LightGBM/blob/main/docs/Features.rst), [Chronos-2 model card](https://huggingface.co/amazon/chronos-2), [Qwen model card](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507) and [license](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/LICENSE).

Why not assume deep learning wins? A [2022 tabular benchmark](https://arxiv.org/abs/2207.08815) supports testing trees on medium-sized tables. A [2024 comparison](https://arxiv.org/abs/2402.03970) provides contrary evidence for some small-data foundation models. Neither study proves a crypto edge. Selection here is based on cost, auditability and our eventual out-of-time results, not a universal claim about trees.

Four billion 16-bit parameters require roughly 8 GB for weights alone; runtime needs more. Quantization can reduce weights, but latency and memory must be measured. Use short retrieved passages, not the advertised maximum context. No promise of a free always-on LLM service or free large-model training.

## Books, prices and charts teach different things

**Reading and retrieval:** Keep licensed passages in a searchable library. At question time, retrieve relevant passages and provide them to the explainer with author, URL, version and retrieval date. This changes what evidence the model sees; it does not change its learned weights. Start with lexical retrieval before adding an embedding model.

**Numerical training:** Historical rows contain only facts available at observation time. Labels describe what happened afterward. This can test whether past patterns help forecast outcomes. It cannot prove that a project is trustworthy or that a trade will succeed.

**Fine-tuning:** Changes a language model's weights using examples. It might later improve extraction or report format, but book ingestion does not establish trading skill. Defer until there are rights-cleared examples and measured failures that prompting/retrieval cannot fix.

**Charts:** Generate our own plots from the same numeric data, clipped at the assessment time. Charts aid human review. Screenshots can leak future candles, hand-picked winners and annotations. There is no demonstrated need to train a vision model initially.

## Resource library and rights decisions

The separate SOURCE_REGISTER.csv records publishers, dates, access, permitted-use interpretation and limitations. Free-to-read is not permission to copy, index or train. Ingestion remains off for restricted/unclear sources. License interpretations below define a conservative project policy, not a guarantee about every future commercial use.

| Source | What it contributes | Free/use decision |
|---|---|---|
| [Mastering Bitcoin, third edition](https://github.com/bitcoinbook/bitcoinbook), Antonopoulos and Harding, 2023 | Bitcoin transactions, keys, consensus and security; legitimate complete online book | CC BY-SA 4.0 shown by repository. Suitable for attributed retrieval with license/changes retained and share-alike requirements respected; keep source adaptations separately labeled. No weights training now |
| [Ethereum documentation](https://ethereum.org/developers/docs/) and [staking risks](https://ethereum.org/staking/pools/) | Protocol fundamentals, security, staking and liquidity risks | Generally CC BY 4.0 non-code content, exceptions apply; verify each item under [terms](https://ethereum.org/terms-of-use/). Selected retrieval source |
| [Ethereum whitepaper](https://ethereum.org/whitepaper/) | Original design and purpose | Free official historical document; same page-specific rights checks. Not a description of every current protocol detail |
| [Ethereum Improvement Proposals](https://eips.ethereum.org/EIPS/eip-1) | Proposed changes and their status | [CC0](https://eips.ethereum.org/LICENSE); selected. A draft proposal is not an activated upgrade |
| [MIT Blockchain and Money](https://ocw.mit.edu/courses/15-s12-blockchain-and-money-fall-2018/) | Lectures, readings and downloadable materials on economics and blockchain | Free study; default [CC BY-NC-SA 4.0](https://ocw.mit.edu/pages/privacy-and-terms-of-use/), third-party exceptions. Reading list, excluded from commercial corpus |
| [MIT Blockchain and the Design of Financial Systems](https://ocw.mit.edu/courses/14-129-blockchain-and-the-design-of-financial-systems-spring-2025/) | More recent economic mechanisms and system design | Same OCW conditions; reading list only. An image's CC BY caption does not license the whole course |
| [CME technical analysis](https://www.cmegroup.com/education/courses/technical-analysis) | Human lessons on chart interpretation, patterns and indicators | Free human reading but [terms explicitly prohibit AI/ML use](https://www.cmegroup.com/tools-information/cme-website-terms-of-use.html). Rejected for ingestion, training and product-generated content |
| [CFTC pump-and-dump advisory](https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/beware_virtual_currency_pump_dump.html) | Recognizing coordinated hype and manipulation | Free official reading. Link/summarize original observations; do not assume third-party illustrations have public-domain rights |
| [Risks and Returns of Cryptocurrency](https://www.nber.org/papers/w24877), Liu and Tsyvinski, 2018; [PDF](https://www.nber.org/papers/w24877.pdf) | Empirical motivation for testing momentum and attention | Free accessible paper; research reading/citation, not a corpus license. Old results are hypotheses for re-testing |
| [Crypto Wash Trading](https://arxiv.org/abs/2108.10984), Cong et al., 2021 | Why reported volume may misrepresent liquidity | Free paper, reading/citation only until individual reuse license checked; no automatic model training |
| [Cryptocurrency Trading: A Comprehensive Survey](https://arxiv.org/abs/2003.11352), Fang et al., 2020 | Map of technical analysis, trading systems, volatility and extreme markets | Free paper; reading/citation, not automatic bulk ingestion |
| [The Probability of Backtest Overfitting](https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf), Bailey et al. | Why repeatedly selecting attractive backtests creates false success | Legitimate author-hosted PDF; methodology reading, no redistribution or training permission presumed |
| [Binance public archive](https://github.com/binance/binance-public-data) | Spot/futures candles and trades; daily/monthly archives, checksum files | Selected for internal testing. Repository says MIT; [provider explicitly promotes backtesting](https://www.binance.com/en/blog/futures/421499824684901131). Do not infer blanket commercial data redistribution rights |
| [Coin Metrics Community](https://github.com/coinmetrics/data) | Daily prices and on-chain metrics; possible independent comparison | Explicit CC BY-NC 4.0. Reserve for separately scoped noncommercial research; not automatically suitable for this product's commercial development |
| [Kraken OHLCVT archive](https://support.kraken.com/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data) | Alternate exchange history and no-trade gaps | Free download documented; archive-specific reuse rights unresolved, hold ingestion pending verification |
| [CoinGecko API](https://www.coingecko.com/en/api/pricing) | Discovery, metadata, market cap, volume | Demo currently 10,000 calls/month, 100/minute, one-year daily/hourly history, attribution required. Demo is not a verified commercial license; use as later prototype option under [API terms](https://www.coingecko.com/en/api_terms), not initial training data |
| [DefiLlama](https://defillama.com/docs/api) | Protocol TVL, fees and other fundamental context | Official API exists, but [terms](https://defillama.com/terms) restrict copying/republication/commercial use. Hold; open-source adapters do not automatically license hosted datasets |
| [CryptoDataDownload](https://www.cryptodatadownload.com/terms-of-use/) and [Coinbase market data](https://www.coinbase.com/legal/market_data) | Alternative market histories | Reviewed alternatives with restrictions; no unqualified commercial reuse. Excluded from initial corpus |

No pirated books, paid textbook mirrors or anonymous relabeled datasets are needed. Own chart examples can be generated from the internal experiment without copying education-site graphics.

## How the product should evaluate a coin

1. Confirm asset identity, chain and contract; a ticker alone can be ambiguous. Check whether the project is live, who can upgrade/pause it, and evidence of security incidents.
2. Separate protocol usage from value accruing to the token. Examine supply, inflation/burn, vesting/unlocks, holder concentration and governance. Missing unlock history is an uncertainty, not zero dilution.
3. Assess actual tradability: venue, bid/ask spread, depth near the proposed size, recent volume, stale quotes and outages. Market cap and volume alone do not establish liquidity.
4. Read price structure using completed candles: returns, trend, volatility, range, drawdown and volume changes. These describe behavior; they do not identify insider intent or guarantee a reversal.
5. Timestamp news by publication, event and retrieval time. Cross-check important claims with primary records and independent reporting. Reposts of one announcement are one piece of evidence.
6. State both support and contradiction, horizon, invalidation and conditional entry. Prefer WAIT when data is stale, estimated advantage fails to cover costs, evidence conflicts, or risk cannot be bounded sensibly.

For the first experiment no news or today's fundamental facts will be retroactively inserted into historical rows. Daily candles cannot reconstruct order-book depth or guarantee a stop fill. Do not simulate exact intrabar stops from daily high/low alone.

## Data contract and missing pieces

Preserve original archive bytes, SHA-256, provider checksum, URL, downloaded-at UTC, symbol, interval, observation times and parser version. Prices are venue-specific and quoted in USDT, not automatically USD. Binance changed spot timestamps from milliseconds to microseconds starting January 2025; normalization must be tested. Reject duplicate/missing daily rows and impossible OHLC relationships, rather than silently repairing them. Updated provider archives require new snapshots.

Missing before broad discovery: historical asset eligibility/delistings; independently verified volume and execution spreads; point-in-time supply/unlocks; trustworthy time-stamped news and reuse rights; long-lived free storage/hosting; tested language-model grounding; prospective outcomes. BTC/ETH results cannot settle these gaps. Commercial redistribution is a separate source-by-source clearance gate.

## Transition to Part 2

Select Colab CPU as the first cloud target: small tabular training needs no GPU. [Colab's official FAQ](https://research.google.com/colaboratory/faq.html) says free resources are dynamic, GPU access is restricted and runs may last at most 12 hours, with earlier termination possible. No guaranteed RAM/GPU quota. Save outputs frequently; do not use free Colab as an always-on server.

[Kaggle notebooks](https://www.kaggle.com/docs/notebooks) are the fallback: documentation lists 12-hour CPU/GPU sessions and 20 GB saved working storage. [GPU documentation](https://www.kaggle.com/docs/efficient-gpu-usage) describes a variable weekly quota around 30 hours; verify the account's actual allocation. [Hugging Face Spaces](https://huggingface.co/docs/hub/spaces-overview) offers a small free CPU environment but sleeping limits make it unsuitable as an uninterrupted research scheduler. None has been provisioned or personally quota-verified in this research step.

Prepare a reproducible notebook and run a small CPU experiment where available. The laptop limitation rules out large-model training; it does not require wasting GPU quota on a small table. Record the actual execution environment honestly. Establish the evaluation protocol before reading held-out results. Do not enter Part 3 on the strength of completed training alone.
