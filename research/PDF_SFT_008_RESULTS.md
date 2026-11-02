# Run 008 completed; reliability gate not passed

Reviewed 23 September 2026. Cloud completion: 13:51:10 UTC. All 53 optimizer steps completed on a Tesla T4 in 2,152.4 seconds (35.9 minutes of fitting). Qwen3-8B, fresh rank-8 QLoRA, pinned revision and configuration in the frozen manifest. 212 training records from selected material in ten PDFs; 36 validation and 36 development-test cases. This does not represent the whole PDF library.

Artifact audit passed: local/cloud manifests and split hashes match, finite loss, complete answer IDs, exact equality of adapted and reloaded answers. Adapter SHA-256: `c6ced5a7d85583e07080df03d717742f62bb7972bc2eb0ed6b5f38c7ce9e66f1`, 15,354,512 bytes. Download: `results/pdf_sft_008_v1/pdf_sft_008`. The cloud's original review-pending result is preserved; this report records subsequent review.

Validation loss decreased from 5.8082 to 4.1069. References do not consistently match the evidence/citation task, so this is not a reliability score or approval criterion.

## Review of all 36 base/adapted pairs

No output was truncated and all cited IDs existed in supplied context. Those checks do not establish that citations support claims.

- Price comparison: the adapter correctly calculates 200 tokens at $0.50 as $100 and at $5 as $1,000. The base incorrectly says the original entry price is missing despite its presence in the question. This is a local improvement. The adapter still suggests a private-round acquisition without evidence and ambiguously says the cost basis changed; the original purchase's basis does not change with current market price.
- Counterparty ownership: both correctly reject the conclusion, but cite unrelated evidence. The adapter adds an irrelevant private-round explanation and cold-storage risks as purported reasons. This is not supported reasoning and does not satisfy the citation goal.
- Capacity comparison: the adapter avoids the base's unsupported implication that an unspecified figure must be outdated; both require missing definitions.
- Signing: both correctly identify the key-controlling spender, but overstate signatures as proof of rightful ownership. Valid authorization under key rules does not establish legal entitlement.
- Selected-success tutorial: both produce a malformed negation suggesting illustrations include failures and costs, contrary to the supporting warning. The main conclusion rejects a general win-rate estimate, but the explanation is unreliable.
- SMA, payoff break-even, leverage and VWAP calculations are correct in both conditions. These are not demonstrated fine-tuning gains. The adapter drops the supporting VWAP citation.
- The backup scenario retains qualified wording about a key explicitly stated to remain available; missing-context boilerplate must not replace attention to the supplied facts.
- Most remaining concepts retain the base's correct main conclusions, with wording changes rather than demonstrated improvement. Some answers attach general extra claims to narrower passages.

**Decision: retain the adapter for diagnosis; do not promote it as expert or product-ready.** One clear local calculation improvement does not establish a reliable overall advantage when unsupported reasoning persists. These exposed development cases overlap training concepts and cannot certify generalization. No price forecasting, profit, all-coin coverage or visual chart ability was evaluated.

The frozen plan also requires an attribution stress comparison. Diagnostic006 replays the existing 16 retrieval cases against base and adapter008 using identical frozen evidence and the prior diagnostic prompt. It is development diagnosis, not an independent acceptance examination. It directly checks sell-limit direction, unidentified-paper attribution, missing inputs and fabricated current claims. Do not start another fitting run merely because loss fell. Preserve these failures when designing the next curriculum and retrieval changes.
