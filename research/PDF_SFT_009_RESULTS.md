# Run009: complete, source-attribution criterion failed

All44 base/adapted answer pairs were read. Artifact audit passed: local/cloud manifests and hashes match, complete answer IDs, finite training loss and exact adapted/reloaded response equality. Fitting took2,771.7seconds (46.2minutes),58 optimizer steps, one epoch on a Tesla T4. Adapter SHA-256: `6fdb8686e878e8d027646bfeb34df7bd859eb702a420bfe2218a6ef29ff4d503`. Files: `results/pdf_sft_009_v1/pdf_sft_009`.

Validation loss decreased from5.8082 to3.9217. That is not the acceptance criterion. The230 training records cover selected material from ten PDFs, not the full library or independent trading expertise.

## Frozen source-identity gate

All three new unidentified-source cases failed for both base and adapter:

- Unknown relative-spread report: confidently assigns the retrieved midpoint denominator to the unidentified report.
- Unknown VWAP article: describes the retrieved equation as the article's definition, then hedges about context rather than requesting article identity.
- Unknown survey: assigns the retrieved1,000-per-country sample size to an unspecified survey.

The five supported application cases retain mainly correct conclusions: identified chart year, transfer-versus-ownership, signature-versus-legal-title, sell-limit direction, and missing evidence in a winners-only tutorial. These successes do not rescue the failed source gate; the base also achieves the main conclusions. The legal-title answer includes unnecessary general legal assertions.

Earlier36 cases retain several problems: irrelevant private-round/cold-storage citations for wallet attribution; conflating key authorization with rightful ownership; malformed negation about missing failures/costs in a tutorial; and omitted citations on VWAP/stop answers. Arithmetic and many basic explanations remain correct. The acquisition-cost calculation improves over the base's missing-input mistake, but adds an unsupported private-round assumption and ambiguous cost-basis claim. No clear overall reliability advantage is established.

**Decision: do not promote; change the answering pipeline before further SFT, as specified before training.** No new fitting job is justified merely by lower loss. This is a failed development gate, not an independent final examination.

## Concrete next change

`workbench/source_scope.py` requires explicit document selection for source-specific questions and excludes other documents' evidence. Without selection it requests identity without invoking a model. General educational mode must be an explicit caller choice. It does not automatically classify free text, prove citation support, repair retrieval or make the LLM an expert. User-facing model generation remains disabled in the offline workbench.

A cloud development comparison will test base/adapter009 with and without this routing on the eight fixed applications. Scope metadata is manually assigned and disclosed, not inferred by a model. Improvements from deterministic routing must be attributed to the system rather than to training. Independent evaluation, remaining PDF coverage, numerical market modeling and prospective paper evaluation remain outstanding.
