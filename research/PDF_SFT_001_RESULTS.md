# Qwen3-8B: first PDF-derived fine-tuning result

Training completed on Kaggle on 2026-09-21. This is a small pipeline pilot using selected material from four supplied PDFs, not training on every uploaded document.

## Execution evidence

- Private notebook: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-001
- Kernel 135203929, version 1, run 351509199.
- Completion recorded at 2026-09-21 07:46:15 UTC.
- Actual training GPU: Tesla T4. The session offered T4 x2; code used one GPU.
- Model: Qwen/Qwen3-8B, exact revision b968826d9c46dd6066d109eabc6255188de91218.
- Four-bit base weights; rank-8 LoRA adapters on query/value projections, alpha 16, dropout 0.05.
- 24 training examples, four validation examples, four initial test examples.
- One epoch, six optimizer steps, approximately 81 seconds of fitting. Model download/setup/evaluation took additional time.
- All fitting and inference ran on Kaggle. Local work prepared data, submitted jobs and downloaded artifacts.

## Data coverage

The examples paraphrase and clarify reviewed passages from Crypto Wealth Academy's introductory technical-analysis PDF (DP05), Elisa Crypto's Risk Management (DP06), Binance Academy's trading ebook (DP17), and Order Book Liquidity on Crypto Exchanges (DP19).

The user attested permission to use the uploaded collection for training. DP19 also states CC BY 4.0. Each example records filename, source hash, PDF page numbers and adaptation notes. Duplicates, unread sections, advertisements and known erroneous claims were not automatically ingested. This is 24 actual training examples, not 32: the remaining eight were excluded from fitting.

## Initial result and limitations

Validation completion loss fell from 5.5023 to 5.1177. This is a token-prediction metric on only four reference answers. It is not a trading accuracy, a general knowledge score, or evidence of profitable decisions.

The saved adapter was reloaded on Kaggle. The adapted and reloaded answer files have identical SHA-256 hashes (70e982866bfe8745273da7f7116a8bc50d3c9e94abb3cb682fcacf661b8dd02e), confirming reproducible outputs for that check.

Manual inspection found a serious hallucination in both baseline and adapted responses: an unidentified-paper question about NOBI produced a fabricated expansion rather than a source-grounded interpretation. The question itself was under-specified because it did not supply or identify the paper. All four initial responses were visibly cut short at the generation limit, so those responses cannot support a complete-answer accuracy score. The adapted depth answer also overstates that a large buy necessarily pushes price up; available depth and order size determine this.

Decision: the cloud training pipeline worked and produced a usable adapter file. Expert-level knowledge, improved factuality and trading performance are NOT established. Do not advance to production or real trading.

## Follow-up diagnostic

A separate inference-only job completed at https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-evaluation-001 (version 1, run 351584047). It compared base and adapter with eight explicit questions, a concise-answer instruction, larger output allowance, and EOS/truncation recording. All 16 responses ended normally; none reached the token limit. The loaded adapter hash matches the saved training artifact. This is a post-inspection diagnostic, not an untouched confirmation test. No further fitting or tuning was performed on these questions.

All 16 complete responses were manually reviewed against the stored rubrics. Both models had the same substantive outcomes:

| Case | Outcome for both | Evidence |
| --- | --- | --- |
| Exchange depth | Partial | Acknowledges liquidity/slippage differences, but adds an unsupported identical-order-books assumption. |
| Unidentified paper | Pass | Acknowledges missing definition/context instead of inventing NOBI's meaning. |
| Supplied imbalance formula | Fail | Reverses the supplied formula and gives 0.4; the correct result is (60-100)/160 = -0.25, indicating more displayed bid depth. |
| Fixed-payoff break-even | Fail | Gives 1/4 instead of 1/5 = 20%; correctly says actual win probability is unknown. |
| RSI persistence | Pass | Recognizes that high RSI does not require immediate reversal. |
| Position sizing | Fail | Gives $200 notional and $6 loss instead of $2,000 and $60. |
| Missing stop | Fail | Invents a quantity despite missing loss per coin and incorrectly says partial coins cannot be traded. The adapter explicitly assumes an unsupported $20 stop loss per coin. |
| Profit guarantee | Pass | Does not treat books or fine-tuning as proof of trading profits. |

Thus each model has three passes, one partial and four failures on this small diagnostic. Five of eight answer strings are identical. This is not a general accuracy estimate: the cases were selected after inspecting earlier responses and overlap reviewed concepts. The disappearance of the earlier acronym hallucination cannot be attributed to fine-tuning because the revised baseline also handles it correctly.

**Decision: no demonstrated answer-quality gain; do not promote this adapter as a reliable trading expert.** Preserve the run as a successful pipeline check with an unsuccessful quality demonstration. More epochs alone are not justified by this result. Next work should expand independently reviewed source-derived examples, include checked calculations and missing-information cases, and establish a fresh evaluation set before another cloud run. Numerical risk calculations should ultimately use tested deterministic calculations rather than rely on generated arithmetic. Full PDF and chart review remains unfinished.

Diagnostic evidence: results/pdf_sft_eval_001/pdf_evaluation_001/{protocol,base,adapted,status}.json and the downloaded kernel log. The cloud status retains manual_review_required=true as original evidence; this report records the subsequent manual review without rewriting cloud artifacts.

## Artifacts

Local directory: results/pdf_sft_001_v1/pdf_sft_001/ . Contains runtime.json, dataset_manifest.json, result.json, before/after/reload answers and adapter/.

The adapter is 15,354,512 bytes. SHA-256: ed3b93060137da7d7aa1e30b1682d91a665988070e07bfe82f1e371cc7fffb76. It requires the exact base model revision above; it is not a standalone eight-billion-parameter model. The base weights were not downloaded to the laptop. The adapter_config.json has a null revision field, so consumers must use runtime.json's explicit revision when loading the base.
