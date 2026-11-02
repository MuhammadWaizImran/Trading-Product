# Qwen3-8B PDF continuation run 002

Run 002 completed on Kaggle on 21 September 2026. It continued the adapter from run 001 and added selected, reviewed material from DP07, *Introduction to On-Chain Analysis*. It did not ingest every page verbatim and does not represent the whole uploaded library.

## Execution evidence

- Private notebook: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-002
- Version 1; completion recorded at 2026-09-21 13:33:13 UTC.
- GPU: Tesla T4; CUDA 12.8. All fitting and generation ran on Kaggle.
- Model: Qwen/Qwen3-8B, exact revision `b968826d9c46dd6066d109eabc6255188de91218`.
- Parent adapter SHA-256: `ed3b93060137da7d7aa1e30b1682d91a665988070e07bfe82f1e371cc7fffb76`.
- New adapter SHA-256: `8e111a2cb193b246ca1fd1c6e4a1c181d8d439d636193a8a5b6c401f5ba561e2`.
- Four-bit base model with the existing rank-8 LoRA adapter; two epochs, 24 optimizer steps, 323.4 seconds of fitting.
- Cumulative data: 48 training, eight validation and eight test records. The training split contains 24 replayed examples from run 001 and 24 new DP07 examples.
- The local frozen manifest exactly matches the downloaded cloud manifest. Adapted and reloaded answer files are byte-identical (`b1cdf14505853e7060cf58e40d5dbd93be0c7c76930d7d4f79b713735b5454dc`).

## Metrics

Validation completion loss fell from 6.0939 for the parent adapter to 3.8143 after continuation. Training loss was 3.9169. This is a token-prediction result on eight reference answers, with source/concept overlap. It is not general accuracy, market prediction performance, or evidence of profit.

## Manual answer review

Four new DP07 application questions were reviewed against the frozen references:

| Question | Parent adapter | New adapter | Review |
| --- | --- | --- | --- |
| Direct holdings plus protocol deposit | Pass | Pass | Both recognize that the displayed USD 900 omits the USD 600 protocol position. |
| Addresses versus investors | Pass | Partial | The new answer notes that one entity may control several addresses, but omits the explicit converse in the question: one exchange address may represent 400 customers. |
| Transfer to a service and ownership attribution | Pass | Pass | Both reject ownership attribution from one transfer and request more evidence. |
| Private entry price versus current price | Pass | Pass | Both correctly distinguish USD 100 historical cost from USD 1,000 current cost. |

The new adapter meets the predeclared minimum of three clear passes out of four, but it does not improve on the parent's four passes. It slightly reduces completeness on the holder-count case. Therefore this batch adds source coverage but does not demonstrate superior answer quality.

Four older retention questions all reached the 384-token limit for both parent and new adapter. Their visible portions correctly discuss depth differences and persistent high RSI, but the NOBI response again invents unsupported acronym expansions because the old question does not identify its source convention. The reward/risk response uses an incorrect expected-value formula before truncation. These incomplete generations cannot receive full-answer passes. The evaluation reused the original under-specified NOBI question; that is a protocol defect, preserved rather than hidden. Future runs will use a fixed concise evaluation prompt and explicit source context.

## Decision

Keep the adapter as the cumulative parent for the next reviewed batch because training completed, artifacts reload exactly, DP07 coverage was added, and no severe regression appeared on the four new checks. Do not promote it as an expert or deploy it for trading decisions. New independent evaluation remains required, and deterministic code should handle arithmetic and risk calculations.

Artifacts: `results/pdf_sft_002_v1/pdf_sft_002/`. The cloud `status.json` retains `human_evaluation_pending` as execution-time evidence; this report records the later manual review without altering that artifact.
