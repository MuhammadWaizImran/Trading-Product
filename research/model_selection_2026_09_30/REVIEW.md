# Pre-adapted model and agent review ? 2026-09-30

Decision: prioritize evaluation of existing domain-adapted weights before further bespoke PDF fitting. Preserve earlier adapters and results as comparators. No model selected for production and no new fitting or deployment launched in this review. All fitting remains private cloud-only; research/paper-only scope persists.

## Five supplied links

1. https://github.com/LLMQuant/awesome-trading-agents ? discovery catalogue of agents, MCPs and skills, not a trained checkpoint. Followed primary repositories for TradingAgents, CryptoTradingAgents, FinGPT and Fin-R1. Listing inclusion is not performance validation or a license grant for listed projects.
2. https://vezgo.com/blog/ai-models-crypto-trading/ ? retrieved full accessible HTML text locally after web fetch timeouts; saved vezgo.txt. Discusses model families, a short contest leaderboard and portfolio-data integration. Useful architecture orientation, not evidence of downloadable crypto-specialist weights. Contest claims were not independently reproduced or used to select a winner.
3. https://huggingface.co/agarkovv/CryptoTrader-LM ? inspected card, repository file list, API metadata and adapter configuration. Genuine published crypto-adapted LoRA, but narrow daily BTC/ETH task. Primary authors' and organizers' papers materially weaken the apparent positive model-card performance story; see below.
4. https://medium.com/@gwrx2005/top-10-ai-powered-crypto-trading-repositories-on-github-0041862546b6 ? initial web index returned page metadata, but repeated body retrieval timed out and direct public request returned403. Full article NOT reviewed. No paywall/access bypass attempted; no claims about its complete ten entries. User can paste article text for completion.
5. https://www.ankr.com/blog/choosing-the-best-ai-models-for-crypto-agents-the-developer-s-guide/ ? March26,2025 general model-selection article, not a release of crypto-trained weights. Its descriptions are not verified model benchmarks. Do not infer that using a generic model inside a crypto agent means the weights were crypto-fine-tuned.

## CryptoTrader-LM evidence

Pinned adapter revision09a36894351d032b7c83dfbc56b6bf9adcae9db8. API lists README, adapter_config, adapter_model.safetensors and inference script; no explicit license file or license metadata found. Adapter file listing is7.69MB; card's approximately16GB checkpoint wording should not be read as adapter size. Base is mistralai/Ministral-8B-Instruct-2410. Configuration specifies rank8, alpha16, dropout0.1, q_proj/v_proj. It also contains model_type:gpt2 despite the declared Mistral base, an inconsistency to check in an isolated compatibility test; not proof that weights fail. No weights executed.

Model card scope: daily BTC/ETH decisions from news and prices; other assets and high-frequency trading explicitly out of scope. No demonstrated all-coin discovery, general fundamentals coverage or chart-image capability.

Card reports validation Sharpe0.94, accuracy72%, average profit8%. Authors' paper Table1 reports BTC Sharpe-0.2549, ETH-0.0252, overall-0.1401 for its evaluated system. Organizers independently report the same values and buy-and-hold overall1.1892. These may be different validation/test settings; neither fraud nor identical-run contradiction is established. The positive card metrics do not validate final trading effectiveness.

Primary sources:
- https://aclanthology.org/2025.finnlp-1.48.pdf (authors, especially p4/Table1)
- https://aclanthology.org/2025.finnlp-1.46.pdf (organizers, p3/Table1)

Authors describe43,553 news instances through September30,2024, label construction from historical decisions and generated explanations. Their testing dates and card data cutoff differ; exact split and label availability need reconciliation before reproduction. Hindsight-generated labels require leakage checks rather than treating narrative quality as predictive evidence. Training hyperparameter descriptions also differ between card and paper (learning rate). Keep exact revisions and actual released config authoritative for loading.

Base release explicitly uses Mistral Research License and asks commercial users to obtain a commercial license: https://huggingface.co/mistralai/Ministral-8B-Instruct-2410 . Public download is not unrestricted product permission. Adapter rights remain unclear. Decision: research comparator only after rights/compatibility checks; do not adopt as our all-coin product core or assume further fine-tuning removes base restrictions.

