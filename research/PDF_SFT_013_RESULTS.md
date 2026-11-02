# SFT013 review — 2026-10-04

Training completed on cloud:108 selected PDF-derived exercises, two epochs,54 optimizer steps,2236.28 seconds (37.27 minutes) fitting. Six overlapping validation probes: loss2.96765 to1.65382. Not an independent accuracy benchmark.

All50 baseline and50 adapted responses inspected. Artifact audit passes;50 reloaded responses equal adapted responses. Structured contract48/50 for both base and adapter; this is format compliance, not semantic accuracy. No model promoted.

Important findings:

- RSI continuation question regresses: base correctly says continued price rise with high RSI is not logically inconsistent; adapter incorrectly says it is inconsistent.
- Both still copy10x leverage rather than calculating4x from250 equity and750 borrowing.
- Both falsely identify details of unspecified external reports (normalization denominator and survey size).
- Both unnecessarily abstain on VWAP, scale conventions and depth applications. Adapter still gives a conclusion on an irrelevant VWAP passage.
- Both now correctly answer SMA15,25% payoff break-even, stop-at-entry non-positive return and several negative conceptual questions. Because same-run base already succeeds, these are not evidence of learned gains over base.
- Schema failures change from throughput/chart in base to correlation/chart in adapter. Net48/50 unchanged.

Frozen013 manifest training_sources summary was inherited from72-example run and is stale. Actual108 rows span DP05:30,DP16:26,DP07:12,DP03:8,DP17:18,DP06:10,DP10:4. Frozen files are preserved;014 recomputes summary from actual rows. No undisclosed extra PDF review or whole-library ingestion.

Decision: bounded run014 tests broader adapter coverage. Hold dataset bytes, prompt, splits, model revision, rank8, alpha16, dropout0.05, seed217, learning rate2e-5 and two epochs fixed. Change q_proj/v_proj to all-linear; add trainable-parameter reporting. This is a capacity hypothesis, not a guarantee. PEFT documents this supported option: https://huggingface.co/docs/peft/v0.21.0/package_reference/lora . Runtime remains pinned to0.17.1, with cloud failure reporting if incompatible or insufficient GPU memory.

Stop promotion if severe attribution, arithmetic or polarity failures remain. Do not keep increasing runs blindly. Independent acceptance, full-library disposition and predictive evaluation remain outstanding. No local inference/fitting, publishing or real orders.
