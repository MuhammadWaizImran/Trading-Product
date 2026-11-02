"""Build bounded cloud-only grounding correction experiment. No local ML execution."""
import ast
import base64
from collections import Counter
from copy import deepcopy
from datetime import datetime, timezone
import gzip
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MARKER='Supplied evidence (reviewed PDF adaptations):\n'


def main():
    prior=ROOT/'data/pdf_sft_batch_017'
    data=ROOT/'data/pdf_sft_batch_022'
    out=ROOT/'notebooks/pdf_sft_022'
    assert not data.exists() and not out.exists(), 'Preserve existing prepared run'
    manifest=json.loads((prior/'manifest.json').read_text())
    payload={}
    for split in ('train','validation','test'):
        raw=(prior/f'{split}.jsonl').read_bytes()
        assert hashlib.sha256(raw).hexdigest()==manifest['splits'][split]
        payload[split]=[json.loads(line) for line in raw.decode().splitlines()]
    bank={}; origins={}
    for row in payload['train']:
        ev=json.loads(row['messages'][1]['content'].split(MARKER)[1])
        for e in ev:bank[e['id']]=e
        if len(ev)==1:origins[ev[0]['id']]=deepcopy(row['provenance'])
    system=(ROOT/'notebooks/pdf_transfer_eval_021/system_prompt.txt').read_text().strip()
    # Use the same021 prompt for all inference comparisons and new fitting targets.
    for split in payload:
        for r in payload[split]:r['messages'][0]['content']=system
    def row(identifier, question, key, supported, answer, missing_key='dp16-receive-offline'):
        evidence=[bank[key]] if supported else [bank[missing_key]]
        provenance=deepcopy(origins[evidence[0]['id']])
        provenance['adaptation']+=' Run022 original grounding exercise; negative examples teach refusal to apply absent rules or attribute unidentified sources. No additional PDF coverage.'
        target=dict(status='supported' if supported else 'insufficient',answer=answer,
                    evidence_id=key if supported else None)
        return dict(id=identifier, provenance=provenance,evidence_ids=[e['id'] for e in evidence],
                    messages=[dict(role='system',content=system),
                              dict(role='user',content=question+'\n\n'+MARKER+json.dumps(evidence)),
                              dict(role='assistant',content=json.dumps(target))])
    def group(prefix, equity, borrow, prices, gains, loss, phrases):
        rows=[]
        p1,v1,p2,v2=prices
        specs=[('leverage','dp10-leverage-definition',
                f'Equity is ${equity} and a simplified cash loan is ${borrow}. Under the supplied total-exposure definition, calculate exposure and leverage.',
                f'Exposure is ${equity+borrow}; total-exposure leverage is {(equity+borrow)/equity:g}x.'),
               ('vwap','dp17-vwap-convention',
                f'Use the supplied trade-level VWAP rule for {v1} units at ${p1} and {v2} units at ${p2}; these are all included trades. What is VWAP?',
                f'Trade-level VWAP is ${(p1*v1+p2*v2)/(v1+v2):g}, using summed price times volume divided by summed volume.'),
               ('rsi','dp05-rsi-definition',
                f'Average gain is {gains} and average loss is {loss}. Apply the supplied RSI formula and state whether this guarantees a reversal.',
                f'RSI is {100-100/(1+gains/loss):g}. This does not guarantee a reversal.')]
        for name,key,question,answer in specs:
            rows.append(row(prefix+'-'+name+'-yes',question,key,True,answer))
            rows.append(row(prefix+'-'+name+'-no',question,key,False,
                            'The supplied passage does not provide the required rule. Please provide relevant evidence; I cannot give an evidence-grounded result from this passage.'))
        for i,phrase in enumerate(phrases):
            key='dp07-exchange-holder'
            question=phrase+' Did it prove that every exchange wallet is owned for the benefit of exactly one customer?'
            r=row(prefix+f'-source-{i}-no',question,key,False,
                  'Please identify the document or supply its text. I cannot determine what it concluded, and the supplied passage is not established as that document.',missing_key=key)
            rows.append(r)
            rows.append(row(prefix+f'-source-{i}-yes',
                            f'Using only dp07-exchange-holder, assess claim {i+1}: an exchange wallet necessarily represents one customer\'s assets and personal conviction.',key,True,
                            'That claim is not established. An exchange address may custody assets for many customers and support operational transfers; its balance does not necessarily express one investor\'s conviction.'))
        return rows
    added=group('r022-train-a',25,75,(4,2,10,1),4,1,
                ['I read a paper but have forgotten its name.', 'Someone mentioned a study; no citation or excerpt is available.', 'A trading newsletter was mentioned to me without a date, title or quotation.'])
    added+=group('r022-train-b',40,160,(10,3,14,1),1,4,
                 ['An article I cannot identify made a claim.', 'I heard about a research note but do not have the text or author.', 'A post was discussed, but neither the link nor its contents are available.'])
    # Avoid identical identified-source questions across the two training groups.
    for r in added[12:]:
        if '-source-' in r['id'] and r['id'].endswith('-yes'):
            r['messages'][1]['content']=r['messages'][1]['content'].replace('assess claim','evaluate assertion')
    heldout=group('r022-new-test',18,90,(5,2,17,2),7,3,
                  ['I remember reading a document last month, but I cannot name or quote it.', 'A friend referred to a publication without sharing any identifying details.', 'There was an analysis somewhere online; I do not know which one.'])
    for r in heldout:
        r['messages'][1]['content']=r['messages'][1]['content'].replace('assess claim','consider proposition')
    payload['train']+=added
    exposed=json.loads((ROOT/'notebooks/pdf_transfer_eval_021/cases.json').read_text())
    payload['test']=deepcopy(exposed)+heldout
    train_questions={r['messages'][1]['content'] for r in payload['train']}
    assert all(r['messages'][1]['content'] not in train_questions for r in payload['test'])
    assert len({r['messages'][1]['content'] for r in added})==24
    assert len(payload['train'])==190 and len(payload['test'])==28
    raw={s:''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in payload[s]).encode() for s in ('train','validation','test')}
    manifest.update(batch='022',created_utc=datetime.now(timezone.utc).isoformat(),parent_adapter=None,
        counts={s:len(payload[s]) for s in raw},splits={s:hashlib.sha256(v).hexdigest() for s,v in raw.items()},
        previous_training_data_sha256=manifest['splits']['train'],
        training_sources=dict(Counter(r['provenance']['source_id'] for r in payload['train'])),
        system_prompt_sha256=hashlib.sha256(system.encode()).hexdigest(),
        method='Fresh pinned base Qwen3-8B QLoRA, rank8 all-linear, LR1e-5,2 epochs. Retain166 examples and add24 grounding contrasts; align all system prompts to021. Not continuation of adapter017.',
        hypothesis='Explicit abstention without leaked verdicts and paired source-identity examples can reduce021 unsupported answers.',
        evaluation='16 exposed021 regression questions plus12 new author-reviewed diagnostic questions. Same-run base/new adapter/reload with021 thinking sampling settings. No independent acceptance.',
        decision_rule='No promotion. Reject any unidentified-source attribution, unsupported verdict under insufficient, arithmetic regression or truncation. Compare semantic failures to same-run base; no endless automatic successor.',
        limitation='Known passages and correlated examples. Prompt alignment and data augmentation both changed; not a single-variable causal ablation. No broader PDF review or trading profitability evidence.',
        comparison='Same-run base and trained adapter;017 results from021 are historical only. New heldout questions are author-reviewed, not externally independent.')
    payload['manifest']=manifest
    payload['attribution']=(prior/'ATTRIBUTION.txt').read_text()+'\nRun022:24 original exercises derived from existing reviewed passages; same private permission basis. No new PDF ingestion.\n'
    source=(ROOT/'notebooks/pdf_sft_017/train.py').read_text()
    node=next(n for n in ast.parse(source).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PAYLOAD' for t in n.targets))
    packed=base64.b64encode(gzip.compress(json.dumps(payload).encode(),mtime=0)).decode()
    lines=source.splitlines(keepends=True)
    lines[node.lineno-1:node.end_lineno]=['PAYLOAD = json.loads(gzip.decompress(base64.b64decode('+repr(packed)+')))\n']
    source=''.join(lines).replace('pdf_sft_017','pdf_sft_022')
    source=source.replace('def prompt(row):','def prompt(row, thinking=False):').replace('enable_thinking=False)', 'enable_thinking=thinking)')
    source=source.replace("inputs = tokenizer(prompt(row), return_tensors='pt').to('cuda:0')", "set_seed(217)\n                inputs = tokenizer(prompt(row, thinking=True), return_tensors='pt').to('cuda:0')")
    source=source.replace('do_sample=False, max_new_tokens=384,','do_sample=True, temperature=0.6, top_p=0.95, top_k=20, max_new_tokens=2048,')
    source=source.replace('>=384)', '>=2048)')
    source=source.replace('results.append(dict(id=row', "raw_response=tokenizer.decode(answer[0,inputs.input_ids.shape[1]:], skip_special_tokens=True)\n                results.append(dict(final_response=raw_response.split('</think>',1)[1].strip() if '</think>' in raw_response else '', thinking=True, id=row")
    # Require the unadapted baseline and restore cache after training for inference.
    source=source.replace("generate('baseline_answers')", "with model.disable_adapter():\n            generate('baseline_answers')")
    source=source.replace("status('adapter_evaluation')", "model.config.use_cache = True\n        status('adapter_evaluation')")
    ast.parse(source)
    data.mkdir();out.mkdir()
    for s,bytes_ in raw.items():(data/f'{s}.jsonl').write_bytes(bytes_)
    (data/'manifest.json').write_text(json.dumps(manifest,indent=2))
    (data/'ATTRIBUTION.txt').write_text(payload['attribution'],encoding='utf-8')
    (out/'train.py').write_text(source,encoding='utf-8')
    meta=json.loads((ROOT/'notebooks/pdf_sft_017/kernel-metadata.json').read_text())
    meta.update(id='waizimran/crypto-qwen3-pdf-sft-022',title='Crypto Qwen3 PDF SFT 022')
    assert meta['is_private'] and meta['enable_gpu']
    (out/'kernel-metadata.json').write_text(json.dumps(meta,indent=2))
    print(json.dumps(dict(counts=manifest['counts'],sha256=hashlib.sha256(source.encode()).hexdigest(),local_training=False)))


if __name__=='__main__':main()
