# Broad assessment010: no promotion (2026-09-29)

Private Kaggle broad-check010 completed and outputs downloaded to `results/pdf_broad_010_v1`. This was inference, not fitting. All100 model-invoked answers were read; all200 records were structurally checked. Each model produced25 supported answers and25 answers with unrelated evidence; another50 requests were handled by deterministic source/evidence gates. No output hit its token limit. The routes correctly returned25 needs_evidence and25 needs_source per model. These routing successes are not learned answer accuracy.

## Findings

Both base and adapter009 fail the gate. In b010-01-irrelevant, both use offline-wallet evidence to justify an incorrect candle-body boundary (18 to15 instead of18 to16). In b010-22-irrelevant, both use that unrelated wallet passage to support claims about validator authorization. Other unrelated-evidence answers mix unsupported background knowledge with an insufficiency statement rather than cleanly abstaining.

In b010-24-supported, both answer “No” to whether a sender can broadcast to a known valid address while the receiving signing device is off, then explain that this is possible. The direct answer must be Yes. Other supported answers invent calculator evidence even though no calculator output was supplied. Examples include adapter009 cases15,16,20,25 and base cases12,13,15,18,25. Prompt instructions about calculators and execution constraints appear to contaminate unrelated topics; this is a diagnosis to test, not an established causal result.

Additional weaknesses include unqualified ADX strength claims, losing the fixed-notional premise in risk questions, and treating possible VWAP differences as inevitable. Many supported answers correctly explain their concepts, but that does not offset severe false attribution or contradictory conclusions. No precise semantic accuracy percentage is claimed from this qualitative review.

## Next experiment

SFT010 adds48 balanced positive/negative and relevant/irrelevant evidence exercises, retaining230 earlier records. The conditional prompt only permits tool references when an actual relevant tool result exists. A fresh base-model baseline receives the same prompt, so any apparent repair must be compared against prompt-only improvement. Six new concept-overlapping test probes and six validation probes are added; old cases remain exposed development evidence. Broad010 now informs training decisions and cannot be an untouched final test.

The12 new training families reuse reviewed, page-traceable adaptations. No new PDF/page coverage is claimed. The same pinned Qwen3-8B revision, rank8 QLoRA, one epoch and2e-5 learning rate are retained. Success requires correct new tests without invented tools, contradictory polarity, false citations or severe regression; base parity is not adapter advantage. Independent acceptance and remaining PDF review are still required.

Structural evidence: `PDF_BROAD_010_STRUCTURAL_AUDIT.json`. No real orders, laptop model execution or public publication.
