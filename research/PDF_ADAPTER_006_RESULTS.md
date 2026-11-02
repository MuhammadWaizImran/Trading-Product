# Diagnostic006 completed: one correction, attribution still fails

All16 base and16 adapter008 answers were read from the completed cloud output in `results/pdf_adapter_006_v1/pdf_adapter_006`. Frozen evidence and prompt match the prior diagnostic. No fitting occurred here; this is exposed development evidence.

The adapter correctly changes the sell-limit explanation to a **minimum** selling price, fixing the base's maximum-price error. This is a real local improvement under the same prompt and evidence.

The unidentified NOBI paper is still treated as the retrieved paper, so source identity remains a blocking failure. That answer also omits its citation. The candle answer improves the no-guarantee wording but drops its supporting citation. Most other answers retain correct main conclusions without a substantial change; missing-chart and current-unlock requests receive appropriate abstention. The historical-report answer still assumes a specific date for an unspecified report. Broad claims about whole PDFs in the guarantee answer exceed the supplied passages.

Decision: do not promote adapter008. Preserve the sell-limit correction as a demonstrated narrow gain, not expertise. Next experiment009 uses controlled matched-source, unidentified-source and irrelevant-source training triples plus fixed development applications. It starts from the pinned base and retains008 settings, so it is not an endorsement or continuation of the failed adapter. If this still fails source identification, change the answering pipeline before more SFT. No automatic training loop.
