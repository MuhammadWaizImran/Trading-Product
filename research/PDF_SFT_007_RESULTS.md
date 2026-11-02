# Run 007: execution complete, model not accepted

Reviewed 23 September 2026. Private cloud run: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-007

The cloud completion record is 07:26:48 UTC. Fitting took 1,355.8 seconds (22.6 minutes), 34 optimizer steps, one epoch on a Tesla T4. The complete job also included setup, baseline generation, validation and adapter reload checks. This is selected PDF-derived educational training, not a completed trading product.

## Artifacts and coverage

Qwen/Qwen3-8B at revision `b968826d9c46dd6066d109eabc6255188de91218`, fresh rank-8 QLoRA adapter. 136 training records, 20 validation, 20 development-test records. The training set comprises 124 canonical adaptations plus 12 evidence/abstention variants from selected material in DP01, DP03, DP04, DP05, DP06, DP07, DP17 and DP19. No claim of whole-document or whole-library ingestion. The user's private-training permission is retained in the manifest/attribution; redistribution is not authorized.

`results/pdf_sft_007_v1/pdf_sft_007/local_artifact_audit.json` passed: local/cloud manifests and split hashes match, expected model revision, finite training loss, complete answer IDs and exact adapted/reloaded answer equality. Adapter: 15,354,512 bytes; SHA-256 `98fd7f25a9f2dc9b3518e7a742bd805ccbc79d67a14d8abe872d07559a304f99`. The immutable cloud result retains its original review-pending status; this report records the subsequent review.

Validation loss fell from 6.2713 to 5.2753; training loss was 1.0587. Validation references do not consistently match the citation/evidence task, so this decrease is diagnostic and cannot establish reliable improvement.

## Answer review and decision

All 20 base/adapted pairs were read. The adapted outputs had no unrecognized citation IDs or output-limit truncations. Those structural checks do not establish citation support. Many answers are identical or nearly identical, and evidence helps the base model too.

- Counterparty ownership: both models cite `dp01-hot-cold` for an attribution claim that this custody passage does not establish. The main conclusion is sensible, but the citation is not adequate evidence.
- Unidentified capacity report: both assume the user's unspecified report is the retrieved 2018 report. Retrieval is not proof of source identity.
- Reserve-chart date: the adapter adds a relevant citation while both correctly decline to infer current shares from a historical chart.
- Permissioned participation: the adapter states the given access restriction more directly; this is a limited wording improvement.
- Book-imbalance sign, reward/probability and RSI examples: both answer correctly with supplied evidence. These are not demonstrated gains from fitting.

**Decision: preserve the adapter for diagnosis; do not promote it or declare expertise.** The small, exposed, concept-overlapping development set does not show a clear reliable advantage over the identically prompted base. No profitability, all-coin forecasting, visual chart interpretation or independent application accuracy was established.

Next: replay the existing 16-case retrieval diagnostic with identical evidence for base and adapter007, specifically checking source identity and sell-limit wording. Freeze its criteria before observing outputs. This is development diagnosis, not an independent acceptance test. Sixty additional training records from four reviewed modules remain staged and unfitted; do not blindly append them to an unaccepted adapter.
