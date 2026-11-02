# SFT012 review — 2026-10-01

Kaggle completed training on Tesla T4: 72 selected reviewed exercises, two epochs, 36 optimizer steps, 1005.30 seconds (16.76 minutes) fitting. Six overlapping validation probes: loss 3.35752 to 2.36506. This is not trading accuracy or an independent benchmark.

All 50 baseline and 50 adapted answers inspected. Artifact audit passes, and all 50 reloaded responses equal the adapted responses. Adapter SHA256: 01362a667c066accc5410d17b2d5dad1bdb602de071b36ea9c397f74a542ef8e. Structured contract passes: baseline 43/50; adapted and reloaded 44/50. Six adapted answers incorrectly combine insufficient status with a citation. No truncation identified.

Some status assignments improve (holder counts, token rights, VWAP specification), but decisive errors persist. Both models copy 10x leverage instead of calculating (250+750)/250=4x. Both attribute a specific normalization or survey size to an unidentified outside source. Many answers unnecessarily abstain despite relevant evidence or enough explicit premises, including stop-at-entry return, StochRSI scale and VWAP applications. ADX and other justified negative answers expose confusion between a false proposition and an unsupported answer. These failures block promotion; no comprehensive expertise or profitability established.

The complete CLI download failed during an intermediate optimizer checkpoint. Primary adapter and both answer files were already saved; remaining top-level results, manifest, runtime, status and reload answers were recovered through authenticated API downloads. Intermediate optimizer checkpoints are incomplete; do not use this directory to resume optimizer state. The final adapter passes the artifact audit.

Decision: one bounded corrective run013 from fresh pinned Qwen3-8B. Keep72 exercises; add14 negative-but-supported answers,14 unknown-document abstentions and8 numerical applications. Clarify that status denotes support for the answer, not truth of the question's proposition. Same updated prompt for baseline and adapter. Dataset and prompt change together: cannot isolate their separate causal effects. Development tests are exposed, not final acceptance. No additional library review claimed.

Artifacts: results/pdf_sft_012_v1/pdf_sft_012. Next preparation: scripts/prepare_pdf_run_013.py. Cloud fitting only; private research/paper scope.
