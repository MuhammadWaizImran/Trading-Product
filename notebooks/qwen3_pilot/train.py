"""Private, cloud-only Qwen3-8B adapter pilot; not a trading strategy.

--validate-data performs only standard-library data checks on a laptop.
No uploaded PDF text, articles, credentials, or model weights are embedded.
"""
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import random
import subprocess
import sys
from datetime import datetime, timezone

MODEL = 'Qwen/Qwen3-8B'
SEED = 217
SYSTEM = ('You are a crypto research assistant. Use only the supplied evidence. '
          'Return one JSON object with status (ok or insufficient_data), value '
          '(number or null), unit, and explanation. Never invent missing inputs '
          'or promise profits. State the assumptions behind a calculation.')


def examples(split, count):
    """Original synthetic arithmetic, not historical observations or advice."""
    offset = {'train': 0, 'validation': 160, 'test': 185}[split]
    rows = []
    for j in range(count):
        i = j + offset
        kind = j % 5
        equity = 1700 + 113 * i
        risk = [0.25, 0.5, 1.0, 1.5][i % 4]
        entry = 40 + 3 * i
        distance = 2 + (i % 9)
        if kind == 0:
            value = equity * risk / 100 / distance
            prompt = (f'Equity USD {equity}; risk budget {risk}%; long entry USD {entry}; '
                      f'stop USD {entry-distance}. Ignore costs. Calculate units at risk-at-stop sizing.')
            if split != 'train':
                prompt = (f'A simulated long loses ${distance} per coin at its stop. '
                          f'The account is ${equity} and allows {risk}% loss. '
                          'How many coins fit that budget before costs?')
            unit = 'coins'
            explanation = 'Units = equity times risk fraction divided by entry-minus-stop. Gaps and costs can increase loss.'
        elif kind == 1:
            reward = round(1.25 + i * 0.025, 3)
            value = 100 / (1 + reward)
            prompt = f'Each win gains {reward}R and each loss loses 1R. What win percentage breaks even before costs?'
            if split != 'train':
                prompt = f'Loss size is 1 unit, gain size is {reward} units. Find the zero-expectancy success rate in percent, excluding fees.'
            unit = 'percent'
            explanation = 'Break-even percentage = 100 / (1 + reward-to-risk). Costs increase the required rate.'
        elif kind == 2:
            amount = 120 + i * 17
            rate = 0.005 + (i % 8) * 0.005
            value = amount * rate / 100
            prompt = f'Notional USD {amount}; single-period funding rate +{rate}%. Under the stated rule longs pay shorts, what does a long pay?'
            if split != 'train':
                prompt = f'The venue says positive funding is paid by longs. For one payment at {rate}% on ${amount}, calculate the long payment in USD.'
            unit = 'USD'
            explanation = 'Payment = notional times funding percentage / 100 under the supplied venue convention. No annualization is assumed.'
        elif kind == 3:
            gross = 25 + i
            fees = 3 + i % 7
            slippage = 2 + i % 5
            value = gross - fees - slippage
            prompt = f'Simulated gross P&L USD {gross}, total fees USD {fees}, total slippage USD {slippage}. Find net P&L.'
            if split != 'train':
                prompt = f'A paper trade earned ${gross} before expenses. Combined entry/exit fees are ${fees}; total execution slippage is ${slippage}. What remains in USD?'
            unit = 'USD'
            explanation = 'Net P&L = gross P&L minus all supplied fees and slippage. One trade does not establish an edge.'
        else:
            value = None
            prompt = f'Account USD {equity}; risk {risk}%; entry USD {entry}. Stop and per-coin loss are unknown. Give risk-at-stop position size.'
            if split != 'train':
                prompt = f'I have ${equity}, allow {risk}% loss, and enter at ${entry}. I have not chosen an exit or loss per coin. Compute the number of coins from my loss budget.'
            unit = 'coins'
            explanation = 'Risk-at-stop sizing requires the entry-to-stop loss per coin. A budget and entry price alone do not determine it.'
        answer = dict(status='insufficient_data' if value is None else 'ok',
                      value=None if value is None else round(value, 6),
                      unit=unit, explanation=explanation)
        rows.append(dict(id=f'{split}-{j:03}', family=kind, prompt=prompt, answer=answer,
                         provenance='Original synthetic case; formula-checked; no source text copied.'))
    return rows


