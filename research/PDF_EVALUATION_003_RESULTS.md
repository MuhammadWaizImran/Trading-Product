# Evidence diagnostic 003 — 22 September 2026

**Decision: use verified evidence and deterministic calculations; do not promote an adapter.** The private Kaggle job completed. All 32 answers were read (8 cases × base/006 × closed/provided evidence); none hit the token limit. This was inference only, with no fitting on any device.

Artifacts: `results/pdf_evaluation_003_v1/pdf_evaluation_003/`. The protocol records the fixed Qwen3-8B revision, adapter hashes, prompts and manually supplied evidence. Kernel: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-evaluation-003.

| Case | Without additional evidence | With checked evidence |
| --- | --- | --- |
| Execution depth | Both correctly reject equal best ask as sufficient to establish equal cost. | Base remains sound. Adapter says extra quantity **will** change cost, which is too categorical: the order might fit at the best ask on both venues. |
| Unidentified NOBI paper | Both ask for the missing source/definition. | Both abstain appropriately. |
| Explicit ask-minus-bid convention | Both reverse the supplied formula and return +0.25. | Both preserve the calculator's correct -0.25 and bid-heavy interpretation; both add “buying pressure,” which is broader than the displayed-depth evidence. |
| +4R/-1R payoff | Both give 20% break-even and do not infer actual probability. | Both preserve those distinctions. |
| USD 12,000 sizing case | Base invents USD 2.4 million notional/USD 72,000 loss. Adapter gives USD 12,000 notional, although its USD 60 loss is correct. | Both return USD 2,000 notional/USD 60 loss and no coin quantity; neither explicitly explains the missing entry-price dependency. |
| Missing stop | Base refuses quantity; adapter invents contradictory 25/2.5 quantities. | Both refuse quantity. Adapter also correctly reports the USD 50 budget. |
| Destroyed backup, working original | Base follows the premise. Adapter contradicts it and declares funds inaccessible. | Both correctly retain access through the original key; neither includes the future backup-loss risk. |
| Open code/restricted validators | Both identify restricted validation but append contradictory claims that the question lacks this information. | Base hedges “not necessarily” before explaining the restriction; adapter identifies permissioned validation. |

These are exposed diagnostic questions, and the evidence was manually matched. Several evidence blocks explicitly contained the correct answer or calculator output. This establishes that supplied context can correct particular failures; it does **not** establish automatic retrieval quality, independent accuracy, general trading competence, profitability or an advantage from fine-tuning. No aggregate pass percentage is reported because partial compliance and residual overstatement matter.

## Resulting implementation

- The offline workbench displays checked adaptations with PDF-page links rather than synthesizing unverified answers.
- Calculations run through tested `scripts/research_math.py`; a language model is not the source of numeric truth.
- Base Qwen3-8B remains the comparison model for the next cloud retrieval diagnostic. Failed adapters are preserved, not promoted.
- Next evaluation must use the actual retrieval algorithm, record retrieved example IDs, include missing/irrelevant evidence, and check citation support. Independent evaluation and the separate prediction/paper-trading gate remain outstanding.
