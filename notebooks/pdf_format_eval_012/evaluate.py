"""Post-inspection diagnostic. Inference only, cloud only; no additional fitting.

Compares base and adapter010 on 12 paired evidence-format cases, no fitting.
This is not an untouched confirmatory test and must not be reported as one.
"""
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys

assert platform.system() == 'Linux' and Path('/kaggle/working').is_dir()
assert os.getenv('KAGGLE_KERNEL_RUN_TYPE')
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
os.environ['HF_HOME'] = '/tmp/pdf-evaluation-hf'
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
OUT = Path('/kaggle/working/pdf_format_012')
OUT.mkdir(parents=True, exist_ok=True)
subprocess.run([sys.executable, '-m', 'pip', 'install', '--quiet', '--retries', '1',
                'transformers==4.56.2', 'peft==0.17.1', 'accelerate==1.10.1',
                'bitsandbytes==0.47.0'], check=True)
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, set_seed

assert torch.cuda.is_available(), 'No GPU; local/CPU inference fallback disabled.'
roots = list(Path('/kaggle/input').rglob('pdf_sft_010/runtime.json'))
assert len(roots) == 1, f'Expected one attached training output; found {len(roots)}'
root = roots[0].parent
runtime = json.loads(roots[0].read_text())
status = json.loads((root/'status.json').read_text())
assert status['stage'] == 'completed_training_human_evaluation_pending'
revision = runtime['revision']
model_id = runtime['model']
assert model_id == 'Qwen/Qwen3-8B'
cases = json.loads('[{"id": "b010-04-supported-qa", "question": "Two identical long-upper-wick candles appear, one after an advance and another after a decline. Must their conventional names be identical?", "retrieved": [{"id": "dp05-upper-wick-context", "source": "DP05", "pages": [29, 30, 31], "question": "How do an inverted hammer and a shooting star differ when their candle shapes look similar?", "answer": "Both can have a small body near the low and a long upper wick. An inverted hammer is conventionally discussed after a decline, while a shooting star is discussed after an advance. Prior context and a defined observation rule matter; the shape alone is not a directional forecast."}], "scope": "general", "source_id": null, "category": "dp05-upper-wick-context", "condition": "supported"}, {"id": "b010-04-supported-declarative", "question": "Two identical long-upper-wick candles appear, one after an advance and another after a decline. Must their conventional names be identical?", "retrieved": [{"id": "dp05-upper-wick-context", "source": "DP05", "pages": [29, 30, 31], "text": "Both can have a small body near the low and a long upper wick. An inverted hammer is conventionally discussed after a decline, while a shooting star is discussed after an advance. Prior context and a defined observation rule matter; the shape alone is not a directional forecast."}], "scope": "general", "source_id": null, "category": "dp05-upper-wick-context", "condition": "supported"}, {"id": "b010-06-supported-qa", "question": "Two positions each expose 600 dollars but have different stop distances. Must their planned stop losses be equal?", "retrieved": [{"id": "risk-budget", "source": "DP06", "pages": [4], "question": "Does risking 1% of an account mean buying an asset with only 1% of the account?", "answer": "No. Risk-at-stop refers to the planned loss if the stop executes as assumed. Position notional is the amount exposed to price movement. For a USD 10,000 account, a 1% loss budget is USD 100, but the notional depends on stop distance and costs."}], "scope": "general", "source_id": null, "category": "risk-budget", "condition": "supported"}, {"id": "b010-06-supported-declarative", "question": "Two positions each expose 600 dollars but have different stop distances. Must their planned stop losses be equal?", "retrieved": [{"id": "risk-budget", "source": "DP06", "pages": [4], "text": "Risk-at-stop refers to the planned loss if the stop executes as assumed. Position notional is the amount exposed to price movement. For a USD 10,000 account, a 1% loss budget is USD 100, but the notional depends on stop distance and costs."}], "scope": "general", "source_id": null, "category": "risk-budget", "condition": "supported"}, {"id": "b010-10-supported-qa", "question": "A buy limit immediately crosses the available ask. Must it receive a maker fee because it is a limit order?", "retrieved": [{"id": "dp17-maker-taker", "source": "DP17", "pages": [39, 40], "question": "Does placing a limit order necessarily make the trader a liquidity maker?", "answer": "No. An order adds liquidity when it rests in the book; an immediately executable limit order can consume existing liquidity and act as a taker. The limit constrains price, while maker/taker classification depends on execution behavior and venue rules."}], "scope": "general", "source_id": null, "category": "dp17-maker-taker", "condition": "supported"}, {"id": "b010-10-supported-declarative", "question": "A buy limit immediately crosses the available ask. Must it receive a maker fee because it is a limit order?", "retrieved": [{"id": "dp17-maker-taker", "source": "DP17", "pages": [39, 40], "text": "An order adds liquidity when it rests in the book; an immediately executable limit order can consume existing liquidity and act as a taker. The limit constrains price, while maker/taker classification depends on execution behavior and venue rules."}], "scope": "general", "source_id": null, "category": "dp17-maker-taker", "condition": "supported"}, {"id": "b010-16-irrelevant-qa", "question": "Two implementations both use RSI14 but initialize smoothing differently. Is the period label enough to guarantee reproducible values?", "retrieved": [{"id": "dp16-receive-offline", "source": "DP16", "pages": [105], "question": "Must an offline signing device connect to the internet before a sender can pay a known valid receiving address?", "answer": "No. A sender can broadcast a payment to a known valid address through the network without the receiving signing device being online. Observing confirmation and later authorizing spending are different steps. This does not remove the need to verify the intended address or retain the required signing material."}], "scope": "general", "source_id": null, "category": "dp05-rsi-definition", "condition": "irrelevant"}, {"id": "b010-16-irrelevant-declarative", "question": "Two implementations both use RSI14 but initialize smoothing differently. Is the period label enough to guarantee reproducible values?", "retrieved": [{"id": "dp16-receive-offline", "source": "DP16", "pages": [105], "text": "A sender can broadcast a payment to a known valid address through the network without the receiving signing device being online. Observing confirmation and later authorizing spending are different steps. This does not remove the need to verify the intended address or retain the required signing material."}], "scope": "general", "source_id": null, "category": "dp05-rsi-definition", "condition": "irrelevant"}, {"id": "b010-22-irrelevant-qa", "question": "A ledger is publicly readable but only approved entities validate. Does public reading make validation permissionless?", "retrieved": [{"id": "dp16-receive-offline", "source": "DP16", "pages": [105], "question": "Must an offline signing device connect to the internet before a sender can pay a known valid receiving address?", "answer": "No. A sender can broadcast a payment to a known valid address through the network without the receiving signing device being online. Observing confirmation and later authorizing spending are different steps. This does not remove the need to verify the intended address or retain the required signing material."}], "scope": "general", "source_id": null, "category": "dp03-permission-models", "condition": "irrelevant"}, {"id": "b010-22-irrelevant-declarative", "question": "A ledger is publicly readable but only approved entities validate. Does public reading make validation permissionless?", "retrieved": [{"id": "dp16-receive-offline", "source": "DP16", "pages": [105], "text": "A sender can broadcast a payment to a known valid address through the network without the receiving signing device being online. Observing confirmation and later authorizing spending are different steps. This does not remove the need to verify the intended address or retain the required signing material."}], "scope": "general", "source_id": null, "category": "dp03-permission-models", "condition": "irrelevant"}, {"id": "b010-24-supported-qa", "question": "A signing device is powered off. Can a sender still broadcast to its already known valid receiving address?", "retrieved": [{"id": "dp16-receive-offline", "source": "DP16", "pages": [105], "question": "Must an offline signing device connect to the internet before a sender can pay a known valid receiving address?", "answer": "No. A sender can broadcast a payment to a known valid address through the network without the receiving signing device being online. Observing confirmation and later authorizing spending are different steps. This does not remove the need to verify the intended address or retain the required signing material."}], "scope": "general", "source_id": null, "category": "dp16-receive-offline", "condition": "supported"}, {"id": "b010-24-supported-declarative", "question": "A signing device is powered off. Can a sender still broadcast to its already known valid receiving address?", "retrieved": [{"id": "dp16-receive-offline", "source": "DP16", "pages": [105], "text": "A sender can broadcast a payment to a known valid address through the network without the receiving signing device being online. Observing confirmation and later authorizing spending are different steps. This does not remove the need to verify the intended address or retain the required signing material."}], "scope": "general", "source_id": null, "category": "dp16-receive-offline", "condition": "supported"}]')
tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision, trust_remote_code=False)
tokenizer.pad_token = tokenizer.eos_token
dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
base = AutoModelForCausalLM.from_pretrained(model_id, revision=revision, trust_remote_code=False,
    device_map={'':0}, torch_dtype=dtype, attn_implementation='sdpa',
    quantization_config=BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type='nf4',
        bnb_4bit_use_double_quant=True, bnb_4bit_compute_dtype=dtype))

