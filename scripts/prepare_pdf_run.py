"""Build a private cloud continuation from reviewed PDF examples. Never fits a model.

Example:
python scripts/prepare_pdf_run.py --batch 003 --parent-batch 002 \
  --parent-results results/pdf_sft_002_v1/pdf_sft_002 \
  --examples research/pdf_training_dp01.json
"""
import argparse
import ast
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def read_json(path):
    return json.loads(path.read_text(encoding='utf8'))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replace_once(source, old, new):
    if source.count(old) != 1:
        raise ValueError('Trainer template changed; review the generator before proceeding: '+old[:90])
    return source.replace(old, new)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--batch', required=True)
    ap.add_argument('--parent-batch', required=True)
    ap.add_argument('--parent-results', required=True, type=Path)
    ap.add_argument('--examples', required=True, type=Path)
    ap.add_argument('--epochs', type=int, default=2, choices=range(1, 5), metavar='1-4')
    ap.add_argument('--learning-rate', type=float, default=0.0001)
    ap.add_argument('--validate-only', action='store_true', help='Check real source data and parent; write nothing')
    args = ap.parse_args()
    assert re.fullmatch(r'\d{3}', args.batch) and re.fullmatch(r'\d{3}', args.parent_batch)
    assert int(args.batch) > int(args.parent_batch), 'Use a new, later batch number'
    assert 0 < args.learning_rate <= 0.001, 'Learning rate is outside the reviewed safety range'
    assert not (ROOT/f'notebooks/pdf_sft_{args.batch}').exists(), 'Refuse to overwrite an existing run'
    assert not (ROOT/f'data/pdf_sft_batch_{args.batch}').exists(), 'Refuse to overwrite an existing dataset'
    parent = args.parent_results.resolve()
    runtime = read_json(parent/'runtime.json')
    assert read_json(parent/'status.json')['stage'] == 'completed_training_human_evaluation_pending', 'Parent must have completed fitting'
    assert runtime['model'] == 'Qwen/Qwen3-8B'
    assert re.fullmatch(r'[0-9a-f]{40}', runtime['revision']), 'Exact base revision required'
    parent_hash = sha(parent/'adapter/adapter_model.safetensors')
    parent_data = ROOT/f'data/pdf_sft_batch_{args.parent_batch}'
    parent_manifest = read_json(parent_data/'manifest.json')
    assert read_json(parent/'dataset_manifest.json') == parent_manifest, 'Local parent data differs from actual cloud dataset'
    inventory = {r['id']:r for r in read_json(ROOT/'tmp/pdfs/data_pdf_review/inventory.json')}
    payload = {}
    for split in ('train','validation','test'):
        path = parent_data/f'{split}.jsonl'
        assert sha(path) == parent_manifest['splits'][split], 'Frozen parent split has changed'
        payload[split] = [json.loads(line) for line in path.read_text(encoding='utf8').splitlines()]
    new = read_json(args.examples)
    assert isinstance(new,list) and new, 'Examples must be a nonempty JSON array'
    counts = Counter(r['split'] for r in new)
    assert set(counts) == {'train','validation','test'}, 'All three splits required'
    assert counts['train'] >= 8 and counts['validation'] >= 2 and counts['test'] >= 2, 'Prepare substantive training and separate checks'
    old_ids = {r['id'] for s in payload for r in payload[s]}
    ids = [r['id'] for r in new]
    assert len(ids)==len(set(ids)) and not old_ids.intersection(ids), 'Duplicate example ID'
    existing_questions = {r['messages'][-2]['content'].strip().casefold() for s in payload for r in payload[s]}
    new_questions = [r['question'].strip().casefold() for r in new]
    assert len(new_questions)==len(set(new_questions)) and not existing_questions.intersection(new_questions), 'Repeated question; check leakage'
    assert len(payload['train'])+counts['train'] <= 2000, 'Reassess free-compute budget before growing beyond 2,000 examples'
    checked = set()
    system = ('You are a crypto research assistant. Explain concepts accurately, distinguish definitions from '
              'evidence of profitable predictions, state assumptions, and acknowledge missing information. '
              'Never promise trading returns. Answer directly in at most four short sentences.')
    for row in new:
        src = inventory[row['source']]
        assert not src['duplicate_of'] and row['source'] != 'DP20', 'Use the canonical source for duplicates'
        assert row['pages'] and all(type(p) is int and 1 <= p <= src['pages'] for p in row['pages'])
        assert all(isinstance(row[k],str) and row[k].strip() for k in ('question','answer','adaptation'))
        if row['source'] not in checked:
            assert sha(ROOT/'Data PDF'/src['file']) == src['sha256'], 'PDF changed since extraction'
            checked.add(row['source'])
        provenance = dict(source_id=row['source'],file=src['file'],sha256=src['sha256'],pdf_pages=row['pages'],
            permission='User attested permission for private model training; independently unverified.',adaptation=row['adaptation'])
        payload[row['split']].append(dict(id=row['id'],provenance=provenance,messages=[
            {'role':'system','content':system},{'role':'user','content':row['question']},{'role':'assistant','content':row['answer']}]))
    # Syntax validation and serialization are allowed locally; no model/tokenizer imports.
    split_text = {s:''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in payload[s]) for s in payload}
    payload['manifest'] = dict(batch=args.batch, model=runtime['model'],revision=runtime['revision'],
        parent_batch=args.parent_batch,parent_kernel=f'waizimran/crypto-qwen3-pdf-sft-{args.parent_batch}',
        parent_adapter_sha256=parent_hash,created_utc=datetime.now(timezone.utc).isoformat(),
        splits={s:hashlib.sha256(t.encode('utf8')).hexdigest() for s,t in split_text.items()},
        counts={s:len(payload[s]) for s in split_text},new_counts=dict(counts),new_sources=sorted(checked),
        new_example_ids=ids,new_examples_file=args.examples.as_posix(),new_examples_sha256=sha(args.examples),
        review_attestation='Prepared examples must be manually checked against source pages. This script checks structure, hashes and exact duplicates, not truth or complete semantic leakage.',
        scope='Selected reviewed passages only; no assertion of complete PDF ingestion.',
        replay='All earlier training examples; earlier validation/test remain excluded from fitting.',
        epochs=args.epochs,learning_rate=args.learning_rate,optimizer_restart=True,
        evaluation='New application checks plus exposed retention checks; concept overlap remains. Manual review required. No automatic selection or retries based on test score.',
        decision_rule='At least 75% of new test answers substantively correct, no new severe errors relative to parent on retention checks; reject promotion on loss alone.',
        ledger=[dict(source_id=sid,file=r['file'],duplicate_of=r['duplicate_of'] or ('DP19' if sid=='DP20' else None),
                     selected_train_examples=sum(x['provenance']['source_id']==sid for x in payload['train'])) for sid,r in inventory.items()])
    attribution = (parent_data/'ATTRIBUTION.txt').read_text(encoding='utf8')
    for sid in sorted(checked):
        attribution += '\nAdditional source '+sid+': '+inventory[sid]['file']+'. User-attested private training permission. Paraphrased/qualified; no endorsement.\n'
    if 'DP01' in checked:
        attribution += ('World Bank. 2018. Cryptocurrencies and Blockchain. Europe and Central Asia Economic Update (May), Washington, DC: World Bank. '
                        'CC BY 3.0 IGO, https://creativecommons.org/licenses/by/3.0/igo/. '
                        'This is an adaptation of an original work by The World Bank. Views and opinions expressed in the adaptation are the sole responsibility '
                        'of the author or authors of the adaptation and are not endorsed by The World Bank. '
                        'No third-party chart images reproduced.\n')
    if 'DP03' in checked:
        attribution += ('Center for the Governance of Change, IE University. 2019. Cryptocurrencies and the Future of Money. '
                        'Research directed by Mike Seiferling with Thamin Ahmed, Abeer Yehia ElBahrawy, Keith Chan and Tales Padilha; © 2020 CGC. '
                        'CC BY-NC-SA 4.0, https://creativecommons.org/licenses/by-nc-sa/4.0/. '
                        'This private noncommercial adaptation corrects or qualifies identified source errors; no author endorsement is implied. '
                        'No chart images reproduced.\n')
    if 'DP04' in checked:
        attribution += ('Peter Evans-Greenwood, Ian Harper, Robert Hillard and Peter Williams. 2015. The Future of Exchanging Value: '
                        'Cryptocurrencies and the Trust Economy. Deloitte. Nicholas Gruen contributed the foreword. '
                        'User-attested private training permission; no open license independently identified and no endorsement implied. '
                        'No chart images reproduced.\n')
    payload['attribution'] = attribution
    source = (ROOT/'scripts/pdf_cloud_trainer.py').read_text(encoding='utf8')
    source = source.replace('pdf_sft_001',f'pdf_sft_{args.batch}')
    source = replace_once(source,'from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training',
                          'from peft import PeftModel, prepare_model_for_kbit_training')
    source = replace_once(source,'revision = model_info(model_id).sha',"revision = PAYLOAD['manifest']['revision']")
    source = replace_once(source,"""        model = get_peft_model(model, LoraConfig(r=8, lora_alpha=16, lora_dropout=0.05,
            target_modules=['q_proj', 'v_proj'], task_type='CAUSAL_LM', bias='none'))""",f"""        parents = list(Path('/kaggle/input').rglob('pdf_sft_{args.parent_batch}/adapter/adapter_model.safetensors'))
        assert len(parents) == 1, 'Expected one attached parent adapter'
        assert hashlib.sha256(parents[0].read_bytes()).hexdigest() == PAYLOAD['manifest']['parent_adapter_sha256']
        model = PeftModel.from_pretrained(model, parents[0].parent, is_trainable=True)
        assert any(p.requires_grad for p in model.parameters())
        model.print_trainable_parameters()""")
    source = replace_once(source,'num_train_epochs=1,',f'num_train_epochs={args.epochs},')
    source = replace_once(source,'learning_rate=1e-4,',f'learning_rate={args.learning_rate!r},')
    source = replace_once(source,"save_strategy='no', report_to=[]","save_strategy='steps', save_steps=10, save_total_limit=2, report_to=[]")
    # Evaluation gets a fixed concise prompt independent of historical per-row prompts.
    source = replace_once(source,"""                inputs = tokenizer(prompt(row), return_tensors='pt').to('cuda:0')""", """                eval_messages = [
                    {'role':'system','content':'Answer the question directly in no more than four short sentences and 100 words. Use the stated source convention, show essential arithmetic, acknowledge missing information, and do not invent definitions or promise profits.'},
                    {'role':'user','content':row['messages'][-2]['content']}]
                eval_text = tokenizer.apply_chat_template(eval_messages, tokenize=False,
                    add_generation_prompt=True, enable_thinking=False)
                inputs = tokenizer(eval_text, return_tensors='pt').to('cuda:0')""")
    source = replace_once(source,'max_new_tokens=220','max_new_tokens=192')
    source = replace_once(source,"response=tokenizer.decode(answer[0,inputs.input_ids.shape[1]:], skip_special_tokens=True)))", """response=tokenizer.decode(answer[0,inputs.input_ids.shape[1]:], skip_special_tokens=True),
                    generated_tokens=int(answer.shape[1]-inputs.input_ids.shape[1]),
                    ended_with_eos=bool(answer[0,-1].item() in ([model.generation_config.eos_token_id] if isinstance(model.generation_config.eos_token_id,int) else model.generation_config.eos_token_id)),
                    hit_token_limit=bool(answer.shape[1]-inputs.input_ids.shape[1] >= 192)))""")
    source = source.replace("'baseline_evaluation'","'parent_adapter_evaluation'").replace("generate('baseline_answers')","generate('parent_answers')")
    source = replace_once(source,'PAYLOAD = None  # EMBED_PDF_PAYLOAD','PAYLOAD = json.loads('+repr(json.dumps(payload,ensure_ascii=False))+')')
    ast.parse(source)
    metadata = dict(id=f'waizimran/crypto-qwen3-pdf-sft-{args.batch}',title=f'Crypto Qwen3 PDF SFT {args.batch}',
        code_file='train.py',language='python',kernel_type='script',is_private=True,enable_gpu=True,enable_internet=True,
        dataset_sources=[],competition_sources=[],kernel_sources=[payload['manifest']['parent_kernel']])
    if not args.validate_only:
        data = ROOT/f'data/pdf_sft_batch_{args.batch}'
        out = ROOT/f'notebooks/pdf_sft_{args.batch}'
        data.mkdir(); out.mkdir()
        for split,value in split_text.items():
            # Exact bytes keep recorded hashes stable across Windows and Linux.
            (data/f'{split}.jsonl').write_bytes(value.encode('utf8'))
        (data/'manifest.json').write_text(json.dumps(payload['manifest'],indent=2),encoding='utf8')
        (data/'ATTRIBUTION.txt').write_text(attribution,encoding='utf8')
        (out/'train.py').write_text(source,encoding='utf8')
        (out/'kernel-metadata.json').write_text(json.dumps(metadata,indent=2),encoding='utf8')
    print(json.dumps(dict(validation='PASS',validate_only=args.validate_only,batch=args.batch,
                         counts=payload['manifest']['counts'],new_sources=sorted(checked),
                         training_executed_locally=False,submitted_to_cloud=False)))


if __name__ == '__main__':
    main()
