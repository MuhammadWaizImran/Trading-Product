"""Read-only public Binance snapshot and deterministic indicators; no orders or fitting."""
import json, urllib.request, urllib.parse, argparse
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor

BASE = 'https://fapi.binance.com'
OUT = Path(__file__).resolve().parents[1] / 'research/market_review_2026_09_24'

def fetch(path, **params):
    url = BASE + path + ('?' + urllib.parse.urlencode(params) if params else '')
    req = urllib.request.Request(url, headers={'User-Agent': 'PrivateResearch/1.0'})
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.load(r)

def ema(xs, n):
    v = sum(xs[:n])/n
    for x in xs[n:]: v += 2/(n+1)*(x-v)
    return v

def indicators(rows, now):
    rows = [r for r in rows if r[6] < now]
    c = [float(r[4]) for r in rows]
    h = [float(r[2]) for r in rows]; l = [float(r[3]) for r in rows]
    v = [float(r[5]) for r in rows]
    changes = [b-a for a,b in zip(c,c[1:])]
    gain = sum(max(x,0) for x in changes[:14])/14
    loss = sum(max(-x,0) for x in changes[:14])/14
    for x in changes[14:]:
        gain = (gain*13+max(x,0))/14; loss = (loss*13+max(-x,0))/14
    tr = [max(h[i]-l[i],abs(h[i]-c[i-1]),abs(l[i]-c[i-1])) for i in range(1,len(c))]
    atr = sum(tr[:14])/14
    for x in tr[14:]: atr = (atr*13+x)/14
    return dict(count=len(rows),last_close=c[-1],last_close_utc=datetime.fromtimestamp(rows[-1][6]/1000,timezone.utc).isoformat(),
                ema20=ema(c,20),ema50=ema(c,50),ema200=ema(c,200),rsi14=100-100/(1+gain/loss) if loss else 100,
                atr14=atr,high20=max(h[-20:]),low20=min(l[-20:]),previous_high20=max(h[-21:-1]),
                previous_low20=min(l[-21:-1]),volume_ratio=v[-1]/(sum(v[-21:-1])/20),last6=rows[-6:])

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--symbols',nargs='+',default=['BTCUSDT','ETHUSDT','SOLUSDT'])
    parser.add_argument('--label',default='market_review_2026_09_24')
    args=parser.parse_args()
    if not args.label.replace('_','').isalnum(): raise ValueError('Invalid output label')
    symbols=args.symbols
    if not all(s.isalnum() and s.endswith('USDT') for s in symbols): raise ValueError('Invalid symbols')
    out=OUT.parent/args.label
    out.mkdir(exist_ok=True)
    tasks = {'time':('/fapi/v1/time',{}),'exchange':('/fapi/v1/exchangeInfo',{})}
    for symbol in symbols:
        for key,path in [('ticker','ticker/24hr'),('premium','premiumIndex'),('book','ticker/bookTicker'),('oi','openInterest')]:
            tasks[symbol+'_'+key] = ('/fapi/v1/'+path,dict(symbol=symbol))
        for interval in ['1h','4h','1d']:
            tasks[symbol+'_'+interval] = ('/fapi/v1/klines',dict(symbol=symbol,interval=interval,limit=250))
    def run(item):
        key,(path,params)=item
        try: return key,fetch(path,**params)
        except Exception as e: return key,{'error':str(e)}
    with ThreadPoolExecutor(max_workers=4) as pool: raw = dict(pool.map(run,tasks.items()))
    raw['retrieved_at_utc']=datetime.now(timezone.utc).isoformat()
    (out/'public_snapshot.json').write_text(json.dumps(raw,indent=2),encoding='utf8')
    now=raw['time'].get('serverTime')
    summary={'retrieved_at_utc':raw['retrieved_at_utc'],'server_time':raw['time']}
    for symbol in symbols:
        s={k:raw[symbol+'_'+k] for k in ['ticker','premium','book','oi']}
        s['filters']=next((x['filters'] for x in raw['exchange'].get('symbols',[]) if x['symbol']==symbol),[])
        for interval in ['1h','4h','1d']:
            rows=raw[symbol+'_'+interval]
            s[interval]=indicators(rows,now) if isinstance(rows,list) and now and len(rows)>201 else {'insufficient_history': True, 'rows':len(rows) if isinstance(rows,list) else rows}
        summary[symbol]=s
    (out/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf8')
    print('Saved public snapshot and indicators:',out)

if __name__=='__main__': main()
