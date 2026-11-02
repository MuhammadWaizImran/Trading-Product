# SFT014 review — 2026-10-06

Cloud fitting completed:108 examples, two epochs,54 steps,33.77 minutes. All-linear rank8 adapter has21,823,488 trainable parameters. Validation loss on six overlapping probes fell2.96765 to0.88712; not an independent accuracy measurement.

All50 baseline and50 adapted answers inspected. Artifact audit passes and50 reload answers match. Format compliance48/50 both. Adapter repeats StochRSI answer to token limit, producing invalid JSON; ownership answer combines insufficient status with a citation.

Some evidence-based negative conclusions improve (depth, correlation, dated capacity, backup scope). Severe failures remain: leverage10 instead of4; contradictory RSI conclusion; unsupported identification of external reports; unnecessary VWAP abstention; verdict from irrelevant VWAP evidence. Cold-storage answer introduces an unsupported destroyed-backup premise. No promotion.

Run015 version1 submitted successfully: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-015 . Controlled change: learning rate2e-5 to1e-5. Same108 examples, prompt, splits, fresh pinned Qwen3-8B, all-linear rank8 and two epochs. Test whether smaller updates reduce regressions. If serious failures persist, stop repeating this narrow recipe and diagnose data distribution and evidence handling. No new PDF coverage or independent acceptance.

Preflight015 passed. Code SHA256:02f88c44b19d1b8015f8943c8d68b1635da55a3e42b65d032a8ec626e14899f1. No local model execution.
