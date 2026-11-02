# Diagnostic016 review ? 2026-10-21

24 outputs inspected: six exposed cases x multi/selected evidence x base/adapter015. All valid JSON, no truncations. No fitting performed.

Manually selected relevant evidence fixes adapted RSI, VWAP and StochRSI answers. VWAP improves in the base too. Leverage remains10 instead of4 in both models and both evidence conditions. Cold-storage and payoff answers are correct here. Payoff differs from original015 despite identical model weights; runtime/generation context differs, so do not claim perfect reproducibility or an isolated causal estimate across jobs. Within-job comparisons support distractor sensitivity, not universal retrieval success.

Decision: SFT017 addresses distribution mismatch:108 original single-passage exercises plus58 multi-passage versions of supported rows, with three distractors drawn exclusively from the existing training bank. Same answers and source provenance; relevant evidence positions shuffled with seed217. Existing numerical applications are included. No test targets moved into training, no new PDF coverage. These are correlated exercises, not58 independent facts. Previously exposed development tests remain unsuitable for final acceptance.

Fresh pinned Qwen3-8B, all-linear rank8, LR1e-5, two epochs. Reject promotion if severe arithmetic, attribution or polarity errors persist. Full-library review and independent acceptance remain unfinished. Product discovery/voice/continuous monitoring not implemented by this training.
