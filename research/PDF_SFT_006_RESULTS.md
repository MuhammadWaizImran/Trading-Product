# Run 006 audit — 22 September 2026

Cloud fitting completed, but this adapter is not promoted to the next PDF run. A diagnostic of model and prompt behavior is the next step.

- Kaggle: `waizimran/crypto-qwen3-pdf-sft-006`, version 1; completed 2026-09-22 03:23:29 UTC.
- Model: Qwen3-8B revision `b968826d9c46dd6066d109eabc6255188de91218`; Tesla T4, CUDA 12.8.
- Data: 100 training, 16 validation, 16 test records, including selected DP03 content and four corrective training examples. This is not complete PDF ingestion.
- One epoch, 25 optimizer steps, 335.4232 seconds; validation loss 3.371198 to 3.265537.
- Adapter: 15,354,512 bytes; SHA-256 `e887415e71b18c75febd30867a857d64e95f9fbd114c1a570550b8d57f716615`.
- Downloaded manifest matches the local frozen manifest. Adapted and reloaded answer files match byte for byte. These establish artifact consistency, not factual quality.

## Review against the frozen rubric

Permission properties: partial. The core distinction is correct, but the response invents meaningless arithmetic about open code and restricted validation. Trust dependencies: partial/fail. It names overlapping network descriptions rather than the required two distinct dependencies, and invents another equation. Historical data: pass on the central requirement to treat old data as historical and require verification, although definitions are not discussed explicitly. Retail CBDC architecture: partial. It rejects the architecture inference but omits the rubric's explicit statement that retail describes the intended users and adds an unverified current project example. It does not reach three clean passes.

Retention still includes a false NOBI correlation interpretation, an incorrect expected-value formula `4R*p - 1R`, and a fabricated correlation coefficient. Corrective examples did not establish reliable correction. None of these generations hit the token limit.

## Evaluation problems found

The evaluation system prompt demands essential arithmetic for every question. Both parent and adapter invent arithmetic in nonnumeric answers. This is a plausible contributor, not a proven cause; it needs a controlled comparison.

The old NOBI question does not identify the paper or provide its formula. Asking for clarification is appropriate; inventing a definition is not. A separate question must supply the formula to measure correct calculation.

The earlier run 004 cold-storage pass was too lenient. Destroying a backup does not imply that a still-functioning original key is destroyed. The response's blanket claim that recovery is impossible was unsupported. Run 004 remains a comparison checkpoint, not a demonstrated reliable model. Earlier promotion reports are historical decisions, not guarantees.

## Next action already submitted

Private cloud diagnostic `waizimran/crypto-qwen3-pdf-evaluation-002` compares the base model, adapter 004 and adapter 006 on the same 12 questions under the original and neutral prompts (72 generations). It includes source-present/source-missing questions, correct risk arithmetic, and explicit backup-versus-original-key context. This is post-inspection diagnosis, not an independent accuracy test. It performs inference only. No further fitting or DP04 submission until the diagnostic is reviewed.