system = 'Answer the question using only the supplied evidence and any explicitly supplied verified tool output. First check whether the evidence supports the requested conclusion. If it does not, state what relevant evidence is missing; do not answer from memory or cite an unrelated passage. When supported, answer directly in at most three short sentences and cite the supporting evidence ID in square brackets. Make Yes or No agree with the question and explanation. Do not invent tool calls, calculator results, measurements or source details. Mention tools only when an actual tool result is supplied and relevant. Preserve uncertainty and distinguish possibility from certainty.'

"""Explicit source scope for experimental answering; no inference or fitting.

The caller must obtain scope/source_id from the user's selection, never from a
retrieval result or model guess. This does not detect intent in arbitrary prose
and does not establish that a passage supports an answer.
"""
from copy import deepcopy


def route_evidence(evidence, *, scope='source_specific', source_id=None):
    if scope not in ('source_specific', 'general'):
        raise ValueError('Choose source_specific or general scope explicitly')
    if scope == 'general' and source_id is not None:
        raise ValueError('A selected source requires source_specific scope')
    if source_id is not None and (not isinstance(source_id, str) or not source_id.strip()):
        raise ValueError('source_id must be a nonempty document identifier')
    if scope == 'source_specific' and source_id is None:
        return dict(status='needs_source', evidence=[], model_allowed=False,
                    response='Please identify or select the document you mean. Retrieved passages alone do not establish the identity of an unnamed source.')
    selected = [deepcopy(e) for e in evidence if scope == 'general' or e.get('source') == source_id]
    if not selected:
        return dict(status='needs_evidence', evidence=[], model_allowed=False,
                    response='No reviewed evidence is available for this request and source selection. Please provide the relevant passage.')
    return dict(status='ready', evidence=selected, model_allowed=True, response=None)


