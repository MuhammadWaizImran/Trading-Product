# Private cloud model migration ? 2026-10-28

Yes: current checkpoints are portable LoRA adapters, not Kaggle-only models. No retraining from scratch is necessary to run existing weights on compatible cloud hardware. Actual target deployment has not been tested or purchased.

Transfer package:
1. Copy results/pdf_sft_017_v1/pdf_sft_017/adapter privately. Retain adapter_model.safetensors, adapter_config.json, tokenizer files, chat template and attribution.
2. Copy dataset_manifest.json, runtime.json, experiment reports, system prompt and generation settings. Check file hashes against research/MODEL_MIGRATION_MANIFEST.json.
3. On authorized cloud only, load Qwen/Qwen3-8B pinned revision b968826d9c46dd6066d109eabc6255188de91218. The adapter config revision is null, so explicitly pin the revision from our manifest. The adapter alone is not the complete model.
4. Reproduce runtime versions (transformers4.56.2, peft0.17.1, accelerate1.10.1, bitsandbytes0.47.0; consult runtime.json for torch/CUDA), tokenizer and quantization. Use compatible GPU memory sized for context and concurrency; adapter size does not represent total memory needs.
5. Load adapter using PEFT on the base; match thinking flag, prompt, sampling and token budget. Run the same frozen cases and compare outputs, latency and truncation before accepting migration. Hardware/library/quantization changes can alter answers.
6. Keep endpoints private/authenticated. Continuous hosting, provider costs and agent/voice/data infrastructure are separate from moving model files. No deployment or expense is authorized by this document alone.

Continuing fine-tuning from adapter weights is possible on cloud. Exact interrupted-training resumption additionally needs compatible optimizer/scheduler/RNG/trainer checkpoints, which the final-artifact downloader deliberately excludes. Do not claim exact resume from adapter alone. Any merge or format conversion must be done on authorized cloud and re-evaluated; preserve original adapter first. Base model is Apache2.0 per its model card; private training permission for PDFs does not authorize publishing PDFs or every derivative artifact. No model is production approved yet.

Official references: https://huggingface.co/docs/peft/developer_guides/checkpoint and https://huggingface.co/Qwen/Qwen3-8B .
