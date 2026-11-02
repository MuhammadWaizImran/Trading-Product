"""Prepare source-attribution contrast training; never execute a model locally."""
import ast
from collections import Counter
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def main():
    prior=ROOT/'data/pdf_sft_batch_008'
    data=ROOT/'data/pdf_sft_batch_009'; out=ROOT/'notebooks/pdf_sft_009'
    assert not data.exists() and not out.exists(), 'Do not overwrite a frozen experiment'
    manifest=json.loads((prior/'manifest.json').read_text())
    payload={}
    for split in ('train','validation','test'):
        raw=(prior/f'{split}.jsonl').read_bytes()
        assert hashlib.sha256(raw).hexdigest()==manifest['splits'][split]
        payload[split]=[json.loads(s) for s in raw.decode().splitlines()]
    byid={r['id']:r for r in payload['train']}
    def evidence(rid):
        row=byid[rid]
        q=row['messages'][1]['content']
        records=json.loads(q.split('Supplied evidence (reviewed PDF adaptations):\n')[1])
        return next(r for r in records if r['id']==rid)
    def add(split,rid,suffix,question,answer,context_ids):
        row=deepcopy(byid[rid]); row['id']='r009-'+suffix
        row['messages'][1]['content']=question+'\n\nSupplied evidence (reviewed PDF adaptations):\n'+json.dumps([evidence(c) for c in context_ids])
        row['messages'][2]['content']=answer
        row['evidence_ids']=context_ids
        row['provenance']['adaptation']+=' Constructed reviewed development exercise; not a source quotation. Evidence IDs: '+', '.join(context_ids)+'.'
        payload[split].append(row)
    cases=[
      ('relative-spread','Which denominator is used for relative spread?',
       'The reviewed passage uses the midpoint, (best ask + best bid) / 2, as the denominator. [relative-spread]'),
      ('book-vwap','Does the average use resting orders or executed trades?',
       'The reviewed passage averages selected resting order-book levels using their quantities; it is distinct from a trade-volume average over time. [book-vwap]'),
      ('dp03-conjoint-design','Which money characteristics did the study vary?',
       'The reviewed study varied issuer/backer, seller acceptability, transaction cost, monthly inflation/deflation and digital versus physical form. [dp03-conjoint-design]'),
      ('dp04-reserve-chart-date','What is the final year of the reserves chart?',
       'The chart discussed in this reviewed passage ends in 2014. That does not establish current reserve composition. [dp04-reserve-chart-date]'),
      ('dp07-links','Do transfers by themselves establish common wallet ownership?',
       'No. Transfers establish observed links; payments, services, custody or common ownership can explain them. Common ownership requires additional attribution evidence. [dp07-links]'),
      ('dp16-signature-roles','Does signature verification alone prove the signer has legal ownership?',
       'No. Verification checks a signature against a message and verification key. It does not by itself establish legal identity or entitlement. [dp16-signature-roles]')]
    for rid,q,a in cases:
        add('train',rid,'identified-'+rid,'For the supplied passage ['+rid+'] specifically: '+q,a,[rid])
        add('train',rid,'unspecified-'+rid,'In a document I have not named or supplied: '+q,
            'The document is unidentified. Please provide its title or relevant passage. The retrieved material is not established to be that document, so I cannot attribute its details to the source you mean.',[rid])
        distractor='dp01-hot-cold' if rid!='dp16-signature-roles' else 'relative-spread'
        add('train',rid,'irrelevant-'+rid,'Using only the supplied passage, answer: '+q,
            'The supplied passage does not support that answer. Please supply the relevant definition or evidence; I cannot cite an unrelated passage as justification.',[distractor])
    # Fixed development applications, never used as training targets or retrieval records.
    tests=[
      ('relative-spread','unknown-normalization','An unnamed report uses a relative-spread measure. Is its denominator definitely the midpoint?',
       'No. Identify the report or supply its equation. The retrieved midpoint convention cannot be assigned to an unidentified report.', ['relative-spread']),
      ('book-vwap','unknown-average','I have not identified the article. Does its VWAP definitely average resting order-book levels?',
       'No. The article or its definition is needed; the retrieved resting-order definition may belong to a different source.', ['book-vwap']),
      ('dp03-conjoint-design','unknown-survey','Someone mentioned a survey without its title. Can you establish that it sampled exactly 1000 people per country?',
       'No. The unspecified survey cannot be identified from a retrieved study alone; request its identity or methods.', ['dp03-conjoint-design']),
      ('dp04-reserve-chart-date','known-chart','For the supplied dp04-reserve-chart-date passage, what year ends the historical series?',
       'It ends in 2014. [dp04-reserve-chart-date]', ['dp04-reserve-chart-date']),
      ('dp07-links','ownership-evidence','Wallet X pays wallet Y for a service. Is that transfer alone proof that Y owns all other addresses belonging to X?',
       'No. A transfer can reflect a payment or service; common ownership needs additional evidence. [dp07-links]', ['dp07-links','dp07-seed-price']),
      ('dp16-signature-roles','signature-title','A person produces a valid signature using a stolen key. Does validity alone prove lawful ownership?',
       'No. Key-based signature validity does not establish lawful ownership or legal identity. [dp16-signature-roles]', ['dp16-signature-roles']),
      ('limit-order','sell-direction','A sell limit is 240. Does the price rule permit an execution at 235, and does it guarantee any execution?',
       'No. The selling price must be 240 or higher under the limit constraint, and execution is not guaranteed. [limit-order]', ['limit-order']),
      ('dp05-pattern-evidence','missing-study','A tutorial shows eight winners only. Which missing evidence prevents treating 8/8 as a general strategy success rate?',
       'A defined sampling procedure including failures, reproducible rules, costs and out-of-sample evaluation is missing. Selected successes do not establish a general success rate. [dp05-pattern-evidence]', ['dp05-pattern-evidence'])]
    for rid,suffix,q,a,ctx in tests: add('test',rid,suffix,q,a,ctx)
    texts={s:''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows) for s,rows in payload.items()}
    payload['attribution']=(prior/'ATTRIBUTION.txt').read_text(encoding='utf8')+'\nRun009: source-attribution contrasts use previously reviewed page-traceable adaptations. No additional PDF or redistribution rights claimed.\n'
    m=deepcopy(manifest)
    m.update(batch='009',created_utc=datetime.now(timezone.utc).isoformat(),epochs=1,
        counts={s:len(payload[s]) for s in texts},splits={s:hashlib.sha256(t.encode()).hexdigest() for s,t in texts.items()},
        previous_training_data_sha256=manifest['splits']['train'],
        training_sources=dict(Counter(r['provenance']['source_id'] for r in payload['train'])),
        method='Fresh rank-8 QLoRA; same settings as008; adds18 matched/unknown/irrelevant-source contrast examples.',
        scope='230 training records from selected material in ten PDFs; no new whole-document coverage.',
        evaluation='36 carried-forward development cases plus8 fixed application contrasts with manually selected training evidence. All exposed/concept-overlapping; not independent acceptance or a retrieval benchmark.',
        decision_rule='Require correct source abstention on all3 new unidentified-source checks, correct identified-source answers on other5 new checks, no severe attribution/risk errors on old checks, and clear improvement over identically prompted base. Loss alone cannot promote. If source-identity errors persist, change the answering pipeline before further SFT, rather than automatic repeated fitting.')
    payload['manifest']=m
    source=(ROOT/'notebooks/pdf_sft_008/train.py').read_text(encoding='utf8')
    node=next(n for n in ast.parse(source).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PAYLOAD' for t in n.targets))
    lines=source.splitlines(keepends=True); lines[node.lineno-1:node.end_lineno]=['PAYLOAD = json.loads('+repr(json.dumps(payload,ensure_ascii=False))+')\n']
    source=''.join(lines).replace('pdf_sft_008','pdf_sft_009'); ast.parse(source)
    data.mkdir(); out.mkdir()
    for s,t in texts.items(): (data/f'{s}.jsonl').write_bytes(t.encode())
    (data/'manifest.json').write_text(json.dumps(m,indent=2),encoding='utf8')
    (data/'ATTRIBUTION.txt').write_text(payload['attribution'],encoding='utf8')
    (out/'train.py').write_text(source,encoding='utf8')
    metadata=json.loads((ROOT/'notebooks/pdf_sft_008/kernel-metadata.json').read_text()); metadata.update(id='waizimran/crypto-qwen3-pdf-sft-009',title='Crypto Qwen3 PDF SFT 009')
    (out/'kernel-metadata.json').write_text(json.dumps(metadata,indent=2))
    print(json.dumps(m,indent=2))

if __name__=='__main__': main()
