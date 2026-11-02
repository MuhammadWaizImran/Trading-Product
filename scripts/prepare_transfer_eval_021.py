"""Prepare new evidence-transfer diagnostic; never loads or fits a model locally."""
import ast
from copy import deepcopy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'notebooks/pdf_transfer_eval_021'
MARKER = 'Supplied evidence (reviewed PDF adaptations):\n'


def main():
    source = (ROOT / 'notebooks/pdf_scope_eval_020/evaluate.py').read_text(encoding='utf-8')
    assignment = next(n for n in ast.parse(source).body
                      if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'PAYLOAD' for t in n.targets))
    payload = json.loads(ast.literal_eval(assignment.value.args[0]))
    bank, provenance = {}, {}
    training = [json.loads(line) for line in (ROOT / 'data/pdf_sft_batch_017/train.jsonl').read_text().splitlines()]
    for row in training:
        for e in json.loads(row['messages'][1]['content'].split(MARKER)[1]):
            bank[e['id']] = e
        # Original single-passage rows carry the corresponding page provenance.
        if not row['id'].startswith('r017-mixed-'):
            for e in json.loads(row['messages'][1]['content'].split(MARKER)[1]):
                provenance[e['id']] = row['provenance']
    system = (ROOT / 'notebooks/pdf_scope_eval_020/system_prompt.txt').read_text().strip()
    specs = [
        ('leverage', 'dp10-leverage-definition',
         'Using the supplied total-exposure definition, equity is $32 and borrowed funds are $96. What is total exposure and leverage?',
         'Total exposure is $128 and leverage is 4x, not 3x.', ['128', '4']),
        ('vwap', 'dp17-vwap-convention',
         'The complete included trades are 3 units at $7 and 1 unit at $11. Using the supplied rule, calculate trade-level VWAP.',
         'VWAP is (3*7+1*11)/4 = $8.', ['8']),
        ('rsi', 'dp05-rsi-definition',
         'Using the supplied RSI rule, average gain is 6 and average loss is 2. Is RSI 25 or 75? Does that number guarantee a reversal?',
         'RSI is 75; it does not guarantee a reversal.', ['75']),
        ('depth', 'dp17-spread-depth',
         'Best ask is $20 for 2 units; next ask is $21 for 3 units. A market buy takes 4 units from this unchanged book, with zero fees. Can all four fill at $20? What is the average?',
         'No; 2 units fill at $20 and 2 at $21, averaging $20.50.', ['20.5']),
        ('custody', 'dp07-exchange-holder',
         'A labelled custodial exchange address receives tokens. Does that establish that one individual investor bought them out of personal conviction?',
         'No; the address may hold customer assets or support operational transfers. Attribution and intent are not established.', []),
        ('offline', 'dp16-receive-offline',
         'A recipient signing device is powered off, but the sender knows the valid receiving address. Does that alone prevent the sender broadcasting a payment?',
         'No. Broadcasting to a known valid address does not require the receiving signing device online; confirmation and spending are separate.', []),
    ]
    cases = []
    def add(identifier, question, evidence, status, reference, target=None, numeric=None):
        p = deepcopy(provenance[evidence[0]['id']])
        p['adaptation'] = 'New author-reviewed diagnostic question using existing checked adaptations; not independent human acceptance.'
        cases.append(dict(id=identifier, provenance=p, evidence=evidence,
                          expected_status=status, expected_evidence_id=target,
                          required_numeric_concepts=numeric or [],
                          messages=[dict(role='system', content=system),
                                    dict(role='user', content=question+'\n\n'+MARKER+json.dumps(evidence)),
                                    dict(role='assistant', content=reference)],
                          evidence_ids=[e['id'] for e in evidence]))
    for name, key, question, reference, numbers in specs:
        distractor = bank['dp16-receive-offline' if key != 'dp16-receive-offline' else 'dp10-leverage-definition']
        add('transfer021-'+name+'-relevant', question, [distractor, bank[key]], 'supported', reference, key, numbers)
        add('transfer021-'+name+'-missing', question, [distractor], 'insufficient',
            'The supplied passage does not support the requested rule or conclusion; request relevant evidence.')
    for label, noun in [('report', 'report'), ('survey', 'survey')]:
        e = bank['dp07-exchange-holder']
        add('transfer021-'+label+'-unidentified',
            f'I saw a {noun} yesterday but cannot provide its title or text. Did that {noun} establish that every exchange address represents just one person?',
            [e], 'insufficient', 'Ask for the source; do not attribute the supplied passage to the unidentified document.')
        add('transfer021-'+label+'-identified',
            ('According to passage dp07-exchange-holder, must an exchange address represent just one individual investor?' if label == 'report' else
             'Read only dp07-exchange-holder: is the balance of an exchange address sufficient evidence of one investor\'s conviction?'),
            [e], 'supported', 'No; exchange addresses can custody assets for many customers.', e['id'])
    previous_questions = {r['messages'][1]['content'].split(MARKER)[0].strip() for r in training + payload['test']}
    assert all(r['messages'][1]['content'].split(MARKER)[0].strip() not in previous_questions for r in cases)
    assert len({r['id'] for r in cases}) == 16
    assert len({r['messages'][1]['content'] for r in cases}) == 16
    payload['test'] = cases
    protocol = dict(training_executed=False, cases=16, generations=32,
                    comparison='New author-reviewed paired evidence-transfer diagnostic, same known passages and same020 prompt; not independent acceptance or trading accuracy.',
                    acceptance='Diagnostic only. No promotion from this suite. Report exact schema, status/citation, truncation and separately reviewed semantic correctness for both models; inspect every contrast pair.',
                    adapter_sha256='98a59cc00ae482e751915af12fee3d6d8fa942755319d91c37567e1e1fb6fd42')
    source_lines = source.splitlines()
    source_lines[assignment.lineno-1:assignment.end_lineno] = ['PAYLOAD = json.loads('+repr(json.dumps(payload))+')']
    source = '\n'.join(source_lines).replace('pdf_scope_020', 'pdf_transfer_021')+'\n'
    tree = ast.parse(source)
    protocol_call = next(n for n in ast.walk(tree) if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call)
                         and isinstance(n.value.func, ast.Name) and n.value.func.id == 'save'
                         and n.value.args and isinstance(n.value.args[0], ast.Constant) and n.value.args[0].value == 'protocol.json')
    lines = source.splitlines()
    lines[protocol_call.lineno-1:protocol_call.end_lineno] = ["        save('protocol.json', "+repr(protocol)+')']
    source = '\n'.join(lines)+'\n'
    ast.parse(source)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'evaluate.py').write_text(source, encoding='utf-8')
    for filename, obj in [('cases.json', cases), ('review_protocol.json', protocol)]:
        (OUT / filename).write_text(json.dumps(obj, indent=2), encoding='utf-8')
    metadata = json.loads((ROOT / 'notebooks/pdf_scope_eval_020/kernel-metadata.json').read_text())
    metadata.update(id='waizimran/crypto-qwen3-transfer-check-021', title='Crypto Qwen3 Transfer Check 021')
    assert metadata['is_private'] is True
    (OUT / 'kernel-metadata.json').write_text(json.dumps(metadata, indent=2), encoding='utf-8')
    (OUT / 'system_prompt.txt').write_text(system, encoding='utf-8')
    print(json.dumps(dict(cases=len(cases), generations=len(cases)*2, training=False,
                         code_sha256=hashlib.sha256(source.encode()).hexdigest())))


if __name__ == '__main__':
    main()
