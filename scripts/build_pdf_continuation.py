"""Prepare the second, cumulative private cloud run. No model execution."""
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'notebooks/pdf_sft_002'
DATA = ROOT/'data/pdf_sft_batch_002'
inventory = json.loads((ROOT/'tmp/pdfs/data_pdf_review/inventory.json').read_text(encoding='utf8'))
sources = {r['id']: r for r in inventory}
rows = json.loads((ROOT/'research/pdf_training_dp07.json').read_text(encoding='utf8'))
assert Counter(r['split'] for r in rows) == {'train':24, 'validation':4, 'test':4}
prior = ROOT/'data/pdf_sft_batch_001'
payload = {s: [json.loads(line) for line in (prior/f'{s}.jsonl').read_text(encoding='utf8').splitlines()]
           for s in ['train', 'validation', 'test']}
old_test = payload['test']
payload['test'] = []
system = ('You are a crypto research assistant. Explain concepts accurately, distinguish definitions '
          'from evidence of profitable predictions, state assumptions, and acknowledge missing information. '
          'Never promise trading returns. Answer directly in at most four short sentences.')
for row in rows:
    src = sources[row['source']]
    assert row['source'] == 'DP07' and all(1 <= p <= src['pages'] for p in row['pages'])
    assert hashlib.sha256((ROOT/'Data PDF'/src['file']).read_bytes()).hexdigest() == src['sha256']
    payload[row['split']].append({'id':row['id'], 'provenance':{
        'source_id':row['source'], 'file':src['file'], 'sha256':src['sha256'], 'pdf_pages':row['pages'],
        'permission':'User attested permission for model training; independently unverified.',
        'adaptation':'Reviewed paraphrase and explicit methodological qualifications. Historical tool/UI claims omitted. Test numbers are constructed applications, not source observations.'},
        'messages':[{'role':'system','content':system}, {'role':'user','content':row['question']},
                    {'role':'assistant','content':row['answer']}]})
# Earlier tests remain evaluation-only. Their ambiguity is kept visible; no fitting on them.
payload['test'] += old_test
assert len({r['id'] for s in ('train','validation','test') for r in payload[s]}) == 64
assert not ({r['id'] for r in payload['train']} & {r['id'] for r in payload['test']})
DATA.mkdir(parents=True, exist_ok=True)
hashes = {}
for split in ('train','validation','test'):
    path = DATA/f'{split}.jsonl'
    path.write_text(''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in payload[split]), encoding='utf8')
    hashes[split] = hashlib.sha256(path.read_bytes()).hexdigest()
parent_sha = 'ed3b93060137da7d7aa1e30b1682d91a665988070e07bfe82f1e371cc7fffb76'
payload['manifest'] = {
    'model':'Qwen/Qwen3-8B', 'revision':'b968826d9c46dd6066d109eabc6255188de91218',
    'batch':'002', 'parent_kernel':'waizimran/crypto-qwen3-pdf-sft-001', 'parent_adapter_sha256':parent_sha,
    'splits':hashes, 'counts':{s:len(payload[s]) for s in hashes},
    'new_pdf':'DP07', 'prior_training_replay':24, 'new_training_examples':24,
    'scope':'Selected source-traceable concepts from five PDFs cumulatively, not full-library or full-page ingestion.',
    'evaluation':'Four new constructed applications plus four previously exposed diagnostic questions; concept overlap with training is explicit. No general accuracy inference.',
    'decision_rule':'Manual review: at least 3 of 4 new answers substantively correct, no new severe errors relative to parent on retention cases; no promotion based on loss alone. No automatic hyperparameter selection.',
    'epochs':2, 'learning_rate':0.0001, 'optimizer_restart':True,
    'ledger':[{'source_id':s['id'],'file':s['file'], 'duplicate_of':s['duplicate_of'] or ('DP19' if s['id']=='DP20' else None),
               'selected_train_examples':sum(r['provenance']['source_id']==s['id'] for r in payload['train'])}
              for s in inventory]}
payload['attribution'] = (prior/'ATTRIBUTION.txt').read_text(encoding='utf8') + '\nAdditional source: Patrick Scott (Dynamo DeFi), Introduction to On-Chain Analysis v3, DP07. User-attested training permission. Paraphrased with corrections and qualifications; no endorsement.\n'
(DATA/'manifest.json').write_text(json.dumps(payload['manifest'],indent=2),encoding='utf8')
(DATA/'ATTRIBUTION.txt').write_text(payload['attribution'],encoding='utf8')

source = (ROOT/'scripts/pdf_cloud_trainer.py').read_text(encoding='utf8')
source = source.replace('pdf_sft_001', 'pdf_sft_002')
source = source.replace('from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training',
                        'from peft import PeftModel, prepare_model_for_kbit_training')
source = source.replace('revision = model_info(model_id).sha', "revision = PAYLOAD['manifest']['revision']")
old = """        model = get_peft_model(model, LoraConfig(r=8, lora_alpha=16, lora_dropout=0.05,
            target_modules=['q_proj', 'v_proj'], task_type='CAUSAL_LM', bias='none'))"""
new = """        parents = list(Path('/kaggle/input').rglob('pdf_sft_001/adapter/adapter_model.safetensors'))
        assert len(parents) == 1, 'Expected exactly one private parent adapter'
        assert hashlib.sha256(parents[0].read_bytes()).hexdigest() == PAYLOAD['manifest']['parent_adapter_sha256']
        model = PeftModel.from_pretrained(model, parents[0].parent, is_trainable=True)
        assert any(p.requires_grad for p in model.parameters()), 'Adapter must be trainable'
        model.print_trainable_parameters()"""
assert old in source
source = source.replace(old,new).replace('num_train_epochs=1,','num_train_epochs=2,')
source = source.replace("save_strategy='no', report_to=[]", "save_strategy='steps', save_steps=10, save_total_limit=2, report_to=[]")
source = source.replace('max_new_tokens=220','max_new_tokens=384')
old_response = """response=tokenizer.decode(answer[0,inputs.input_ids.shape[1]:], skip_special_tokens=True)))"""
new_response = """response=tokenizer.decode(answer[0,inputs.input_ids.shape[1]:], skip_special_tokens=True),
                    generated_tokens=int(answer.shape[1]-inputs.input_ids.shape[1]),
                    hit_token_limit=bool(answer.shape[1]-inputs.input_ids.shape[1] >= 384)))"""
assert old_response in source
source = source.replace(old_response,new_response)
source = source.replace("'baseline_evaluation'", "'parent_adapter_evaluation'")
source = source.replace("generate('baseline_answers')", "generate('parent_answers')")
source = source.replace('PAYLOAD = None  # EMBED_PDF_PAYLOAD', 'PAYLOAD = json.loads('+repr(json.dumps(payload,ensure_ascii=False))+')')
ast.parse(source)
OUT.mkdir(parents=True,exist_ok=True)
(OUT/'train.py').write_text(source,encoding='utf8')
metadata = {'id':'waizimran/crypto-qwen3-pdf-sft-002','title':'Crypto Qwen3 PDF SFT 002',
    'code_file':'train.py','language':'python','kernel_type':'script','is_private':True,
    'enable_gpu':True,'enable_internet':True,'dataset_sources':[],'competition_sources':[],
    'kernel_sources':['waizimran/crypto-qwen3-pdf-sft-001']}
(OUT/'kernel-metadata.json').write_text(json.dumps(metadata,indent=2),encoding='utf8')
print(json.dumps({'counts':payload['manifest']['counts'],'syntax':'PASS','training_executed_locally':False}))
