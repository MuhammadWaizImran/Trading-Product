# Run009: source attribution contrasts

User authorized continued private cloud training. Adapter008 fixed sell-limit direction in diagnostic006, but still assumed the identity of an unspecified paper. The next controlled experiment adds18 exercises to the212 existing records: six matched sets of identified-source answers, unidentified-source abstentions and irrelevant-evidence abstentions. All derive from previously reviewed passages with PDF page/hash/permission provenance. No new PDF coverage is claimed.

230 training,36 validation and44 development-test records. The eight added development cases include three unidentified sources and five supported applications; their evidence is manually selected from training passages. They assess answering, not retrieval. The older36 retain their frozen prompts. All tests overlap development concepts and cannot certify independent expertise.

Fresh Qwen3-8B adapter from the same pinned revision; same rank8 q/v QLoRA, one epoch, learning rate2e-5, seed217 and batch/length settings as008. Do not load008 as parent. All model execution is private on Kaggle; no laptop fitting. Provider availability is subject to account quota. Official references checked during preparation: https://www.kaggle.com/docs/notebooks and https://huggingface.co/Qwen/Qwen3-8B .

Before any outputs: require all three new unidentified-source answers to request source identity without assigning retrieved details; require all five identified/application checks correct with supporting citations; no severe source/risk error on old cases; and clear improvement over the same base under identical prompts. Require full artifact/hash/reload checks and no output truncation. Falling loss is insufficient. If source identity persists, change the answering pipeline before further SFT; do not run an automatic retry loop. Passing development checks still requires independent assessment under PDF_MODEL_ACCEPTANCE_PROTOCOL.md.

An approximately80-minute full run is a planning estimate based on008, not a deadline. No percentage of total expertise or full-product completion is implied.

Manual continuation (after confirming COMPLETE, never execute train.py locally):

```powershell
$env:PYTHONUTF8='1'
tmp/kaggle_client/Scripts/kaggle.exe kernels status waizimran/crypto-qwen3-pdf-sft-009
tmp/kaggle_client/Scripts/kaggle.exe kernels output waizimran/crypto-qwen3-pdf-sft-009 -p results/pdf_sft_009_v1
python scripts/audit_pdf_run.py --batch 009 --results results/pdf_sft_009_v1/pdf_sft_009
```

Read all44 base/adapted answer pairs and write a result/decision report. Preserve errors. No real-order functionality, publication, profitability claim or Part3 approval follows from this run.
