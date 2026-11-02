# Diagnostic 005: adapter007 does not fix the known failures

Reviewed 23 September 2026. Private cloud inference job: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-adapter-diagnostic-005 . Downloaded status.json reports complete; all16 base and16 adapter answers were read. No fitting occurred in this job. The Kaggle UI/API can lag behind the completed output record during finalization.

The same16 frozen diagnostic004 evidence packets and prompt were used for both conditions. The cloud script verified the adapter007 SHA-256 before loading it. Both conditions use the same pinned base revision and deterministic generation. This is an exposed development diagnostic, not an independent acceptance test.

## Findings

Both known blocking errors remain, with identical answers between base and adapter:

- **Sell-limit direction:** both describe a maximum price to receive on a sell. The relevant price constraint is a minimum acceptable selling price; neither wording nor citation is acceptable as written.
- **Unidentified source:** both attribute the retrieved NOBI equation and sign convention to a paper explicitly not supplied or identified. The displayed convention may be correct for the retrieved paper, but that does not identify the user's paper. They should request identity/equation or clearly label a conditional example.

Candles, trend, stop trigger, RSI, holder counts, contract verification, receipt tokens, oracle trust, stablecoin reserves and article/data licensing largely retain the base's correct conclusions. Historical/current-data distinctions generally work, although the historical-report answer still assumes a specific source date. Both abstain on a missing chart, an unavailable current unlock schedule and a guaranteed doubling coin. The adapter sometimes shortens answers but shows no clear substantive reliability improvement.

No answer hit its generation limit. All cited IDs exist in the supplied context; the unidentified-source failure demonstrates why that is insufficient. The candlestick answer also overstates absence of predictive information when the supported claim is absence of a guarantee. The guarantee answer generalizes about whole documents from limited passages. These qualifications further argue against an expertise claim.

**Decision: adapter007 fails the frozen development gate and is not promoted.** Preserve the negative result. Run008 had already been submitted as a fresh corrected-curriculum experiment before these outputs were inspected; its immutable plan explicitly records the pending diagnostic. Do not imply that run008 was tuned after seeing these results or that it fixes them. Its source-support contrasts address the general attribution problem; future evaluation must directly verify sell-limit direction as well.

Evidence: `results/pdf_adapter_005_v1/pdf_adapter_005/{base.json,adapter007.json,protocol.json,status.json}` and `notebooks/pdf_adapter_eval_005/review_protocol.json`. Structural verification is recorded in local_review_checks.json beside the downloaded answers.
