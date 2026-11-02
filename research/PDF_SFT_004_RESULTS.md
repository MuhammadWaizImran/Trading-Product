# PDF SFT 004 — corrective cloud run result

Run 004 completed on Kaggle on 21 September 2026 and passes its narrow, predeclared continuation gate. It is not production-approved and does not demonstrate profitability or general crypto expertise.

- Private Kaggle job: `waizimran/crypto-qwen3-pdf-sft-004`, version 1
- Model revision: `Qwen/Qwen3-8B` at `b968826d9c46dd6066d109eabc6255188de91218`
- Runtime: Tesla T4, CUDA 12.8
- Parent: accepted run 002 adapter, SHA-256 `8e111a2cb193b246ca1fd1c6e4a1c181d8d439d636193a8a5b6c401f5ba561e2`
- New adapter: 15,354,512 bytes, SHA-256 `ab4250c6d48025e12c16aec4e35e54b9bf6a7fab6fec46ce44bdc70e2659dda3`
- Training: one epoch, learning rate 0.00005, 18 optimizer steps, 227.232 seconds
- Validation loss: 3.792656 before to 3.416587 after
- Data: 72 train, 12 validation, 12 test; the four DP01 promotion questions were fresh and absent from runs 001–003
- Cloud and local manifests match exactly.
- Adapted and reloaded answer files are byte-identical, SHA-256 `69208f586a73a01330631d13f617c3d6cb85a2f94a04afbaab2951e1f336edb5`.

## Predeclared fresh-test review

1. Capacity comparison: **pass**. It identifies missing transaction size, batching, protocol version and layer. Its `2,000 TPS` number is an invented illustrative example and should have been omitted, but it does not present it as the report's measured value.
2. Cold-storage loss: **pass**. It correctly separates reduced online exposure from backup destruction and permanent loss.
3. Token versus shareholder rights: **pass**. It rejects automatic equity equivalence and points to legal structure and documentation. This remains educational, not legal advice.
4. Correlation and causation: **fail**. It correctly rejects causation and mentions confounding, but fabricates an unstated correlation coefficient of `r = 0.75`.

This is three passes out of four, satisfying the frozen 75% threshold. No response hit the 192-token limit, so the new repetition failure seen in run 003 disappeared.

## Retention limitations

The adapter still mishandles important older checks. It treats the holder scenario as `400 + 5 = 405` addresses, invents a generic correlation meaning for NOBI instead of applying the paper's ask-minus-bid convention, and writes the invalid equation `4R = p × R` in the reward/probability answer. Those are severe factual weaknesses already present in the parent family; run 004 is accepted only as a controlled continuation parent under the stated rule, not as a reliable user-facing model.

Future evaluation must keep checking these errors and add corrective examples without reusing already inspected questions as independent evidence. Training completion and falling loss do not establish profitable trading behavior.
