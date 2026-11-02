"""Cloud-only Qwen3-8B PDF SFT template. The notebook builder embeds PAYLOAD.

Do not execute locally: the guard runs before ML imports or downloads.
"""
import hashlib
import importlib.metadata
import json
import math
import os
from pathlib import Path
import platform
import subprocess
import sys
import traceback
from datetime import datetime, timezone

PAYLOAD = None  # EMBED_PDF_PAYLOAD


def cloud_root():
    if platform.system() != 'Linux':
        raise RuntimeError('Cloud-only policy: laptop training is disabled.')
    if os.environ.get('KAGGLE_KERNEL_RUN_TYPE') and Path('/kaggle/working').is_dir():
        return Path('/kaggle/working/pdf_sft_001')
    if os.environ.get('COLAB_RELEASE_TAG') and Path('/content').is_dir():
        return Path('/content/pdf_sft_001')
    raise RuntimeError('A hosted Kaggle or Colab runtime is required; no local override.')


def main():
    out = cloud_root()
    out.mkdir(parents=True, exist_ok=True)
    def save(name, value):
        (out/name).write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')
    def status(stage, **extra):
        save('status.json', dict(stage=stage, utc=datetime.now(timezone.utc).isoformat(), **extra))
        print(stage, flush=True)
    try:
        assert PAYLOAD and PAYLOAD['manifest']['model'] == 'Qwen/Qwen3-8B'
        status('cloud_preflight')
        os.environ['CUDA_VISIBLE_DEVICES'] = '0'
        os.environ['TOKENIZERS_PARALLELISM'] = 'false'
        os.environ['WANDB_DISABLED'] = 'true'
        os.environ['HF_HOME'] = '/tmp/pdf-sft-hf'
        import torch
        if not torch.cuda.is_available():
            raise RuntimeError('No working CUDA GPU. CPU training is disabled; fix cloud allocation.')
        # Check connectivity before spending time on package retries or model download.
        import urllib.request
        for url in ['https://pypi.org/simple/transformers/', 'https://huggingface.co/api/models/Qwen/Qwen3-8B']:
            with urllib.request.urlopen(url, timeout=15) as response:
                assert response.status == 200
        status('installing_dependencies')
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--quiet', '--retries', '1',
                        'transformers==4.56.2', 'peft==0.17.1', 'accelerate==1.10.1',
                        'bitsandbytes==0.47.0'], check=True)
        from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, Trainer, TrainingArguments, set_seed
        from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
        from huggingface_hub import model_info
        set_seed(217)
        model_id = 'Qwen/Qwen3-8B'
        revision = model_info(model_id).sha
        dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
        save('dataset_manifest.json', PAYLOAD['manifest'])
        save('runtime.json', dict(model=model_id, revision=revision, seed=217,
            gpu=torch.cuda.get_device_name(0), cuda=torch.version.cuda,
            packages={p: importlib.metadata.version(p) for p in
                      ['torch', 'transformers', 'peft', 'accelerate', 'bitsandbytes']},
            payload_sha256=hashlib.sha256(json.dumps(PAYLOAD, sort_keys=True).encode()).hexdigest()))
        (out/'ATTRIBUTION.txt').write_text(PAYLOAD['attribution'], encoding='utf-8')
        status('loading_model')
        tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision, trust_remote_code=False)
        tokenizer.pad_token = tokenizer.eos_token
        model = AutoModelForCausalLM.from_pretrained(model_id, revision=revision,
            trust_remote_code=False, device_map={'': 0}, torch_dtype=dtype, attn_implementation='sdpa',
            quantization_config=BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type='nf4',
                bnb_4bit_use_double_quant=True, bnb_4bit_compute_dtype=dtype))
        model = prepare_model_for_kbit_training(model)
        model = get_peft_model(model, LoraConfig(r=8, lora_alpha=16, lora_dropout=0.05,
            target_modules=['q_proj', 'v_proj'], task_type='CAUSAL_LM', bias='none'))
        def prompt(row):
            return tokenizer.apply_chat_template(row['messages'][:-1], tokenize=False,
                                                 add_generation_prompt=True, enable_thinking=False)
        def tokenize(row):
            a = tokenizer.encode(prompt(row), add_special_tokens=False)
            b = tokenizer.encode(row['messages'][-1]['content']+tokenizer.eos_token, add_special_tokens=False)
            assert len(a)+len(b) <= 768, 'Refuse silent truncation'
            return dict(input_ids=a+b, attention_mask=[1]*(len(a)+len(b)), labels=[-100]*len(a)+b)
        def collate(rows):
            n = max(len(r['input_ids']) for r in rows)
            pads = dict(input_ids=tokenizer.pad_token_id, attention_mask=0, labels=-100)
            return {k: torch.tensor([r[k]+[p]*(n-len(r[k])) for r in rows]) for k,p in pads.items()}
        args = TrainingArguments(output_dir=str(out/'checkpoints'), num_train_epochs=1,
            learning_rate=1e-4, warmup_ratio=0.1, per_device_train_batch_size=1,
            gradient_accumulation_steps=4, per_device_eval_batch_size=1,
            gradient_checkpointing=True, gradient_checkpointing_kwargs={'use_reentrant': False},
            bf16=dtype == torch.bfloat16, fp16=dtype == torch.float16,
            optim='paged_adamw_8bit', save_strategy='no', report_to=[], logging_steps=1,
            seed=217, data_seed=217, dataloader_num_workers=0)
        trainer = Trainer(model=model, args=args, data_collator=collate,
            train_dataset=[tokenize(r) for r in PAYLOAD['train']],
            eval_dataset=[tokenize(r) for r in PAYLOAD['validation']])
        def generate(label):
            model.eval()
            results = []
            for row in PAYLOAD['test']:
                inputs = tokenizer(prompt(row), return_tensors='pt').to('cuda:0')
                with torch.inference_mode():
                    answer = model.generate(**inputs, do_sample=False, max_new_tokens=220,
                                            use_cache=True, pad_token_id=tokenizer.pad_token_id)
                results.append(dict(id=row['id'], question=row['messages'][-2]['content'],
                    reference=row['messages'][-1]['content'], provenance=row['provenance'],
                    response=tokenizer.decode(answer[0,inputs.input_ids.shape[1]:], skip_special_tokens=True)))
            save(label+'.json', results)
        status('baseline_evaluation')
        generate('baseline_answers')
        before = trainer.evaluate()
        model.config.use_cache = False
        status('training_pdf_examples', count=len(PAYLOAD['train']))
        result = trainer.train()
        assert math.isfinite(result.training_loss), 'Non-finite training loss'
        trainer.save_model(str(out/'adapter'))
        tokenizer.save_pretrained(out/'adapter')
        (out/'adapter'/'ATTRIBUTION.txt').write_text(PAYLOAD['attribution'], encoding='utf-8')
        after = trainer.evaluate()
        status('adapter_evaluation')
        generate('adapted_answers')
        model.load_adapter(str(out/'adapter'), adapter_name='reload_check', is_trainable=False)
        model.set_adapter('reload_check')
        generate('reloaded_answers')
        save('result.json', dict(before_validation=before, after_validation=after,
            train_metrics=result.metrics, training_log=trainer.state.log_history,
            factuality_review='pending human review of baseline/adapted/reloaded responses',
            production_approved=False, profitability_evaluated=False,
            coverage='Only the PDF-derived examples recorded in dataset_manifest.json'))
        status('completed_training_human_evaluation_pending')
    except Exception as exc:
        status('failed', error_type=type(exc).__name__, error=str(exc),
               completed_training=False)
        (out/'failure.txt').write_text(traceback.format_exc(), encoding='utf-8')
        raise


if __name__ == '__main__':
    main()