def dataset():
    data = {name: examples(name, n) for name, n in [('train', 160), ('validation', 25), ('test', 25)]}
    prompts = [r['prompt'] for rows in data.values() for r in rows]
    assert len(set(prompts)) == len(prompts), 'Duplicate prompts across splits'
    for rows in data.values():
        for r in rows:
            a = r['answer']
            assert (a['value'] is None) == (a['status'] == 'insufficient_data')
            assert a['value'] is None or math.isfinite(a['value'])
    return data


def validate():
    data = dataset()
    # Independent spot checks: first sizing, break-even, funding, net and missing-data cases.
    assert data['train'][0]['answer']['value'] == 2.125
    assert abs(data['train'][1]['answer']['value'] - 4000/91) < 1e-6
    assert abs(data['train'][2]['answer']['value'] - 0.0231) < 1e-6
    assert data['train'][3]['answer']['value'] == 17
    assert data['train'][4]['answer']['value'] is None
    print(json.dumps({'data_checks': 'PASS', 'counts': {k: len(v) for k, v in data.items()},
                      'training_executed': False}))


def require_cloud():
    if not (platform.system() == 'Linux' and os.environ.get('KAGGLE_KERNEL_RUN_TYPE')
            and Path('/kaggle/working').is_dir()):
        raise RuntimeError('Cloud-only policy: training can run only inside hosted Kaggle. No local override.')


