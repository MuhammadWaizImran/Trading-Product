# Run 008: broader corrected curriculum and evidence-support training

Prepared 23 September 2026. This plan is not evidence that training completed.

The user authorized continued cloud training. Run007 completed but is not accepted: both it and the base made unsupported citations and assumed an unidentified source. Diagnostic005 is still running at preparation time. Run008 is a fresh experiment from the pinned original base, not a continuation or promotion of adapter007. Diagnostic005 must still be reviewed; its results cannot retrospectively change this frozen dataset or criteria.

## Data and changes

212 training examples = 184 canonical PDF adaptations + 28 constructed evidence/identity exercises. The 60 newly incorporated canonical records cover selected DP05 technical analysis, DP10 corrected risk arithmetic, DP17 execution/indicators and DP16 signature/custody foundations. Selected sources are DP01, DP03, DP04, DP05, DP06, DP07, DP10, DP16, DP17 and DP19. Full books, the other distinct works and chart images are not included.

The eight new pairs of exercises contrast related questions with unrelated evidence and with an unidentified author. They explicitly teach that finding a citation ID does not make it supporting evidence. Supported passages vary in position among distractors. The system prompt requires source support rather than filling evidence gaps from memory. These changes target observed failure modes; they are not evidence the failure is fixed. Supported examples still contain answer-like adaptations, so copying remains a limitation.

36 validation and 36 development-test cases are used. Earlier cases are exposed and newer cases overlap training concepts. Evaluation evidence is retrieved only from canonical training adaptations; no test reference is inserted. References can exceed retrieved support and omit citation targets, so validation loss is not a promotion measure. Adding material changes retrieval conditions; compare the within-run base and adapter, not raw scores from earlier runs.

Each record retains source filename, hash, PDF page, private-permission basis and adaptation description. Source errors are corrected rather than taught as facts. User-attested permission is not a verified universal open license; artifacts remain private.

## Configuration and decision

Qwen/Qwen3-8B revision `b968826d9c46dd6066d109eabc6255188de91218`, fresh rank-8 q/v QLoRA, NF4, one epoch, learning rate 0.00002, seed217, batch1/accumulation4, maximum2048 tokens with refusal of silent truncation. All fitting and generation run on Kaggle. No local model execution. GPU allocation/quota are subject to the account and provider; cloud guards refuse CPU/laptop fallback. Provider documentation: https://www.kaggle.com/docs/notebooks .

Before considering further continuation, review all36 base/adapted answer pairs with identical evidence. Require a clear increase in fully supported correct answers, no newly introduced severe factual/risk/source error and no truncated answer. Also assess source identity and citation support in a separate development stress comparison. Artifact hashes and reloaded answers must match. No automated promotion or retry; preserve negative outcomes. Even passing development checks requires independent assessment under PDF_MODEL_ACCEPTANCE_PROTOCOL.md. No profit or all-coin prediction claims follow.

Run007 fitting took22.6minutes for136 examples. Run008 has212 examples and more evaluation: roughly an hour or more for the whole job is a planning estimate, not a deadline. Queueing, GPU availability and runtime behavior can change this. The whole product has no reliable completion estimate yet.

## Manual continuation

Do not execute `notebooks/pdf_sft_008/train.py` locally. Check the private cloud job before any submission to avoid duplicates:

```powershell
$env:PYTHONUTF8='1'
tmp/kaggle_client/Scripts/kaggle.exe kernels status waizimran/crypto-qwen3-pdf-sft-008
```

Once COMPLETE, download and audit:

```powershell
tmp/kaggle_client/Scripts/kaggle.exe kernels output waizimran/crypto-qwen3-pdf-sft-008 -p results/pdf_sft_008_v1
python scripts/audit_pdf_run.py --batch 008 --results results/pdf_sft_008_v1/pdf_sft_008
```

Read every answer and the corresponding supplied evidence after the audit passes. Write a new results report with errors, changes versus base and an explicit decision. Structural pass is not model acceptance. If ERROR, preserve logs and failure.json/status.json as available, diagnose before submitting a versioned correction, and never fall back to laptop training.
