# Phase 2: Qwen3-8B pilot

Authorized by the user's explicit request on 2026-09-21. This changes the earlier phase restriction; Part 1's PDF and playlist review is still incomplete.

## Scope

First experiment: adapt Qwen/Qwen3-8B to a small, original collection of checked risk-arithmetic and evidence-handling examples. No copied PDF passages, news articles, or third-party charts will be uploaded. This is a training-pipeline and response-quality pilot, not a comprehensive crypto curriculum or a trading strategy. All data, code and outputs remain private. No orders or trading-account integrations.

Cloud only: private Kaggle GPU session. Local work is limited to dataset construction, API orchestration, syntax and data checks. Training code must reject local execution before installing ML libraries or downloading model weights. No paid runtime is authorized.

## Predeclared comparison

Compare the unmodified model with the trained adapter on the same locked synthetic test cases. Train and test use disjoint prompts/numbers and different prompt templates. Shared mathematical concepts are intentional: this measures narrow generalization, not general crypto expertise. No hyperparameter selection from test results and no repeated training to improve that exposed test.

Record exact model revision, package versions, dataset hashes, seed, GPU and training logs. Measure numeric-answer correctness, valid JSON rate, and correct abstention when inputs are missing. Also measure held-out completion loss before and after. Do not equate a lower loss with profitable trading.

Pilot acceptance requires a saved reloadable adapter, finite training loss and no regression in held-out numeric correctness or missing-data abstention. Improvement is claimed only if at least one held-out behavioral metric strictly increases. Tiny synthetic test results cannot authorize production or establish profitability; an independent, broader human-reviewed evaluation remains required.

## Source documentation checked

- https://huggingface.co/Qwen/Qwen3-8B
- https://huggingface.co/docs/peft/developer_guides/quantization
- https://huggingface.co/docs/trl/sft_trainer
- https://www.kaggle.com/docs/efficient-gpu-usage
- https://www.kaggle.com/docs/api

Kaggle GPU access is quota- and account-dependent. Availability must be checked for this account; advertised limits are not a promise of an allocation.

## Execution status

LATEST: Version 1 FAILED during package installation, before model download or training. Retrieved cloud logs show repeated DNS resolution errors connecting to the package index, followed by pip failure after roughly 204 seconds. No adapter or trained checkpoint exists. The earlier RUNNING observation below was session status only. A separate private environment diagnostic is being prepared; the user now explicitly requests a PDF-derived corpus instead of another synthetic pilot.

Private Kaggle version 1 submitted successfully. Kernel ID 135200908:
https://www.kaggle.com/code/waizimran/crypto-qwen3-8b-pilot-001

Kaggle reports RUNNING. Returned server metadata independently confirms `is_private: true`, `enable_gpu: true` and internet enabled. This is session status, not yet evidence that gradient updates have begun. Training metrics and completion are pending.

The current Kaggle CLI returned `Not found` for the listing endpoint; a direct legacy endpoint returned HTTP 200. Kaggle CLI 1.6.17 successfully submitted version 1. No tokens were included in the notebook or output. Local checks validated 160 original training examples, 25 validation examples and 25 test examples and compiled the script without running it. No local model fitting occurred.

The bounded configuration runs one epoch, 20 optimizer steps, with rank-8 adapters on query/value projections and 4-bit base weights. It is not full-parameter training. Runtime compatibility, GPU allocation and memory fitness must still be confirmed from the cloud logs. Package versions are pinned; the cloud script records the exact model revision and installed environment.