"""Exact arithmetic for hypothetical research scenarios. No fitting or order execution."""
from decimal import Decimal, InvalidOperation


def number(value):
    if isinstance(value, bool):
        raise ValueError('Boolean is not a numeric input')
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError):
        raise ValueError('Expected a finite decimal number') from None
    if not result.is_finite():
        raise ValueError('Expected a finite decimal number')
    return result


def limit_price_rule(side, limit_price, hypothetical_fill_price):
    """Check a hypothetical price constraint only; never submit or simulate an order."""
    if side not in ('buy', 'sell'):
        raise ValueError('Explicit buy or sell side required')
    limit, fill = number(limit_price), number(hypothetical_fill_price)
    if limit <= 0 or fill <= 0:
        raise ValueError('Positive limit and hypothetical fill prices required')
    return {'price_constraint_satisfied': fill <= limit if side == 'buy' else fill >= limit,
            'side': side, 'limit_price': limit, 'hypothetical_fill_price': fill,
            'constraint': 'fill <= limit' if side == 'buy' else 'fill >= limit',
            'execution_guaranteed': False,
            'scope': 'Gross price comparison only; no fees, liquidity, venue rules or actual execution assessed.'}


def position_size(account, risk_fraction, stop_fraction=None, entry_price=None):
    """Linear spot notional under exact stop execution, excluding costs and leverage."""
    account, risk = number(account), number(risk_fraction)
    if account <= 0 or not Decimal(0) < risk <= Decimal(1):
        raise ValueError('Positive account and risk fraction in (0,1] required')
    budget = account * risk
    if stop_fraction is None:
        return {'status': 'insufficient_information', 'risk_budget': budget,
                'missing': 'entry-to-stop fractional loss', 'notional': None, 'quantity': None}
    stop = number(stop_fraction)
    if not Decimal(0) < stop <= Decimal(1):
        raise ValueError('Spot stop fraction must be in (0,1]')
    notional = budget / stop
    quantity = None
    if entry_price is not None:
        entry = number(entry_price)
        if entry <= 0:
            raise ValueError('Positive entry price required')
        quantity = notional / entry
    return {'status': 'calculated', 'risk_budget': budget, 'notional': notional,
            'quantity': quantity, 'exceeds_account': notional > account,
            'assumptions': 'Linear spot; exact stop execution; no costs. Not an order.'}


def payoff(win_r, loss_r, probability=None, cost_r=0):
    """Loss is a positive magnitude; constant per-outcome costs in risk units."""
    win, loss, cost = map(number, (win_r, loss_r, cost_r))
    if win <= 0 or loss <= 0 or cost < 0:
        raise ValueError('Positive win/loss magnitudes and nonnegative costs required')
    breakeven = (loss + cost) / (win + loss)
    expected = None
    if probability is not None:
        p = number(probability)
        if not Decimal(0) <= p <= Decimal(1):
            raise ValueError('Probability must be in [0,1]')
        expected = p * win - (1-p) * loss - cost
    return {'breakeven_probability': breakeven, 'feasible': breakeven <= 1,
            'expected_r': expected, 'actual_probability_known': probability is not None}


