# Source-scope diagnostic007: routing works; answer reliability still fails

All32 responses were reviewed: eight cases for each base/adapter009 and unguarded/scoped condition. Cloud status reports complete. The source-specific scope labels were manually assigned, not inferred from arbitrary user prose.

The three unknown-source cases in both scoped conditions correctly request a document identity without model execution. This is a deterministic pipeline improvement, not knowledge learned by either model. Without routing, both models still assign the retrieved information to unspecified sources.

The five cases allowed through the router have identical answers within each model with/without routing, so this small check found no answer change caused by filtering. However, the combined system does **not** pass its correctness gate: both models reverse the sell-limit direction and allow a hypothetical235 sale under a240 sell limit. The provided passage states the correct rule. The same adapter answered a differently prompted version correctly in run009, demonstrating prompt sensitivity. The adapter's chart-year answer lacks the requested citation; its signature answer adds unsupported general assertions about registration/documentation.

Decision: retain the explicit source gate as a tested prototype; do not promote the complete answer system or launch another blind fitting run. No evidence of expert or profitable performance. The gate depends on trustworthy caller-supplied selection and does not validate claim support.

Concrete follow-up: scripts/research_math.py now contains limit_price_rule, an exact Decimal comparison for hypothetical buy/sell limit prices. Buy requires fill<=limit; sell requires fill>=limit. It never guarantees a fill, assesses fees/liquidity or submits an order. Direction, equality, decimal precision and invalid inputs are tested locally without model execution. It is a backend primitive, not yet integrated into a model-facing tool flow. Next development should connect explicit numerical/source inputs to these verified tools and evaluate the resulting answer flow before more SFT.

Evidence: results/pdf_scope_007_v1/pdf_scope_007, the frozen notebooks/pdf_scope_eval_007/review_protocol.json and local_review_checks.json. This is development evidence, not an independent final test.
