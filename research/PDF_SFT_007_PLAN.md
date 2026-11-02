# PDF training run 007: evidence-based answers

Prepared 23 September 2026. **Preparation is complete; this file alone does not mean cloud fitting has started or completed.** Consult CURRENT_PROGRESS.md and Kaggle status.

## Why change the training design

Runs 001-006 fitted small PDF-derived datasets, but did not demonstrate reliable improvement. Diagnostic 003 showed that both base and adapter can correct specific failures when supplied checked evidence. Continuing to stack failed adapters is not justified. Run 007 starts a fresh adapter from the original fixed Qwen3-8B revision and teaches use of source evidence, citations and missing-evidence responses.

This is an educational explanation experiment, not a predictor of price or profit. It does not establish cryptocurrency expertise or complete the user's full-library request.

## Frozen data

- 124 reviewed PDF-derived question/answer records: 100 from the earlier dataset and 24 staged DP04 records.
- Eight constructed empty-evidence variants of training records, plus four source-identity variants, giving **136 training examples** in total.
- 20 validation and 20 development test records. Earlier tests are already exposed, and staged DP04 checks overlap training concepts. None is represented as an untouched final assessment.
- Selected sources: DP01, DP03, DP04, DP05, DP06, DP07, DP17 and DP19. Source filenames, permissions, hashes and PDF pages are in every record's provenance. Other documents remain outside this run; no whole-book or whole-library ingestion claim.
- Training contexts contain the checked adaptation supporting the answer plus up to two automatically retrieved distractors. This intentionally teaches evidence use, but can be an easy copying task; a low loss is not proof of generalization.
- Evaluation contexts contain up to four automatically retrieved **training** adaptations. Evaluation reference answers are never inserted into prompts. The evaluation corpus is larger than retrieval diagnostic 004's corpus because it adds DP04; scores across those jobs are not directly comparable.
- Validation references lack citation targets and may exceed what retrieved evidence supports. Validation loss is diagnostic only. The manual review must reward warranted abstention and inspect whether cited evidence actually supports each claim.

## Cloud configuration

Qwen/Qwen3-8B revision `b968826d9c46dd6066d109eabc6255188de91218`; fresh rank-8 LoRA on q_proj/v_proj; 4-bit NF4 base; one epoch; learning rate 0.00002; seed 217; batch 1 with gradient accumulation 4; maximum combined sequence 2048 with refusal to truncate silently. Only assistant tokens contribute to loss. No failed parent adapter is loaded.

Cloud runtime checks refuse laptop/CPU fallback. The notebook and outputs are private. The generated code records GPU, package versions, losses, baseline/adapted/reloaded answers and model files. It saves periodic checkpoints, but does not automatically select the best result or retrain after a failed gate.

Provider references checked during preparation: [Kaggle notebook settings](https://www.kaggle.com/docs/notebooks), [GPU usage guidance](https://www.kaggle.com/docs/efficient-gpu-usage), and [official Qwen3-8B model card](https://huggingface.co/Qwen/Qwen3-8B). Account quota and allocation remain subject to Kaggle; no unlimited or guaranteed free GPU claim.

## Review decision fixed before submission

Compare all 20 base/adapted answers under identical evidence. Check correctness, material contradictions, missing-information handling, citation existence **and support**, and truncation. Require more fully supported answers than the base, no newly introduced severe error, and no truncated response before considering a separate independent assessment. Matching a weak base is not improvement. Loss improvement alone cannot promote the adapter. Numerical truth must still come from tested calculators.

Even passing these development checks cannot approve Part 3. Full corpus review, broader independent evaluation, multi-coin market modeling and prospective paper trading remain separate requirements.

## Manual commands

Do not run `train.py` locally. Prepared files are in `notebooks/pdf_sft_007`; data is in `data/pdf_sft_batch_007`.

```powershell
$env:PYTHONUTF8 = '1'
tmp\kaggle_client\Scripts\kaggle.exe kernels status waizimran/crypto-qwen3-pdf-sft-007
tmp\kaggle_client\Scripts\kaggle.exe kernels output waizimran/crypto-qwen3-pdf-sft-007 -p results\pdf_sft_007_v1
```

Once outputs exist, check `pdf_sft_007/status.json`, `runtime.json`, `dataset_manifest.json`, `result.json`, and all three answer files. Compare local/cloud manifests exactly, hash the adapter, and compare adapted/reloaded responses. Preserve rejected results. Do not submit duplicate jobs just because the assistant is unavailable.
