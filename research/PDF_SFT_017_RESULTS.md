# SFT017 results ? 2026-10-21

166 training exercises, two epochs,73.68 minutes fitting. Validation loss0.97320 after fitting on six overlapping development probes. Artifact checks pass;50 saved-adapter reload responses equal original adapted responses. All50 adapted responses read; baseline verified identical to previously reviewed015 baseline. JSON contract50/50 adapted versus48/50 base, no truncations. This is format compliance, not semantic accuracy.

No promotion: leverage still10 instead of4; RSI answer contradicts itself; VWAP and scale questions incorrectly refused; unknown-report attribution still wrong. New severe regression: offline-receiving answer cites unrelated exchange-holder passage. Some depth, correlation and payoff answers improve. Supported-only mixed-evidence augmentation did not resolve grounding and may bias toward answering; this is a hypothesis, not a causal claim.

Run018 tests previously unused thinking mode before more fitting. Eight exposed questions x base/adapter017 x thinking off/on =32 generations. Same sampling settings across conditions (temperature0.6, top_p0.95, top_k20, seed217) and2048-token output ceiling. Not comparable directly with historical greedy decoding. Shared token cap gives thinking less final-answer space; truncation must be reported as inconclusive, not successful reasoning. Single-seed diagnostic, no independent acceptance. Raw output retained and final answer separated at </think> for review.

Official guidance: https://huggingface.co/Qwen/Qwen3-8B recommends sampling rather than greedy decoding for thinking mode. Adapter017 was trained on non-thinking responses, so reasoning behavior is unvalidated. No new fitting, local model execution, public data or real orders.
