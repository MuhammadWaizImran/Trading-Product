"""Construct and validate a private PDF-derived SFT batch. Never fits a model."""
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'data/pdf_sft_batch_001'
SYSTEM = ('You are a crypto research assistant. Explain concepts accurately, distinguish '
          'definitions from evidence of profitable predictions, state assumptions, and '
          'acknowledge missing information. Never promise trading returns.')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    inventory = json.loads((ROOT/'tmp/pdfs/data_pdf_review/inventory.json').read_text(encoding='utf-8'))
    sources = {r['id']: r for r in inventory}
    examples_path = ROOT/'research/pdf_training_examples.json'
    rows = json.loads(examples_path.read_text(encoding='utf-8'))
    assert len({r['id'] for r in rows}) == len(rows)
    assert len({r['question'].casefold() for r in rows}) == len(rows)
    assert len({r['answer'].casefold() for r in rows}) == len(rows)
    assert Counter(r['split'] for r in rows) == {'train': 24, 'validation': 4, 'test': 4}
    assert set(r['source'] for r in rows) == {'DP05', 'DP06', 'DP17', 'DP19'}
    reviewed = {'DP05': {8, 11, 12, 13, 14}, 'DP06': {4, 5, 6, 7, 8},
                'DP17': {31, 32, 35, 36, 37, 38, 54}, 'DP19': {1, 2, 9, 10, 13, 26}}
    OUT.mkdir(parents=True, exist_ok=True)
    split_rows = {s: [] for s in ('train', 'validation', 'test')}
    for row in rows:
        source = sources[row['source']]
        assert not source['duplicate_of']
        assert set(row['pages']) <= reviewed[row['source']]
        path = ROOT/'Data PDF'/source['file']
        assert digest(path) == source['sha256'], 'Source has changed since review'
        permission = ('CC BY 4.0; copyright 2025 Martin Angerer, Marius Gramlich and Michael Hanke; '
                      'https://doi.org/10.3390/jrfm18030124; '
                      'https://creativecommons.org/licenses/by/4.0/; paraphrased and clarified; no endorsement'
                      if row['source'] == 'DP19' else
                      'User attested permission for model training in conversation; independently unverified.')
        provenance = dict(source_id=row['source'], file=source['file'], sha256=source['sha256'],
                          pdf_pages=row['pages'], permission=permission, adaptation=row['adaptation'])
        split_rows[row['split']].append(dict(
            id=row['id'], provenance=provenance,
            messages=[{'role': 'system', 'content': SYSTEM},
                      {'role': 'user', 'content': row['question']},
                      {'role': 'assistant', 'content': row['answer']}]))
    for split, records in split_rows.items():
        (OUT/f'{split}.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in records), encoding='utf-8')
    ledger = []
    for source in inventory:
        selected = [r for r in rows if r['source'] == source['id']]
        duplicate = source['duplicate_of'] or ('DP19' if source['id'] == 'DP20' else None)
        ledger.append(dict(source_id=source['id'], file=source['file'], sha256=source['sha256'],
                           duplicate_of=duplicate, selected_examples=len(selected),
                           selected_pages=sorted({p for r in selected for p in r['pages']}),
                           status='selected_passages_only' if selected else
                                  'duplicate_excluded' if duplicate else 'pending_content_preparation',
                           permission='user_attestation_recorded; preserve any existing license conditions'))
    manifest = dict(name='pdf_sft_batch_001', model='Qwen/Qwen3-8B',
                    scope='Small first PDF-derived batch. Not all documents/pages or a comprehensive curriculum.',
                    counts={s: len(v) for s, v in split_rows.items()},
                    examples_sha256=digest(examples_path),
                    splits={s: digest(OUT/f'{s}.jsonl') for s in split_rows},
                    split_limitation='Same educational sources/concepts occur across splits; this evaluates held-out applications, not source-independent generalization.',
                    training_executed=False, source_ledger=ledger)
    (OUT/'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    (OUT/'ATTRIBUTION.txt').write_text(
        'Private PDF-derived educational examples. Answers are adaptations, not verbatim source text.\n'
        'Crypto for Beginners: Technical Analysis Course — Crypto Wealth Academy.\n'
        'Risk Management — Elisa Crypto.\n'
        'Cryptocurrency Trading ebook — Binance Academy.\n'
        'Order Book Liquidity on Crypto Exchanges — Martin Angerer, Marius Gramlich and Michael Hanke, 2025.\n'
        'https://doi.org/10.3390/jrfm18030124 ; CC BY 4.0 https://creativecommons.org/licenses/by/4.0/\n'
        'Questions and answers paraphrase selected concepts and add qualifications listed per example.\n'
        'No author endorsement is implied. Underlying CryptoTick data are not included.\n', encoding='utf-8')
    print(json.dumps({'checks': 'PASS', 'output': str(OUT), 'counts': manifest['counts'],
                      'source_documents': 4, 'training_executed': False}))


if __name__ == '__main__':
    main()