def orderbook_imbalance(ask_depth, bid_depth, convention):
    """Require explicit sign convention; never infer a paper's definition."""
    ask, bid = number(ask_depth), number(bid_depth)
    if ask < 0 or bid < 0 or ask + bid == 0:
        raise ValueError('Nonnegative comparable depths with positive total required')
    if convention not in ('ask_minus_bid', 'bid_minus_ask'):
        raise ValueError('Explicit ask_minus_bid or bid_minus_ask convention required')
    result = (ask-bid)/(ask+bid)
    if convention == 'bid_minus_ask':
        result = -result
    return {'value': result, 'convention': convention,
            'larger_displayed_side': 'bid' if bid > ask else 'ask' if ask > bid else 'equal',
            'predictive_claim': None}

from peft import PeftModel
assert hashlib.sha256((root/'adapter/adapter_model.safetensors').read_bytes()).hexdigest() == '48d2664db5b46246ee98bfd688318b2d28a6f14be0a10892117c6303ca5fc8bf'
(OUT/'protocol.json').write_text(json.dumps(dict(cases=cases,system=system,model=model_id,revision=revision,
    training_executed=False,independent_test=False,
    scope_origin='Explicit caller scope and calculator arguments; no automatic intent parsing or tool selection; system gains are not learned gains.'),indent=2))
for condition in ['base','adapter010']:
    if condition=='adapter010':
        base=PeftModel.from_pretrained(base,root/'adapter',is_trainable=False)
    for mode in ['conditional_evidence']:
        rows=[]
        for case in cases:
            decision=route_evidence(case['retrieved'],scope=case['scope'],source_id=case['source_id'])
            if not decision['model_allowed']:
                response=decision['response']; count=0; truncated=False
            else:
                set_seed(217)
                question=case['question']+'\n\nRetrieved evidence (may be irrelevant):\n'+json.dumps(decision['evidence'])
                if case.get('tool_args'):
                    checked=limit_price_rule(**case['tool_args'])
                    question+='\n\nVerified calculator result (explicit caller inputs, not inferred by the model):\n'+json.dumps(checked,default=str)
                    question+='\nExplain this result faithfully. Do not reverse its inequality or infer an actual execution.'
                effective_system=system
                if mode=='conditional_evidence':
                    effective_system = 'Answer the question using only the supplied evidence and any explicitly supplied verified tool output. First check whether the evidence supports the requested conclusion. If it does not, state what relevant evidence is missing; do not answer from memory or cite an unrelated passage. When supported, answer directly in at most three short sentences and cite the supporting evidence ID in square brackets. Make Yes or No agree with the question and explanation. Do not invent tool calls, calculator results, measurements or source details. Mention tools only when an actual tool result is supplied and relevant. Preserve uncertainty and distinguish possibility from certainty.'
                messages=[dict(role='system',content=effective_system),dict(role='user',content=question)]
                prompt=tokenizer.apply_chat_template(messages,tokenize=False,add_generation_prompt=True,enable_thinking=False)
                inputs=tokenizer(prompt,return_tensors='pt').to('cuda:0')
                base.eval()
                with torch.inference_mode():
                    output=base.generate(**inputs,do_sample=False,max_new_tokens=384,pad_token_id=tokenizer.pad_token_id,use_cache=True)
                generated=output[0,inputs.input_ids.shape[1]:]
                eos=base.generation_config.eos_token_id
                eos=[eos] if isinstance(eos,int) else eos
                count=len(generated); truncated=bool(count>=384 and generated[-1].item() not in eos)
                response=tokenizer.decode(generated,skip_special_tokens=True)
            rows.append(dict(id=case['id'],response=response,generated_tokens=count,hit_token_limit=truncated,
                model_invoked=decision['model_allowed'],prompt_condition=mode,route_status=decision['status'],evidence_ids=[e['id'] for e in decision['evidence']]))
            (OUT/(condition+'_'+mode+'.json')).write_text(json.dumps(rows,indent=2))
            print(condition,mode,case['id'],decision['status'],count,flush=True)
(OUT/'status.json').write_text(json.dumps(dict(status='complete',training_executed=False,production_approved=False,manual_review_required=True)))
