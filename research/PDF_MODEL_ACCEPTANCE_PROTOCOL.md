# What completing PDF model training means

23 September 2026. This protocol defines the remaining educational-model work. It does not supersede the separate market-prediction and prospective paper-trading gates in EVALUATION_PROTOCOL.md.

## Target capability

Given a crypto educational question and retrieved, attributable evidence, answer accurately; cite the supporting record and PDF pages; distinguish historical facts, definitions, hypotheses and measured outcomes; request missing inputs; and use deterministic tools for calculations. No real orders or return guarantees. Broad explanations do not establish a trading edge.

## Corpus completion record

Every distinct uploaded work must have a documented disposition: usable reviewed material, corrected material, duplication, irrelevant content, unsupported claims, unresolved visual/text extraction, or a specific rights restriction. Do not teach incorrect claims merely to include every file. Track covered concepts and cited pages, not just raw file count. “Read,” “prepared,” “submitted,” “fitted,” and “passed evaluation” are different statuses.

The current coverage ledger is PDF_COVERAGE_LEDGER.md. No whole-library completion is claimed. The staged batches created on 23 September contain 60 training and 32 development-evaluation examples across four sources; these are separate from run 007's 136 examples.

## Curriculum coverage to audit

1. Price/time/volume conventions, OHLC, timeframes and point-in-time availability.
2. Market structure, levels, candlestick and chart geometry, failed/ambiguous setups.
3. Indicators, their formulas and implementation assumptions; dependence between indicators.
4. Position sizing, payoff versus probability, fees, slippage, stops, leverage and liquidation distinctions.
5. Order books, spreads, depth, maker/taker behavior, execution and liquidity limitations.
6. Crypto protocol fundamentals, custody, security assumptions and network-specific differences.
7. Token rights, incentives, issuance, reserves, valuation hypotheses and dated fundamental evidence.
8. On-chain addresses versus entities, protocol activity, inference limits and data-provider scope.
9. Derivatives/funding, portfolio risk and correlated exposures where supported by reviewed material.
10. News/event provenance, timestamping, missing/current evidence and contradictory reports.
11. Research design, leakage, selection bias, uncertainty, regime dependence and realistic evaluation.
12. Tool inputs, source attribution, arithmetic checks and warranted abstention.

These are audit categories, not a claim that the supplied PDFs fully and correctly cover all of them. Finish existing review before requesting additional books. Text-only fine-tuning does not establish chart-image recognition; that requires its own dataset and assessment or an explicit OHLC-based alternative.

## Development and independent assessment

Current questions are development diagnostics with substantial conceptual overlap. Preserve all failures and do not relabel them unseen. New training examples informed by those failures are legitimate development work, but invalidate those cases as independent evidence.

For an eventual acceptance assessment, freeze the model revision/adapter, retrieval corpus and algorithm, prompts and calculator versions before running at least 100 independently constructed application questions across the covered categories. Keep references and rubrics outside inference prompts and all fitting. Include at least 25 cases where relevant information is absent, stale, ambiguous or contradictory. The assessment must contain affirmative answerable cases as well as refusals, so an always-abstain model cannot pass.

Engineering acceptance target: at least 95% substantively correct and evidence-supported answers; zero severe fabricated facts, source attributions or risk calculations; at least 95% appropriate handling of insufficient evidence; no invented citation IDs; no truncated answers. Audit citation **support**, not just valid IDs. Report counts and uncertainty rather than presenting the target as an established market standard. If a candidate fails, preserve that evaluation as exposed development history and require fresh assessment for a later candidate.

Compare the base model and candidate under identical context and decoding. Adopt an adapter only if it demonstrates a useful improvement without introducing severe regressions. If the base with retrieval is better, report that outcome; running more epochs is not automatically progress. Do not select a model from loss alone.

## Separate prediction gate

Even a successful educational model cannot establish which coins will make money. Coin ranking/direction/return estimation requires timestamped multi-coin observations, point-in-time eligibility, realistic costs, frozen chronological tests and prospective paper outcomes. Do not infer calibrated win probabilities from textbook payoff ratios or LLM confidence. The existing numerical experiment failed and remains historical. The paper-trading duration requirement cannot be compressed into a longer fine-tuning job.

## Deliverables at completion

Provide the private adapter with hashes, fixed base revision, source/disposition ledger, frozen datasets/splits, reproducible cloud code, runtime record, baseline/candidate answer comparisons, independent assessment and model card. Include exact manual continuation commands. Until those artifacts and required evidence exist, describe the result as experimental rather than a completed crypto expert.
