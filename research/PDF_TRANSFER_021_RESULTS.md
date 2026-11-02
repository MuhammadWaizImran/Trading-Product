# Run021 answer review — 2026-10-28

Reviewed all32 final answers against the16 question/evidence pairs. Both output files are complete and no records hit the output cap according to structural review. This is the author/agent's review, not independent expert adjudication.

| Measure | Base | Adapter017 |
|---|---:|---:|
| Valid response schema |16/16|16/16|
| Expected status and citation |16/16|15/16|
| Strict grounded-answer review |13/16|14/16|

The last row is a narrow protocol-compliance judgment, NOT trading accuracy or a statistically established adapter advantage. Known passages and only16 correlated cases cannot establish general expertise.

## Specific failures

- Base `rsi-missing`: states the RSI formula and75 despite no RSI evidence. Number correct, evidence-only rule violated.
- Base `depth-missing`: gives20.50 and a fill verdict under insufficient. Arithmetic follows the scenario, but the deliberately strict missing-rule protocol requires abstention. This is a protocol-dependent grounding failure, not an arithmetic error; a product with a deterministic calculator can handle such questions differently.
- Base `report-unidentified`: says the report contradicts the proposition before admitting its title/text is unknown. This is unsupported attribution inside an otherwise correct insufficient envelope.
- Adapter `leverage-missing`: supplies128 and4x, then admits evidence does not cover leverage. Numbers correct; fails the evidence-only abstention contract.
- Adapter `report-unidentified`: falsely says the report contains the supplied custody facts and cites that unrelated passage as the report. This is the status/citation mismatch already detected automatically.

Both correctly answered all eight supported questions, including leverage, VWAP, RSI, depth and custody/offline-receipt limitations. Base survey response distinguishes the provided evidence from the unknown survey, so it was accepted with a verbosity note. Both custody-missing responses describe a lack of evidence rather than asserting the real-world conclusion; accepted. Offline-receipt wording is interpreted within the stated sender/valid-address scenario, not as an unconditional guarantee of payment execution.

## Decision

Do not promote either model. Automatic100% format/status scores hid substantive failures. A bounded correction experiment is justified by the repeated pattern: insufficient responses must not leak unsupported answers, and unidentified outside documents cannot inherit nearby passage facts. Run022 adds original contrastive exercises without moving021 answers into fitting. The application source guard and manual semantic review remain necessary; improving model compliance alone cannot establish a trading edge.
