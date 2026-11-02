# Latest: source guard implementation (2026-10-28)

Implemented workbench source-identity guard: explicit English unidentified-document cues request source clarification even when general scope or a stale document selection is supplied. Existing source-selection behavior retained. This is a conservative cue guard, NOT general intent detection or semantic entailment; paraphrases/languages not covered and quoted/negated cues may cause clarification.

Added workbench/response_review.py: standalone offline generated-response rejection module rejects malformed/duplicate-key JSON, invalid status, bad citation shape, missing/ambiguous IDs, wrong document and truncation. Passing checks ALWAYS remains needs_semantic_review and publishable=False, including abstentions. Not connected to a model endpoint; workbench still returns checked passages only. Existing IDs cannot prove claim support.

Verification:13 workbench HTTP/data tests,6 source-scope tests,5 response-review tests passed (24 total). Includes general-scope and selected-document bypass checks. No fitting/inference, deployment, real orders or cloud run performed. These are engineering regression tests, not independent model acceptance.

Next: collect independently reviewed question/evidence pairs for semantic acceptance and design source-confirmation handling for broader phrasing. Keep generation unapproved pending that evaluation. Run020 is complete, not currently training. Discovery/continuous monitoring/voice remain unimplemented.

---

