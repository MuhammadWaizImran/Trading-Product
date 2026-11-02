import csv
from datetime import date, timedelta
import hashlib
import json
import math
from pathlib import Path
import re
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]


def tokens(text):
    return set(re.findall(r'[a-z0-9]+', text.lower())) - {'the','a','an','is','of','to','and','in','what','how','does','for','can','it'}


class Library:
    def __init__(self, root=ROOT):
        self.root = root
        self.rows = []
        self.sources = {}
        path = root/'data/pdf_sft_batch_006/train.jsonl'
        checked = {}
        for line in path.read_text(encoding='utf8').splitlines():
            row = json.loads(line)
            p = row['provenance']
            source = (root/'Data PDF'/p['file']).resolve()
            if source.parent != (root/'Data PDF').resolve():
                raise ValueError('Source path outside PDF directory')
            if source not in checked:
                checked[source] = hashlib.sha256(source.read_bytes()).hexdigest()
            if checked[source] != p['sha256']:
                raise ValueError('PDF hash differs from reviewed source: '+p['source_id'])
            self.sources[p['source_id']] = source
            item = {'id': row['id'], 'question': row['messages'][-2]['content'],
                    'answer': row['messages'][-1]['content'], 'source': p['source_id'],
                    'file': p['file'], 'pages': p['pdf_pages'], 'permission': p['permission'],
                    'adaptation': p['adaptation'], 'sha256': p['sha256']}
            item['_tokens'] = tokens(item['question']+' '+item['answer'])
            self.rows.append(item)
        self.frequency = Counter(t for row in self.rows for t in row['_tokens'])

    def search(self, query, source_id=None):
        terms = tokens(query[:500])
        scored = []
        for row in self.rows:
            if source_id is not None and row['source'] != source_id:
                continue
            overlap = terms & row['_tokens']
            if not overlap:
                continue
            score = sum(math.log(1 + len(self.rows)/self.frequency[t]) for t in sorted(overlap))
            scored.append((score, row))
        scored.sort(key=lambda x: (-x[0], x[1]['id']))
        return [{k:v for k,v in row.items() if k != '_tokens'} for _,row in scored[:6]]


def load_candles(path):
    assets = {}
    seen = set()
    with Path(path).open(encoding='utf8', newline='') as stream:
        for raw in csv.DictReader(stream):
            symbol = raw['symbol']
            if not re.fullmatch(r'[A-Za-z0-9_.:-]{1,40}', symbol):
                raise ValueError('Invalid asset identifier')
            day = date.fromisoformat(raw['date'][:10])
            key = (symbol, day)
            if key in seen:
                raise ValueError('Duplicate asset/date')
            seen.add(key)
            row = {k:float(raw[k]) for k in ('open','high','low','close','volume')}
            if not all(math.isfinite(v) for v in row.values()):
                raise ValueError('Nonfinite candle value')
            if min(row[k] for k in ('open','high','low','close')) <= 0 or row['volume'] < 0:
                raise ValueError('Invalid candle price/volume')
            if row['high'] < max(row['open'],row['close'],row['low']) or row['low'] > min(row['open'],row['close']):
                raise ValueError('Impossible OHLC values')
            row['date'] = day.isoformat()
            assets.setdefault(symbol, []).append(row)
    for rows in assets.values():
        rows.sort(key=lambda r:r['date'])
    return assets


def snapshot(assets, symbol, through):
    cutoff = date.fromisoformat(through)
    if symbol not in assets:
        raise ValueError('Asset is absent from the local dataset')
    # All calculations operate on the selected prefix; later rows cannot affect them.
    rows = [r for r in assets[symbol] if date.fromisoformat(r['date']) <= cutoff]
    if not rows:
        raise ValueError('No observations on or before the selected date')
    recent = rows[-90:]
    last = recent[-1]
    gaps = sum((date.fromisoformat(b['date'])-date.fromisoformat(a['date'])).days != 1 for a,b in zip(recent,recent[1:]))
    ma = sum(r['close'] for r in rows[-20:])/20 if len(rows)>=20 and not gaps else None
    change = (rows[-1]['close']/rows[-8]['close']-1)*100 if len(rows)>=8 and not gaps else None
    trend = 'insufficient data' if ma is None else 'above 20-day average' if last['close']>ma else 'below 20-day average' if last['close']<ma else 'at 20-day average'
    return {'symbol':symbol,'through':through,'last_observation':last['date'],
            'observation_count':len(rows),'candles':recent,'close':last['close'],
            'mean20':ma,'change7_pct':change,'description':trend,'gaps_in_chart':gaps,
            'days_missing_to_cutoff':(cutoff-date.fromisoformat(last['date'])).days,
            'decision':'WAIT — historical evaluation only',
            'limitations':['No validated predictive model.', 'No current news, fundamentals or order-book evidence.',
                           'Price relative to an average describes past data; it does not establish a profitable forecast.'],
            'time_basis':'Daily candles through the end of the selected UTC day.'}