def main():
    require_cloud()  # Must precede ML imports, installs, downloads and fitting.
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'
    os.environ['TOKENIZERS_PARALLELISM'] = 'false'
    os.environ['WANDB_DISABLED'] = 'true'
    os.environ['HF_HOME'] = '/tmp/qwen-pilot-hf'
    out = Path('/kaggle/working/pilot_001')
    out.mkdir(parents=True, exist_ok=True)
    def save(name, obj):
        (out / name).write_text(json.dumps(obj, indent=2), encoding='utf-8')
    save('status.json', {'stage': 'setup', 'utc': datetime.now(timezone.utc).isoformat()})
    subprocess.run([sys.executable, '-m', 'pip', 'install', '--quiet',
                    'transformers==4.56.2', 'peft==0.17.1', 'accelerate==1.10.1',
                    'bitsandbytes==0.47.0'], check=True)
    import torch
    from transformers import (AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig,
                              Trainer, TrainingArguments, set_seed)
    from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
    from huggingface_hub import model_info
    import importlib.metadata
    if not torch.cuda.is_available():
        raise RuntimeError('Kaggle GPU not allocated; CPU training is disabled.')
    set_seed(SEED)
    revision = model_info(MODEL).sha
    data = dataset()
    save('dataset.json', data)
    manifest = dict(model=MODEL, revision=revision, seed=SEED,
                    purpose='Limited synthetic instruction pilot; no profitability claim',
                    gpu=torch.cuda.get_device_name(0),
                    dataset_sha256=hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest(),
                    script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                    packages={p: importlib.metadata.version(p) for p in
                              ['torch', 'transformers', 'peft', 'accelerate', 'bitsandbytes']})
    save('manifest.json', manifest)
    dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
    tokenizer = AutoTokenizer.from_pretrained(MODEL, revision=revision, trust_remote_code=False)
    tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(
        MODEL, revision=revision, trust_remote_code=False, torch_dtype=dtype,
        device_map={'': 0}, attn_implementation='sdpa',
        quantization_config=BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type='nf4',
                                              bnb_4bit_use_double_quant=True,
                                              bnb_4bit_compute_dtype=dtype))
    model = prepare_model_for_kbit_training(model)
    model = get_peft_model(model, LoraConfig(r=8, lora_alpha=16,
        target_modules=['q_proj', 'v_proj'], lora_dropout=0.05, bias='none', task_type='CAUSAL_LM'))
    model.print_trainable_parameters()

    def prompt_text(row):
        return tokenizer.apply_chat_template(
            [{'role': 'system', 'content': SYSTEM}, {'role': 'user', 'content': row['prompt']}],
            tokenize=False, add_generation_prompt=True, enable_thinking=False)

    def tokenize(row):
        prefix = tokenizer.encode(prompt_text(row), add_special_tokens=False)
        completion = tokenizer.encode(json.dumps(row['answer']) + tokenizer.eos_token,
                                      add_special_tokens=False)
        assert len(prefix) + len(completion) <= 512, 'No silent example truncation'
        return dict(input_ids=prefix + completion, attention_mask=[1]*(len(prefix)+len(completion)),
                    labels=[-100]*len(prefix) + completion)

    def collate(rows):
        length = max(len(r['input_ids']) for r in rows)
        pads = {'input_ids': tokenizer.pad_token_id, 'attention_mask': 0, 'labels': -100}
        return {k: torch.tensor([r[k] + [v]*(length-len(r[k])) for r in rows]) for k, v in pads.items()}

    args = TrainingArguments(output_dir=str(out/'checkpoints'), num_train_epochs=1,
        per_device_train_batch_size=1, gradient_accumulation_steps=8,
        per_device_eval_batch_size=1, learning_rate=1e-4, warmup_ratio=0.1,
        fp16=dtype == torch.float16, bf16=dtype == torch.bfloat16,
        gradient_checkpointing=True, gradient_checkpointing_kwargs={'use_reentrant': False},
        optim='paged_adamw_8bit', logging_steps=1, save_strategy='no',
        report_to=[], seed=SEED, data_seed=SEED, dataloader_num_workers=0)
    trainer = Trainer(model=model, args=args, data_collator=collate,
                      train_dataset=[tokenize(r) for r in data['train']],
                      eval_dataset=[tokenize(r) for r in data['validation']])

    def assess(label):
        model.eval()
        results = []
        for row in data['test']:
            inputs = tokenizer(prompt_text(row), return_tensors='pt').to('cuda:0')
            with torch.inference_mode():
                ids = model.generate(**inputs, do_sample=False, max_new_tokens=160,
                                     pad_token_id=tokenizer.pad_token_id, use_cache=True)
            text = tokenizer.decode(ids[0, inputs.input_ids.shape[1]:], skip_special_tokens=True)
            parsed = None
            try:
                parsed = json.loads(text.strip())
                assert isinstance(parsed, dict)
            except (ValueError, AssertionError):
                parsed = None
            expected = row['answer']
            correct = False
            if parsed is not None and parsed.get('status') == expected['status'] and parsed.get('unit') == expected['unit']:
                val = parsed.get('value')
                correct = (val is None and 'value' in parsed) if expected['value'] is None else (
                    isinstance(val, (int, float)) and not isinstance(val, bool)
                    and math.isclose(val, expected['value'], rel_tol=1e-4, abs_tol=1e-5))
            results.append(dict(id=row['id'], family=row['family'], output=text,
                                valid_json=parsed is not None, correct=correct))
        score = dict(valid_json=sum(r['valid_json'] for r in results)/len(results),
                     numeric_accuracy=sum(r['correct'] for r in results if r['family'] != 4)/20,
                     abstention_accuracy=sum(r['correct'] for r in results if r['family'] == 4)/5)
        save(label+'.json', dict(metrics=score, cases=results))
        return score

    save('status.json', {'stage': 'baseline_evaluation'})
    before = assess('baseline')
    before_loss = trainer.evaluate()['eval_loss']
    model.config.use_cache = False
    save('status.json', {'stage': 'training', 'utc': datetime.now(timezone.utc).isoformat()})
    train_result = trainer.train()
    trainer.save_model(str(out/'adapter'))
    tokenizer.save_pretrained(out/'adapter')
    after_loss = trainer.evaluate()['eval_loss']
    after = assess('adapted')
    # Verify saved weights can be loaded without allocating a second base model.
    model.load_adapter(str(out/'adapter'), adapter_name='reload_check', is_trainable=False)
    model.set_adapter('reload_check')
    reload_metrics = assess('reloaded')
    finite = math.isfinite(train_result.training_loss)
    no_regression = all(after[k] >= before[k] for k in ['numeric_accuracy', 'abstention_accuracy'])
    improvement = any(after[k] > before[k] for k in ['numeric_accuracy', 'abstention_accuracy'])
    save('result.json', dict(before=before, after=after, reloaded=reload_metrics,
        before_validation_loss=before_loss, after_validation_loss=after_loss,
        training=train_result.metrics, log_history=trainer.state.log_history,
        pilot_acceptance=finite and no_regression and reload_metrics == after,
        behavioral_improvement=improvement and no_regression,
        production_approved=False, trading_performance_measured=False))
    save('status.json', {'stage': 'complete', 'utc': datetime.now(timezone.utc).isoformat()})
    print('PILOT_COMPLETE: private adapter and evidence saved; not a production trading model.')


if __name__ == '__main__':
    if sys.argv[1:] == ['--validate-data']:
        validate()
    elif sys.argv[1:]:
        raise SystemExit('Only --validate-data is accepted locally.')
    else:
        main()