## Other candidates / frameworks

Fin-R1: https://huggingface.co/SUFE-AIFLM-Lab/Fin-R1 and https://github.com/SUFE-AIFLM-Lab/Fin-R1 . Pinned HF revision026768c4a015b591b54b240743edeac1de0970fa. Actual full weights published; Qwen2.5-7B-Instruct-derived financial reasoning with SFT/RL, broader finance rather than proven crypto specialization. README declares Apache2.0 via badge; API detects no standalone repository license and HF metadata lacks license. Clarify weight-license scope before product distribution. Suitable finance-reasoning evaluation candidate, not a claimed solution to all-coin crypto expertise. Reported finance QA scores do not establish profitable ranking.

FinGPT: https://github.com/AI4Finance-Foundation/FinGPT . Family of finance models/tasks. Official Forecaster documentation states training on US Dow30 data; not a ready all-coin crypto forecaster. Sentiment models could be a component if their exact checkpoint/task and license fit. Do not call every community crypto-named adapter an official FinGPT release.

CryptoTradingAgents: https://github.com/Tomortec/CryptoTradingAgents . Crypto research/report framework, external Qwen/ChatGPT model APIs plus data/indicator providers. Repository API identifies Apache2.0. Useful architecture candidate, not crypto-trained weights. Provider access, data rights and costs remain separate. No external tools or order functions installed or invoked.

TradingAgents: https://github.com/TauricResearch/TradingAgents . Multi-agent orchestration with replaceable LLM providers and OpenAI-compatible endpoint support. Useful modular reference. Multi-agent debate is not independent verification when agents share data/model errors.

Challenge winner Sam's Fans is a further investigation lead, not yet a deployable selected checkpoint: https://aclanthology.org/2025.finnlp-1.47.pdf . Organizer results show BTC improvement over buy-and-hold but not ETH. We have not verified a downloadable licensed checkpoint corresponding exactly to that winning submission; do not substitute a similarly named model.

## Evaluation-first protocol

Separate three questions: factual crypto research, tool-grounded analysis, and predictive coin ranking. First freeze task-specific inputs and scoring before seeing candidate answers. Use identical dated evidence and calculation tools, each model's supported chat template, pinned revision and recorded generation budget. Native reasoning models may need a larger token budget; report latency/truncation instead of unfairly imposing a tiny cap. Cloud inference only, no laptop fitting.

Knowledge gate: original questions spanning token economics, vesting/dilution, liquidity, protocol activity, custody, technical indicators, execution assumptions, uncertainty, stale/missing/conflicting evidence. Include unrelated citations and affirmative/negative formulations. Target at least95% supported correctness,95% appropriate abstention and zero severe fabricated support/risk arithmetic errors; these are project engineering targets, not guarantees or external standards. Development comparisons and untouched acceptance sets must be separate.

Ranking gate: frozen eligible liquid-coin universe per historical date, defined forecast horizon, delisted assets where data allows, timestamp-safe news/fundamentals, walk-forward splits and untouched final period. Compare against buy-and-hold, simple momentum/rules and a simple ranking baseline. Report rank correlation/precision-at-k, net returns with fees/slippage/funding where applicable, drawdown, turnover, Sharpe conventions and uncertainty. Data coverage bounds the claim; do not promise literal every-coin coverage. Prospective paper evaluation follows historical testing.

Proposed research-only architecture after model gate: discovery over dated market universe; fundamentals with cited project/news/on-chain evidence; technical analysis with deterministic OHLCV calculations; risk/fact-checking; report synthesis. Choose one model or multiple only if measured benefit justifies complexity. Existing PDFs can support retrieval without additional domain SFT, subject to permissions. Current data connections remain necessary even for crypto-adapted weights.

Next: resolve CryptoTrader adapter/base rights and winning-checkpoint availability; validate Fin-R1 weight license; freeze and run a small cloud screening comparison before larger independent tests. No new custom SFT should be launched merely to continue the old sequence while model selection is under review. The existing SFT011 result still requires collection/review; not evaluated in this research turn.
