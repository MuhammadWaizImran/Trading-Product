# Latest verified status: run 008 complete

Run 008 completed all fitting, validation, answer generation and saved-model reload checks. Its artifacts are downloaded and verified. All 36 base/adapted answer pairs were read; unsupported reasoning remains, so the adapter is not accepted. Read [run 008 results](PDF_SFT_008_RESULTS.md).

No fitting job is currently active. Private diagnostic006 has been submitted for the required source-attribution and order-definition comparison. This is cloud inference, not additional training. Do not confuse completion of fitting with model acceptance. Older running-status notes below are historical.

## Next manual step

Check the diagnostic without submitting a duplicate:

```powershell
$env:PYTHONUTF8='1'
tmp/kaggle_client/Scripts/kaggle.exe kernels status waizimran/crypto-qwen3-pdf-adapter-diagnostic-006
```

After COMPLETE:

```powershell
tmp/kaggle_client/Scripts/kaggle.exe kernels output waizimran/crypto-qwen3-pdf-adapter-diagnostic-006 -p results/pdf_adapter_006_v1
```

Read status.json, protocol.json, base.json and adapter008.json in the downloaded pdf_adapter_006 folder. Require 16 matching IDs in each answer file and no truncation. Compare every answer with the frozen evidence and rubric in notebooks/pdf_adapter_eval_006. Especially inspect minimum selling price, unidentified source identity, missing charts and unsupported current claims. Record the result before proposing another fitting run. Do not run the evaluator or trainer on the laptop.

---

Latest live check: all 53 optimizer steps of run 008 finished (one epoch; 35.9 minutes of fitting). Kaggle still reports running while post-training validation and answer/reload checks remain. The full job and quality review are not complete.

# Cloud run 008 submitted and running — 23 September 2026

Private job: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-008 . Version1, run352135817. Submission accepted; browser inspection confirmed PRIVATE, GPU T4 x2 allocation and successful cloud preflight/dependency installation. The trainer uses GPU0 only. Subsequent optimizer logs confirm epoch0.25 at elapsed1580seconds. Fitting is underway, not complete; this is progress within this run only.

212 training examples from selected material in ten PDFs, plus36 validation and36 development-test cases. This includes the60 previously staged examples and additional exercises for irrelevant citations and unidentified authors. Run008 starts from the original pinned Qwen3-8B base, not adapter007. The frozen plan and decision criteria are in [PDF_SFT_008_PLAN.md](PDF_SFT_008_PLAN.md). Static payload/source checks passed; the cloud tokenizer performs the actual length check.

Run007 completed and passed artifact checks, but has no demonstrated reliable advantage and is not accepted. Diagnostic005 has now completed and all32 answers were reviewed. Adapter007 retains both the sell-limit direction and unidentified-source errors; see [findings](PDF_ADAPTER_005_RESULTS.md). Run008 was submitted as a separate corrected-curriculum experiment, without assuming that pending diagnostic passes. Both jobs are private and cloud-only.

The former staged modules are now part of submitted run008; do not call them trained until completion. The [coverage ledger](PDF_COVERAGE_LEDGER.md) separates completed007 from submitted008. Other PDF material, independent acceptance, visual chart capability, market prediction and prospective paper evaluation remain unfinished. No model is certified expert or profitable.

## Continue manually

From the project PowerShell terminal:

```powershell
$env:PYTHONUTF8='1'
tmp/kaggle_client/Scripts/kaggle.exe kernels status waizimran/crypto-qwen3-pdf-sft-008
tmp/kaggle_client/Scripts/kaggle.exe kernels status waizimran/crypto-qwen3-pdf-adapter-diagnostic-005
```

Do not submit duplicate jobs. When each reports COMPLETE, download:

```powershell
tmp/kaggle_client/Scripts/kaggle.exe kernels output waizimran/crypto-qwen3-pdf-sft-008 -p results/pdf_sft_008_v1
tmp/kaggle_client/Scripts/kaggle.exe kernels output waizimran/crypto-qwen3-pdf-adapter-diagnostic-005 -p results/pdf_adapter_005_v1
python scripts/audit_pdf_run.py --batch 008 --results results/pdf_sft_008_v1/pdf_sft_008
```

The audit does not load or train a model. Inspect every paired answer and its evidence, not just loss or citation existence. Review all32 diagnostic answers against its frozen rubric. Write result reports and decisions before further fitting. On failure preserve logs and diagnose; never fall back to laptop fitting. Keep datasets, notebooks and adapters private.

Only after008 has actually finished successfully, update coverage with:

```powershell
python scripts/validate_staged_curriculum.py --completed-batch 008 --active-batch none
```

An execution-complete ledger does not approve the model. Follow PDF_MODEL_ACCEPTANCE_PROTOCOL.md for the separate quality gate.
