# Current checkpoint: run 009 submitted

Private Kaggle run009 has been submitted: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-009 . It uses230 training examples from selected material in ten PDFs,36 validation and44 development-test cases. Submission does not prove optimizer completion. No local training was executed.

Diagnostic006 is complete and all32 answers were reviewed. Adapter008 corrected sell-limit direction but still assumes the identity of an unidentified paper and sometimes omits citations. It is not promoted. See [diagnostic findings](PDF_ADAPTER_006_RESULTS.md).

Run009 starts from the same pinned base with unchanged fitting settings, adding18 source-attribution contrasts. It is a controlled follow-up, not an unlimited retry loop. If identity failures persist, change the answering pipeline before further SFT. See [frozen plan and manual commands](PDF_SFT_009_PLAN.md). The coverage ledger distinguishes completed008 from submitted009. No whole-library, expertise, profitability or product-completion claim is made.

## Continue manually

Do not execute train.py locally. Check before submitting anything to avoid duplicate jobs:

```powershell
$env:PYTHONUTF8='1'
tmp/kaggle_client/Scripts/kaggle.exe kernels status waizimran/crypto-qwen3-pdf-sft-009
```

Only after COMPLETE:

```powershell
tmp/kaggle_client/Scripts/kaggle.exe kernels output waizimran/crypto-qwen3-pdf-sft-009 -p results/pdf_sft_009_v1
python scripts/audit_pdf_run.py --batch 009 --results results/pdf_sft_009_v1/pdf_sft_009
```

Review all44 paired answers and supporting passages against the frozen criteria. Preserve both errors and gains in a new report before choosing further work. Check checkpoints/logs if ERROR; never use laptop fitting as a fallback. No automatic new training is scheduled after this job. Kaggle can execute the submitted job without the chat, but subsequent review requires active work here or manual continuation.

Earlier checkpoints below are historical where inconsistent.

---

