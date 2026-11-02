# Diagnostic 002 — reviewed 22 September 2026

All 72 answers were inspected: 12 cases under two prompts for base Qwen3-8B, adapter 004 and adapter 006. The cloud job completed and no answer reached the generation limit. This is a post-inspection diagnostic on exposed concepts, not an independent accuracy estimate. Outputs are preserved in `results/pdf_evaluation_002_v1/pdf_evaluation_002`.

## Findings

The neutral prompt removes several invented arithmetic passages on nonnumeric questions and improves requests for missing source definitions. However, it does not consistently improve correctness: the base model gets the supplied imbalance sign and position-sizing arithmetic wrong under the neutral prompt, while computing them correctly under the original prompt. Changing the prompt alone is insufficient.

Both adapters reverse the explicitly supplied ask-minus-bid formula in both prompt conditions, giving +0.25 instead of -0.25. Both miscalculate the USD 12,000 / 0.5% risk / 3% stop sizing example under both prompts. The correct results are USD 60 risk budget and USD 2,000 notional. Both incorrectly infer a risk-at-stop quantity without a supplied stop. They also contradict the premise that a working signing device still contains its key when only the backup was destroyed.

The base model performs better on several of these paired diagnostic cases. It correctly distinguishes a working key from a lost backup under the neutral prompt; both adapters fail. Base also calculates 20% break-even correctly under both prompts. Adapter 006 with the original prompt falsely infers an actual probability and 60% break-even. Adapter 006 under the neutral prompt merely echoes the RSI question instead of answering it.

Several educational explanations remain useful: depth/price distinctions, profit-claim rejection, and missing-source handling under the neutral prompt. A correct opening is not a full pass when later text contradicts it, invents facts or supplies incorrect calculations. No aggregate score is reported because several rubrics have ambiguous partial-credit boundaries; the specific paired failures are sufficient to reject a demonstrated training improvement.

## Decision

Do not promote adapter 004 or 006 as a reliable model or continue adding PDFs under the assumption that these fine-tunes improve reasoning. Keep all artifacts and historical reports. The previous narrow promotion gates were inadequate and their decisions do not establish quality.

Added `scripts/research_math.py` for exact Decimal arithmetic, explicit sign conventions and missing-stop abstention. Seven arithmetic tests pass. This helper is not automatically invoked by the model and is not a trading system.

Prepared diagnostic 003 to compare base and adapter 006 with and without manually supplied checked evidence under the same neutral prompt (32 answers). Calculation evidence comes from the tested helper; educational context has page references. This assesses evidence use, not automatic retrieval or generalization, and performs no fitting. Review this before choosing between improved SFT, retrieval-supported explanations or a different model configuration. Further training and independent evaluation remain unfinished.
