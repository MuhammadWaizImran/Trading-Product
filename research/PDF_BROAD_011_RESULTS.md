# Broad011 review: adapter010 not accepted (2026-09-29)

Downloaded private cloud outputs to results/pdf_broad_011_v1. All100 model-invoked responses were read:25 supported and25 irrelevant-evidence answers per model. All200 records were structurally checked against protocol IDs. Each model also had50 deterministic routes (25 missing,25 unidentified); those correctly prevented invocation and are not learned-model successes. No output was truncated. See pdf_broad_011/local_structural_audit.json for hashes.

## Main conclusions

No demonstrated overall advantage sufficient to select adapter010. Both models still fail strict grounding. The conditional prompt removes the earlier explicit fabricated calculator references in these reviewed answers, but comparison with broad010 changes both prompt and adapter for the trained condition; do not attribute all gains to training.

The adapter correctly recognizes the unrelated passage in the candle-body case01, avoiding the earlier false candle calculation. Many other irrelevant cases now explicitly identify missing topical evidence. However both models often begin with a factual-sounding No before explaining insufficiency, including the offline-broadcast case24 whose supported answer should be Yes.

## Supported-case failures

- 04: base correctly distinguishes inverted hammer after decline versus shooting star after advance. Adapter says identical shapes must have identical names despite quoting the contrary context rule: clear regression.
- 10: both incorrectly start Yes, a crossing limit must get maker fees. Base then contradicts itself by describing taker fees; adapter incorrectly infers maker fees from acting as a taker. This is a market-mechanics error.
- 24: base correctly answers Yes to broadcasting with a powered-off receiving signing device; adapter starts No then states broadcasting is possible: clear regression.
- 06: both ignore the premise that notionals are already fixed equal, explaining different planned losses by changing notional instead of different stop distances.
- 02: adapter adds increased volatility as an ADX interpretation unsupported by the supplied passage.
- 07: adapter asserts moving a stop makes a trade less reliable; the passage establishes changed setup/stop-hit likelihood, not that universal conclusion.
- 15: adapter says different reset anchors lead to different values, without allowing numerical coincidence.
- 20: adapter says multiple transfers are parts of a single operation, whereas the passage permits multiple operations and does not establish one operation here.
- 09: adapter omits the supporting evidence ID.

Other supported cases commonly preserve the main concepts, including candle body, range uncertainty, squeeze direction uncertainty, costs, execution limits, order changes, absolute imbalance, RSI conventions, custody, backing, signature scope and indicator correlation. These successes do not compensate for the above failures under the zero-severe-error gate.

## Irrelevant-evidence failures

Base cases14 and16 incorrectly cite offline-wallet evidence for absolute imbalance and RSI conventions. Adapter case14 answers from arithmetic/background despite the evidence-only rubric; case16 supplies RSI claims and an unrelated offline-wallet citation. Adapter case22 states that the unrelated passage supports controlled validation. Both case23 answers attach the offline-wallet citation to a signature-binding claim. Cases04 and21 also answer substantive questions despite no relevant supplied evidence. Citation presence alone is not entailment.

This is a qualitative failure review, not a fully scored semantic accuracy estimate. The100 cases are25 correlated families reused from broad010 and exposed to training decisions; they are not100 independent final acceptance questions.

## Decision and next experiment

Do not promote adapter010 or repeat identical fitting. Preserve its artifacts and base comparator. Diagnostic012 tests a concrete input-format hypothesis: embedded evidence questions and leading Yes/No may anchor the answer to a different question. Six selected failure scenarios are compared as original Q&A evidence versus declarative evidence (remove the evidence question, rename answer to text, remove only an initial Yes./No.). This bundles three representation changes, so it cannot isolate their separate causes. Facts, sources, pages, user questions, model revisions and prompt remain unchanged.12 cases x2 models=24 generations; no fitting. The diagnosis may fail and is not proof of repair.

Private job: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-format-check-012 . Preparation and frozen protocol: scripts/prepare_evidence_format_012.py and notebooks/pdf_format_eval_012/review_protocol.json. No rubric answers are injected. Review all24 outputs before further training decisions. Independent evaluation and incomplete full-library review remain outstanding; no trading profitability or visual chart reading established.
