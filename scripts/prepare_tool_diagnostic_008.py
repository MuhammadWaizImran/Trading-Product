"""Prepare a private cloud diagnostic. No local model imports or execution."""
import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'notebooks/pdf_tool_eval_008'
assert not OUT.exists(), 'Frozen experiment already exists'
prior = ROOT/'notebooks/pdf_scope_eval_007'
cases = json.loads((prior/'review_protocol.json').read_text())['cases']
limit = next(c for c in cases if c['id']=='r009-sell-direction')
limit['tool_args'] = dict(side='sell', limit_price='240', hypothetical_fill_price='235')
for side, price, fill in [('sell','240','245'),('buy','240','235'),('buy','240','245'),('sell','0.1001','0.1000'),('buy','240','240')]:
    cases.append(dict(id=f't008-{side}-{price}-{fill}',
        question=f'A {side} limit is {price}. Does a hypothetical fill at {fill} satisfy its gross price constraint? Is execution guaranteed?',
        retrieved=limit['retrieved'], scope='general', source_id=None,
        tool_args=dict(side=side,limit_price=price,hypothetical_fill_price=fill),
        rubric='Use the exact buy<=limit/sell>=limit constraint; never guarantee execution; cite limit-order.'))
source = (prior/'evaluate.py').read_text(encoding='utf8')
node = next(n for n in ast.parse(source).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='cases' for t in n.targets))
lines=source.splitlines(keepends=True)
lines[node.lineno-1:node.end_lineno]=['cases = json.loads('+repr(json.dumps(cases))+')\n']
source=''.join(lines).replace('pdf_scope_007','pdf_tool_008')
source=source.replace('Replays all 16 diagnostic 004 packets against base and adapter008 with identical prompts.',
                      'Compares explicit calculator context for base and adapter009 on 13 development cases.')
math_source=(ROOT/'scripts/research_math.py').read_text(encoding='utf8')
source=source.replace('from peft import PeftModel',math_source+'\nfrom peft import PeftModel')
source=source.replace("for mode in ['unguarded','scoped']:","for mode in ['scoped','scoped_tools']:")
source=source.replace(" if mode=='scoped' else dict(model_allowed=True,evidence=case['retrieved'],status='bypassed')",'')
needle="                messages=[dict(role='system',content=system),dict(role='user',content=question)]"
replacement="""                if mode=='scoped_tools' and case.get('tool_args'):
                    checked=limit_price_rule(**case['tool_args'])
                    question+='\\n\\nVerified calculator result (explicit caller inputs, not inferred by the model):\\n'+json.dumps(checked,default=str)
                    question+='\\nExplain this result faithfully. Do not reverse its inequality or infer an actual execution.'
                messages=[dict(role='system',content=system),dict(role='user',content=question)]"""
assert needle in source
source=source.replace(needle,replacement)
source=source.replace("scope_origin='Manually assigned explicit request metadata, not automatically classified; system comparison, not learned improvement.'",
    "scope_origin='Explicit caller scope and calculator arguments; no automatic intent parsing or tool selection; system gains are not learned gains.'")
ast.parse(source)
assert 'is_trainable=False' in source and "assert torch.cuda.is_available()" in source
protocol=dict(cases=cases,responses=52,models=['base','adapter009'],modes=['scoped','scoped_tools'],
    independent_test=False,training_executed=False,
    code_sha256=hashlib.sha256(source.encode()).hexdigest(),
    math_sha256=hashlib.sha256(math_source.encode()).hexdigest(),
    decision='Manually read all outputs. All six limit cases must preserve calculator truth, deny guaranteed execution and cite supporting evidence. Three unidentified sources must route without model invocation. Known evidence cases must remain correct and cited. Any severe error blocks promotion. This exposed diagnostic may guide future training but is not final acceptance.',
    limitations='Inputs and tool dispatch are manually supplied, not learned; no full-corpus review, profit claims or live orders.')
OUT.mkdir()
(OUT/'evaluate.py').write_text(source,encoding='utf8')
(OUT/'review_protocol.json').write_text(json.dumps(protocol,indent=2),encoding='utf8')
metadata=json.loads((prior/'kernel-metadata.json').read_text())
metadata.update(id='waizimran/crypto-qwen3-pdf-tool-check-008',title='Crypto Qwen3 PDF Tool Check 008')
assert metadata['is_private'] and metadata['enable_gpu']
(OUT/'kernel-metadata.json').write_text(json.dumps(metadata,indent=2))
print('Prepared 13 cases x 2 models x 2 conditions; cloud-only evaluation, not new fitting.')
