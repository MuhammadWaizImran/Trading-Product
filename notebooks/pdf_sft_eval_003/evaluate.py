"""Post-inspection diagnostic. Inference only, cloud only; no additional fitting.

Repairs ambiguous source context and inadequate output length in the first check.
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
OUT = Path('/kaggle/working/pdf_evaluation_003')
OUT.mkdir(parents=True, exist_ok=True)
subprocess.run([sys.executable, '-m', 'pip', 'install', '--quiet', '--retries', '1',
                'transformers==4.56.2', 'peft==0.17.1', 'accelerate==1.10.1',
                'bitsandbytes==0.47.0'], check=True)
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, set_seed
from peft import PeftModel
assert torch.cuda.is_available(), 'No GPU; local/CPU inference fallback disabled.'
roots = list(Path('/kaggle/input').rglob('pdf_sft_006/runtime.json'))
assert len(roots) == 1, f'Expected one attached training output; found {len(roots)}'
root = roots[0].parent
runtime = json.loads(roots[0].read_text())
status = json.loads((root/'status.json').read_text())
assert status['stage'] == 'completed_training_human_evaluation_pending'
revision = runtime['revision']
model_id = runtime['model']
assert model_id == 'Qwen/Qwen3-8B'
cases = [{'id': 'depth', 'question': 'Two exchanges have the same best ask. Must a large market buy cost the same on both?', 'rubric': 'No; different quantities/depth and fills can produce different average costs. Do not claim every large buy necessarily moves price.', 'evidence': {'source': 'DP17 PDF pages 35-37; reviewed educational summary', 'text': 'Equal best ask prices do not imply equal quantities at each ask level. Total execution cost depends on quantities and prices consumed across levels.'}}, {'id': 'unknown-paper', 'question': 'Using the convention in a paper that I have not identified or supplied, what does NOBI = -0.2 mean?', 'rubric': 'Ask for definition/source or state convention dependence; do not invent an expansion or a definite sign interpretation.', 'evidence': {'source': 'Question scope', 'text': 'No paper or definition was supplied. There is no evidence permitting a source-specific interpretation.'}}, {'id': 'provided-convention', 'question': 'Source context: normalized order-book imbalance is (ask depth - bid depth)/(ask depth + bid depth). Ask depth is 60 and bid depth is 100. Calculate it and interpret the sign.', 'rubric': '-0.25; bid-heavy. This is a description of displayed depth, not a guaranteed future return.', 'evidence': {'source': 'Deterministic research_math.py on the question inputs; not a measured market outcome', 'text': '{"value": "-0.25", "convention": "ask_minus_bid", "larger_displayed_side": "bid", "predictive_claim": null}'}}, {'id': 'payoff', 'question': 'A setup offers +4R if it wins and -1R if it loses. Does that reveal the actual win probability? What is cost-free break-even?', 'rubric': 'Actual probability unknown; 20% break-even under stated fixed payoffs.', 'evidence': {'source': 'Deterministic research_math.py on the question inputs; not a measured market outcome', 'text': '{"breakeven_probability": "0.2", "feasible": true, "expected_r": null, "actual_probability_known": false}'}}, {'id': 'sizing', 'question': 'A hypothetical account has USD 12,000, a 0.5% risk budget, and a 3% entry-to-stop distance. Ignore costs. Compute position notional and planned loss. Do not give coin quantity without an entry price.', 'rubric': 'USD 2,000 notional; USD 60 planned loss; quantity cannot be determined without entry price.', 'evidence': {'source': 'Deterministic research_math.py on the question inputs; not a measured market outcome', 'text': '{"status": "calculated", "risk_budget": "60.000", "notional": "2000.0", "quantity": null, "exceeds_account": false, "assumptions": "Linear spot; exact stop execution; no costs. Not an order."}'}}, {'id': 'no-stop', 'question': 'Account USD 5,000, risk budget 1%, entry USD 20 per coin. No stop or loss-per-coin estimate is supplied. Give the risk-at-stop coin quantity.', 'rubric': 'Insufficient information; budget USD 50 is known but risk-at-stop quantity is not.', 'evidence': {'source': 'Deterministic research_math.py on the question inputs; not a measured market outcome', 'text': '{"status": "insufficient_information", "risk_budget": "50.00", "missing": "entry-to-stop fractional loss", "notional": null, "quantity": null}'}}, {'id': 'backup-versus-key', 'question': 'An offline signing device still works and contains the key. Its only backup is destroyed. Are the funds already permanently inaccessible?', 'rubric': 'No; the working key remains accessible. Backup loss increases future loss risk; do not conflate backup destruction with destruction of all keys.', 'evidence': {'source': 'Explicit premise of the question; logical check', 'text': 'The original device is functional and contains the signing key. Only its backup was destroyed. The original signing key has not been stated to be lost.'}}, {'id': 'permission-properties', 'question': 'A ledger publishes source code but only approved institutions validate. Is validation permissionless?', 'rubric': 'No; distinguish source access from admission. No invented arithmetic.', 'evidence': {'source': 'DP03 PDF pages 46-49; reviewed adaptation', 'text': 'A permissionless system generally lets participants join validation under public protocol rules, while a permissioned system restricts validation or access to approved parties. Openness of source code, read access, transaction submission, and validation authority are separate properties and should be stated explicitly.'}}]
prompts = {'closed': 'Answer directly in no more than four short sentences and 100 words. Use only supplied evidence for source-specific claims. Calculate only when the question requires a calculation and the inputs are available. Otherwise explain in words. If a source or definition is missing, say what is missing. Do not invent facts, quotations, numbers, citations or profits.', 'provided_evidence': 'Answer directly in no more than four short sentences and 100 words. Use only supplied evidence for source-specific claims. Calculate only when the question requires a calculation and the inputs are available. Otherwise explain in words. If a source or definition is missing, say what is missing. Do not invent facts, quotations, numbers, citations or profits.'}
expected_hashes = {'004':'ab4250c6d48025e12c16aec4e35e54b9bf6a7fab6fec46ce44bdc70e2659dda3', '006':'e887415e71b18c75febd30867a857d64e95f9fbd114c1a570550b8d57f716615'}
adapter_dirs = {}
for batch, digest in expected_hashes.items():
 matches = list(Path('/kaggle/input').rglob(f'pdf_sft_{batch}/adapter/adapter_model.safetensors'))
 assert len(matches)==1
 assert hashlib.sha256(matches[0].read_bytes()).hexdigest()==digest
 adapter_dirs[batch]=matches[0].parent
(OUT/'protocol.json').write_text(json.dumps({'label':'post-inspection provided-evidence diagnostic; manually matched context, not tested retrieval; no fitting or promotion', 'cases':cases, 'prompts':prompts, 'model':model_id, 'revision':revision, 'adapter_hashes':expected_hashes},indent=2))
tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision, trust_remote_code=False)
tokenizer.pad_token = tokenizer.eos_token
dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
base = AutoModelForCausalLM.from_pretrained(model_id, revision=revision, trust_remote_code=False,
    device_map={'':0}, torch_dtype=dtype, attn_implementation='sdpa',
    quantization_config=BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type='nf4',
        bnb_4bit_use_double_quant=True, bnb_4bit_compute_dtype=dtype))
def evaluate(model, label, system, with_evidence):
    set_seed(217)
    model.eval()
    rows = []
    for case in cases:
        question = case['question']
        if with_evidence:
            question += '\n\nProvided evidence (use it to answer; identify missing information):\n' + json.dumps(case['evidence'])
        messages = [{'role':'system','content':system}, {'role':'user','content':question}]
        text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True, enable_thinking=False)
        inputs = tokenizer(text, return_tensors='pt').to('cuda:0')
        with torch.inference_mode():
            output = model.generate(**inputs, do_sample=False, max_new_tokens=384,
                                    pad_token_id=tokenizer.pad_token_id, use_cache=True)
        generated = output[0,inputs.input_ids.shape[1]:]
        eos = model.generation_config.eos_token_id
        eos = [eos] if isinstance(eos, int) else eos
        ended = bool(len(generated) and generated[-1].item() in eos)
        rows.append(dict(**case, response=tokenizer.decode(generated, skip_special_tokens=True),
                         generated_tokens=len(generated), ended_with_eos=ended,
                         hit_token_limit=len(generated) >= 384 and not ended))
        (OUT/f'{label}.json').write_text(json.dumps(rows, indent=2))
        print(label, case['id'], 'tokens', len(generated), 'ended', ended, flush=True)
    return rows
for name, system in prompts.items():
 evaluate(base, 'base_'+name, system, name=='provided_evidence')
adapted = PeftModel.from_pretrained(base, adapter_dirs['004'], adapter_name='run004', is_trainable=False)
adapted.load_adapter(adapter_dirs['006'],adapter_name='run006',is_trainable=False)
for batch in ['006']:
 adapted.set_adapter('run'+batch)
 for name, system in prompts.items():
  evaluate(adapted,'run'+batch+'_'+name,system,name=='provided_evidence')
(OUT/'status.json').write_text(json.dumps({'status':'complete','training_executed':False,'manual_review_required':True,'production_approved':False}))
print('DIAGNOSTIC_COMPLETE',flush=True)
