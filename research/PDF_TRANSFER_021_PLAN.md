# Run021: evidence-transfer diagnosis

Private cloud evaluation submitted and confirmed running on 2026-10-28:
https://www.kaggle.com/code/waizimran/crypto-qwen3-transfer-check-021

No fitting, no local model inference, no model promotion. Compare the pinned Qwen3-8B base with SHA-verified adapter017. Same prompt, seed, reasoning mode, sampling and 2048-output-token cap as020. New sixteen questions produce thirty-two answers. Source code hash: 1b9648a558c1d7ecfdc38aea6f0fc6dcd4e6e5991d042195de89653abbec1db5.

Six relevant-versus-missing evidence pairs cover total-exposure leverage, VWAP, RSI, execution depth, custodial attribution and offline receipt. Two additional pairs test unidentified reports versus identified passages. All sources are existing checked, page-traceable PDF adaptations under the recorded private permission basis. No new library-wide review or permissions claimed.

These are new author-reviewed diagnostic questions using known training passages. They are NOT an independently reviewed holdout and do not measure trading performance. Numbers and premises were checked when authored. Reference answers are excluded from model prompts by the cloud runner. Assertions verify unique questions and no exact question reuse from017 training or020. This is not a guarantee against semantic overlap.

## Decision rules fixed before seeing outputs

Report schema compliance, correct expected status/citation, truncation and manually reviewed factual correctness separately for each model and each contrast pair. An answer must not make unsupported factual assertions merely because it labels itself insufficient. Check all final responses, not just keyword/numeric matches. Never interpret automatic format checks as semantic accuracy.

Any source-attribution error remains a blocker. Good results here permit preparation of independently reviewed acceptance cases, not product promotion. If adapter results show no advantage, keep base as a baseline and avoid another blind training continuation. If failures form a coherent pattern, develop reviewed correction examples and a separately held-out test before any new cloud fitting. More epochs on the same material are not the default intervention.

## Manual continuation

From project root:

```powershell
tmp\kaggle_client\Scripts\kaggle.exe kernels status waizimran/crypto-qwen3-transfer-check-021
tmp\kaggle_client\Scripts\kaggle.exe kernels output waizimran/crypto-qwen3-transfer-check-021 -p results/pdf_transfer_021_v1
python scripts/review_transfer_eval_021.py --results results/pdf_transfer_021_v1/pdf_transfer_021
```

Inspect status.json and failure.txt if present. Kernel completion alone is not evaluation success; require both sixteen-record output files and completed diagnostic status. Read structural_review.json and manually score every reference/response against the actual evidence. Missing or truncated records count as failures, not exclusions. No background monitor or auto-started next training job is installed.
