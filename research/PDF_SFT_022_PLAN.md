# Run022: targeted grounding correction

Model: pinned Qwen/Qwen3-8B revision b968826d9c46dd6066d109eabc6255188de91218. Fresh all-linear rank8 QLoRA adapter, alpha16, dropout0.05, learning rate1e-5, two epochs, seed217. It does not resume017 optimizer state or overwrite that adapter. Only hosted Kaggle/Colab execution is permitted by the notebook guard; CUDA is required.

190 training examples: retain166 from017 plus24 original contrastive exercises (12 supported,12 insufficient), grounded in existing reviewed PDF adaptations. No new PDF coverage. Seven source documents remain represented in the retained set; private permission basis and page/file hashes persist in each row. Library-wide review remains unfinished. System prompts are aligned to021 in fitting and evaluation, so this is a combined curriculum/prompt-alignment intervention, not a clean single-variable ablation.

Six existing validation probes remain diagnostic, not independent acceptance. Evaluation uses16 exposed021 regression cases and12 newly authored questions excluded from training. The new questions use known passages and correlated templates: they are a held-out diagnostic split, NOT independently authored acceptance. Every expected numeric value was checked while preparing the examples. Test reference answers are excluded from model prompts.

Same-run unadapted base, newly fitted adapter and reloaded adapter each generate28 answers with thinking enabled, seed217, temperature0.6, top-p0.95, top-k20 and2048-token cap. Training remains non-thinking direct-answer SFT, as before; evaluation tests whether the corrections transfer to thinking-mode inference. Training source hash:93c4146600806f673a7aa6cb5aadec7d4dd3041629c820c10596d001c8a57b90.

## Predeclared review and stop rules

Read every final answer against the actual passage. Report schema, expected status/citation, arithmetic, unsupported verdicts, unknown-source attribution and truncation separately. Any unsupported unknown-source assertion blocks approval. Relevant-evidence questions must retain correct numerical/negative answers rather than learning blanket refusal. Compare with same-run base;017's021 results are historical context, not a matched same-run comparison for all questions. Do not treat lower loss or training completion as success.

No automatic successor training. If this bounded run does not resolve the targeted failures, preserve failures and prioritize constrained tool-backed responses and better independent evaluation rather than blindly extending epochs. Even a clean diagnostic run does not certify trading performance or authorize live agents.

## Manual continuation

```powershell
tmp\kaggle_client\Scripts\kaggle.exe kernels status waizimran/crypto-qwen3-pdf-sft-022
tmp\kaggle_client\Scripts\python.exe scripts/download_pdf_artifacts.py --batch 022 --dest results/pdf_sft_022_v1
```

Inspect status.json before claiming fitting started/completed. Expected stages: cloud_preflight, installing_dependencies, loading_model, baseline_evaluation, training_pdf_examples, adapter_evaluation, completed_training_human_evaluation_pending. A Kaggle running status alone does not establish active fitting. Inspect failure.txt if present, require result.json and all28 records in each answer file. Review final_response, not hidden reasoning or only JSON format. Compare original/reloaded outputs and preserve the adapter hash. Runtime and manifest record actual GPU/packages/data hashes. No laptop fallback, paid compute or public upload is authorized.
