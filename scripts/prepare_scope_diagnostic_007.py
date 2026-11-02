"""Freeze a cloud-only pipeline comparison; local preparation, no ML execution."""
import ast
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
out=ROOT/'notebooks/pdf_scope_eval_007'
assert not out.exists(), 'Refuse to overwrite a frozen experiment'
rows=[json.loads(s) for s in (ROOT/'data/pdf_sft_batch_009/test.jsonl').read_text(encoding='utf8').splitlines()]
cases=[]
for row in rows:
    if not row['id'].startswith('r009-'): continue
    prompt=row['messages'][1]['content']
    evidence=json.loads(prompt.split('Supplied evidence (reviewed PDF adaptations):\n')[1])
    unknown=row['id'].startswith('r009-unknown-')
    specific=unknown or row['id']=='r009-known-chart'
    cases.append(dict(id=row['id'],question=prompt.split('\n\nSupplied evidence')[0],retrieved=evidence,
        rubric=row['messages'][2]['content'],scope='source_specific' if specific else 'general',
        source_id='DP04' if row['id']=='r009-known-chart' else None))
assert len(cases)==8
source=(ROOT/'notebooks/pdf_adapter_eval_006/evaluate.py').read_text(encoding='utf8')
node=next(n for n in ast.parse(source).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='cases' for t in n.targets))
lines=source.splitlines(keepends=True); lines[node.lineno-1:node.end_lineno]=['cases = json.loads('+repr(json.dumps(cases))+')\n']
source=''.join(lines).replace('pdf_adapter_006','pdf_scope_007').replace('pdf_sft_008','pdf_sft_009')
source=source.split("(OUT/'protocol.json').write_text")[0]
gate=(ROOT/'workbench/source_scope.py').read_text(encoding='utf8')
source+='\n'+gate+'\n'
source+='''
from peft import PeftModel
assert hashlib.sha256((root/'adapter/adapter_model.safetensors').read_bytes()).hexdigest() == '6fdb8686e878e8d027646bfeb34df7bd859eb702a420bfe2218a6ef29ff4d503'
(OUT/'protocol.json').write_text(json.dumps(dict(cases=cases,system=system,model=model_id,revision=revision,
    training_executed=False,independent_test=False,
    scope_origin='Manually assigned explicit request metadata, not automatically classified; system comparison, not learned improvement.'),indent=2))
for condition in ['base','adapter009']:
    if condition=='adapter009':
        base=PeftModel.from_pretrained(base,root/'adapter',is_trainable=False)
    for mode in ['unguarded','scoped']:
        rows=[]
        for case in cases:
            decision=route_evidence(case['retrieved'],scope=case['scope'],source_id=case['source_id']) if mode=='scoped' else dict(model_allowed=True,evidence=case['retrieved'],status='bypassed')
            if not decision['model_allowed']:
                response=decision['response']; count=0; truncated=False
            else:
                set_seed(217)
                question=case['question']+'\\n\\nRetrieved evidence (may be irrelevant):\\n'+json.dumps(decision['evidence'])
                messages=[dict(role='system',content=system),dict(role='user',content=question)]
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
                model_invoked=decision['model_allowed'],route_status=decision['status'],evidence_ids=[e['id'] for e in decision['evidence']]))
            (OUT/(condition+'_'+mode+'.json')).write_text(json.dumps(rows,indent=2))
            print(condition,mode,case['id'],decision['status'],count,flush=True)
(OUT/'status.json').write_text(json.dumps(dict(status='complete',training_executed=False,production_approved=False,manual_review_required=True)))
'''
ast.parse(source)
protocol=dict(cases=cases,conditions=['base','adapter009'],modes=['unguarded','scoped'],responses=32,
    gate_sha256=hashlib.sha256(gate.encode()).hexdigest(),code_sha256=hashlib.sha256(source.encode()).hexdigest(),
    scope_origin='Explicit manually assigned request metadata; cannot infer these labels from unstructured user text.',
    decision='All three unidentified-source requests must be needs_source without model execution. Known/general cases must remain answerable without new errors. Compare citations and semantics manually. Gate gains belong to the pipeline, not model training. No expert/production approval from this exposed diagnostic.')
out.mkdir(); (out/'evaluate.py').write_text(source,encoding='utf8'); (out/'review_protocol.json').write_text(json.dumps(protocol,indent=2),encoding='utf8')
m=json.loads((ROOT/'notebooks/pdf_adapter_eval_006/kernel-metadata.json').read_text()); m.update(id='waizimran/crypto-qwen3-pdf-source-scope-007',title='Crypto Qwen3 PDF Source Scope 007',kernel_sources=['waizimran/crypto-qwen3-pdf-sft-009'])
assert m['is_private'] and m['enable_gpu']
(out/'kernel-metadata.json').write_text(json.dumps(m,indent=2))
print('Prepared 8 cases x 2 models x 2 pipeline modes. No local model execution.')
