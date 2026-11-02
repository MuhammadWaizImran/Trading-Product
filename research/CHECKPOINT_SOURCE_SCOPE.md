# Latest checkpoint: run 009 reviewed; answering pipeline under test

Run009 completed and its artifact audit passed. All44 paired answers were read. Both base and adapter failed all three unidentified-source cases. The adapter is not accepted. Read [run009 findings](PDF_SFT_009_RESULTS.md). There is no fitting job currently running.

Following the decision fixed before009, the next work changes the answering pipeline rather than automatically repeating SFT. workbench/source_scope.py requires explicit source selection for document-specific requests and filters evidence to that source; six nonfitting tests passed. General educational scope is an explicit caller choice. This does not classify arbitrary free text or prove evidence support, and is not yet connected to public model answering in the offline workbench.

Private cloud diagnostic007 was submitted: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-source-scope-007 . It compares base and adapter009 with and without source routing on eight development cases (32 responses). Scope metadata is manually assigned. A rule preventing a model call is a system improvement, not learned expertise. Frozen criteria are in notebooks/pdf_scope_eval_007/review_protocol.json.

## Remaining work

1. Review this pipeline diagnostic, including supported-answer preservation and citation quality.
2. Fix remaining retrieval/support errors; design further training only around an evidenced improvement hypothesis.
3. Complete broader PDF/source coverage and prepare an independent application assessment.230 records from selected sections of ten PDFs do not represent the whole library.
4. Separately develop and validate time-stamped multi-coin market analysis with realistic costs and prospective paper evaluation. PDF explanation does not demonstrate profitable prediction.

No reliable percentage or finish date for expertise exists. No real-order capability is authorized.

## Manual continuation

```powershell
$env:PYTHONUTF8='1'
tmp/kaggle_client/Scripts/kaggle.exe kernels status waizimran/crypto-qwen3-pdf-source-scope-007
```

After COMPLETE:

```powershell
tmp/kaggle_client/Scripts/kaggle.exe kernels output waizimran/crypto-qwen3-pdf-source-scope-007 -p results/pdf_scope_007_v1
```

Read pdf_scope_007/status.json, protocol.json and the four base/adapter009 x unguarded/scoped answer files. Require eight matching IDs per file. The three unknown-source requests in scoped mode must have model_invoked=false, needs_source and no guessed details. The other five must still receive supported correct answers. Attribute deterministic abstention to routing, not model learning; inspect citations and meaning manually. Save a results report before further fitting. Do not execute any cloud evaluator/trainer locally or start duplicate jobs.

Previous checkpoints below are historical where inconsistent.

---

