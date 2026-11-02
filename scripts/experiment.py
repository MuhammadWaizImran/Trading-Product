"""Experiment 001: private, daily spot research. No order or account APIs."""
import argparse
import calendar
import concurrent.futures
import hashlib
import io
import json
import os
from pathlib import Path
import platform
import time
import zipfile
from datetime import datetime, timezone

os.environ.setdefault('OMP_NUM_THREADS', '2')
os.environ.setdefault('OPENBLAS_NUM_THREADS', '2')
import numpy as np
import pandas as pd
import requests
import sklearn
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import brier_score_loss, log_loss, accuracy_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from threadpoolctl import threadpool_limits

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
OUT = ROOT / 'results' / 'experiment_001'
SYMBOLS = ['BTCUSDT', 'ETHUSDT']
COLS = ['timestamp','open','high','low','close','volume','close_time','quote_volume',
        'trades','taker_base','taker_quote','ignore']
FEATURES = ['r1','r3','r7','r14','r30','vol7','vol30','gap20','gap60',
            'range','body','volume_ratio','drawdown30','asset_eth']

def utcnow():
    return datetime.now(timezone.utc).isoformat()

def digest(b):
    return hashlib.sha256(b).hexdigest()

def require_cloud_training():
    """Fail closed outside recognized hosted runtimes; no local override."""
    linux = platform.system() == 'Linux'
    kaggle = linux and bool(os.environ.get('KAGGLE_KERNEL_RUN_TYPE')) and Path('/kaggle/working').is_dir()
    colab = linux and bool(os.environ.get('COLAB_RELEASE_TAG')) and Path('/content').is_dir()
    if kaggle:
        return 'Kaggle CPU'
    if colab:
        return 'Colab CPU'
    raise RuntimeError('Cloud-only training policy: run in a hosted Kaggle or Colab runtime. Laptop training is disabled.')

def fetch_month(task):
    symbol, year, month = task
    name = f'{symbol}-1d-{year}-{month:02d}.zip'
    url = f'https://data.binance.vision/data/spot/monthly/klines/{symbol}/1d/{name}'
    path = DATA / 'raw' / name
    meta_path = path.with_suffix('.json')
    if path.exists() and meta_path.exists():
        meta = json.loads(meta_path.read_text())
        if digest(path.read_bytes()) == meta['sha256'] == meta['provider_sha256']:
            return meta
        raise ValueError(f'Cached archive checksum mismatch: {name}')
    for attempt in range(3):
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            check = requests.get(url + '.CHECKSUM', timeout=30)
            check.raise_for_status()
            expected = check.text.split()[0].lower()
            actual = digest(r.content)
            if actual != expected:
                raise ValueError(f'Provider checksum mismatch: {name}')
            meta = dict(symbol=symbol, year=year, month=month, url=url,
                        retrieved_at=utcnow(), sha256=actual, provider_sha256=expected,
                        bytes=len(r.content), parser_version='1',
                        use='private backtesting only; redistribution not cleared')
            path.write_bytes(r.content)
            meta_path.write_text(json.dumps(meta, indent=2), encoding='utf-8')
            return meta
        except requests.RequestException:
            if attempt == 2:
                raise
            time.sleep(1 + attempt)

def parse_archive(path):
    with zipfile.ZipFile(path) as z:
        files = [n for n in z.namelist() if n.endswith('.csv')]
        if len(files) != 1:
            raise ValueError(f'Unexpected archive contents: {path}')
        frame = pd.read_csv(io.BytesIO(z.read(files[0])), names=COLS)
    raw = pd.to_numeric(frame.timestamp, errors='raise')
    # Preserve integer precision, independently normalize every observation.
    millis = raw.where(raw < 10**14, raw // 1000)
    frame['date'] = pd.to_datetime(millis, unit='ms', utc=True).dt.tz_localize(None)
    for col in COLS[1:]:
        frame[col] = pd.to_numeric(frame[col], errors='raise')
    return frame

def audit(frame):
    if frame.date.duplicated().any() or not frame.date.is_monotonic_increasing:
        raise ValueError('Dates duplicated or unsorted')
    if not (frame.date.diff().dropna() == pd.Timedelta(days=1)).all():
        raise ValueError('Missing daily candles')
    if not (frame.date == frame.date.dt.normalize()).all():
        raise ValueError('Non-midnight daily candle')
    prices = frame[['open','high','low','close']]
    if not np.isfinite(prices.to_numpy()).all() or (prices <= 0).any().any():
        raise ValueError('Invalid prices')
    if (frame.high < prices.max(axis=1)).any() or (frame.low > prices.min(axis=1)).any():
        raise ValueError('Impossible OHLC')
    if not np.isfinite(frame.volume).all() or (frame.volume < 0).any():
        raise ValueError('Invalid volume')

def prepare():
    (DATA / 'raw').mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    tasks = [(s,y,m) for s in SYMBOLS for y in range(2018,2026) for m in range(1,13)]
    records = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for i, meta in enumerate(pool.map(fetch_month, tasks), 1):
            records.append(meta)
            if i % 24 == 0:
                print(f'Verified archives: {i}/{len(tasks)}', flush=True)
    frames = []
    for symbol in SYMBOLS:
        parts = []
        for s, y, m in tasks:
            if s != symbol:
                continue
            f = parse_archive(DATA / 'raw' / f'{s}-1d-{y}-{m:02d}.zip')
            if len(f) != calendar.monthrange(y,m)[1] or not ((f.date.dt.year == y) & (f.date.dt.month == m)).all():
                raise ValueError('Archive month coverage mismatch')
            parts.append(f)
        frame = pd.concat(parts, ignore_index=True).sort_values('date')
        audit(frame)
        frame['symbol'] = symbol
        frames.append(frame)
    pd.concat(frames, ignore_index=True).to_csv(DATA / 'candles.csv', index=False)
    manifest = dict(created_at=utcnow(), archives=records,
                    candles_sha256=digest((DATA/'candles.csv').read_bytes()),
                    rows=sum(map(len, frames)),
                    rights_evidence=['https://github.com/binance/binance-public-data',
                    'https://www.binance.com/en/blog/futures/421499824684901131'])
    (OUT/'data_manifest.json').write_text(json.dumps(manifest, indent=2))
    print(f'Data audit passed: {manifest["rows"]} candles', flush=True)

def features(f):
    f = f.sort_values('date').copy()
    for n in [1,3,7,14,30]:
        f[f'r{n}'] = f.close.pct_change(n, fill_method=None)
    for n in [7,30]:
        f[f'vol{n}'] = f.r1.rolling(n).std()
    for n in [20,60]:
        f[f'gap{n}'] = f.close / f.close.rolling(n).mean() - 1
    f['range'] = (f.high-f.low)/f.close
    f['body'] = f.close/f.open-1
    f['volume_ratio'] = f.volume/f.volume.rolling(30).mean().replace(0,np.nan)
    f['drawdown30'] = f.close/f.close.rolling(30).max()-1
    f['asset_eth'] = (f.symbol == 'ETHUSDT').astype(int)
    f['entry'] = f.date.shift(-2)
    f['exit'] = f.date.shift(-3)
    f['future_return'] = f.open.shift(-3)/f.open.shift(-2)-1
    f['up'] = (f.future_return > 0).astype(int)
    f['trend'] = (f.close.rolling(20).mean() > f.close.rolling(60).mean()).astype(int)
    return f

def new_models():
    return dict(logistic=make_pipeline(StandardScaler(), LogisticRegression(C=1,max_iter=1000,random_state=42)),
                histogram=HistGradientBoostingClassifier(max_iter=100,max_leaf_nodes=7,
                    learning_rate=0.05,l2_regularization=1,min_samples_leaf=40,
                    early_stopping=False,random_state=42))

def score(y,p):
    return dict(brier=float(brier_score_loss(y,p)), log_loss=float(log_loss(y,p,labels=[0,1])),
                accuracy=float(accuracy_score(y,p >= .5)), n=len(y))

def performance(r):
    r = np.asarray(r, dtype=float)
    equity = np.r_[1.,np.cumprod(1+r)]
    dd = equity/np.maximum.accumulate(equity)-1
    return dict(net_return=float(equity[-1]-1), max_drawdown=float(-dd.min()),
                daily_sharpe=float(np.mean(r)/np.std(r,ddof=1)*np.sqrt(365)) if len(r)>1 and np.std(r)>0 else 0.,
                days=len(r))

def net_returns(frame, active, cost):
    # Costs on each leg: buy at marked-up entry and sell at marked-down exit.
    return np.asarray(active) * ((1+frame.future_return.to_numpy())*(1-cost)/(1+cost)-1)

def bootstrap_difference(a,b):
    d=np.asarray(a)-np.asarray(b)
    rng=np.random.default_rng(42)
    means=[]
    for _ in range(2000):
        starts=rng.integers(0,len(d),size=int(np.ceil(len(d)/14)))
        idx=np.concatenate([(s+np.arange(14)) % len(d) for s in starts])[:len(d)]
        means.append(d[idx].mean())
    return dict(mean_daily_excess=float(d.mean()),ci95=list(map(float,np.quantile(means,[.025,.975]))),
                method='paired circular 14-day blocks; 2000 replicates; both assets grouped by date')

def evaluate():
    environment = require_cloud_training()
    started=time.perf_counter()
    manifest=json.loads((OUT/'data_manifest.json').read_text())
    if digest((DATA/'candles.csv').read_bytes()) != manifest['candles_sha256']:
        raise ValueError('Processed data changed since manifest')
    raw=pd.read_csv(DATA/'candles.csv',parse_dates=['date'])
    frame=pd.concat([features(g) for _,g in raw.groupby('symbol')],ignore_index=True)
    frame=frame.replace([np.inf,-np.inf],np.nan).dropna(subset=FEATURES+['future_return','entry','exit'])
    validation=[]
    with threadpool_limits(limits=2):
        for year in [2022,2023]:
            boundary=pd.Timestamp(f'{year}-01-01')
            train=frame[frame.exit < boundary]
            valid=frame[(frame.entry >= boundary)&(frame.exit < pd.Timestamp(f'{year+1}-01-01'))]
            for name,model in new_models().items():
                model.fit(train[FEATURES],train.up)
                p=model.predict_proba(valid[FEATURES])[:,1]
                validation.append(dict(year=year,model=name,**score(valid.up,p)))
        v=pd.DataFrame(validation)
        means=v.groupby('model').brier.mean()
        selected='logistic' if means['logistic'] <= means['histogram'] else 'histogram'
        train=frame[frame.exit < pd.Timestamp('2024-01-01')]
        test=frame[(frame.entry >= pd.Timestamp('2024-01-01')) & (frame.exit < pd.Timestamp('2026-01-01'))].copy()
        model=new_models()[selected]
        model.fit(train[FEATURES],train.up)
        test['probability']=model.predict_proba(test[FEATURES])[:,1]
    test['active']=(test.probability >= .55).astype(int)
    test['regime']=np.where(test.trend == 1,'bull_trend','bear_trend')
    prevalence=float(train.up.mean())
    result=dict(experiment='001',executed_at=utcnow(),execution_environment=environment,
                platform=platform.platform(),python=platform.python_version(),
                versions=dict(numpy=np.__version__,pandas=pd.__version__,sklearn=sklearn.__version__),
                features=FEATURES,selected_model=selected,validation=validation,
                test_prediction=score(test.up,test.probability),
                prevalence_baseline=score(test.up,np.full(len(test),prevalence)),
                training_rows=len(train),test_rows=len(test),
                first_entry=str(test.entry.min()),last_exit=str(test.exit.max()),
                active_asset_days=int(test.active.sum()),exposure=float(test.active.mean()),
                costs={},by_asset={},by_year={},by_regime={})
    daily_all=None
    for cost in [.0015,.003]:
        key=f'{cost*20000:.0f}bps_round_trip'
        daily={}
        for name,active in [('model',test.active),('trend',test.trend),('cash',np.zeros(len(test)))]:
            test[f'{name}_net']=net_returns(test,active,cost)
            # Each daily sleeve is 50% of total equity, cash for inactive sleeve.
            daily[name]=test.groupby('entry')[f'{name}_net'].mean().sort_index()
        matrix=test.pivot(index='entry',columns='symbol',values='future_return').sort_index()
        if matrix.isna().any().any() or matrix.shape[1] != 2:
            raise ValueError('Unequal test coverage')
        wealth=(1+matrix).cumprod()/(1+cost)
        wealth.iloc[-1] *= (1-cost)
        portfolio=wealth.mean(axis=1)
        daily['buy_hold']=portfolio.pct_change(fill_method=None)
        daily['buy_hold'].iloc[0]=portfolio.iloc[0]-1
        result['costs'][key]={name:performance(r) for name,r in daily.items()}
        result['costs'][key]['model_vs_trend']=bootstrap_difference(daily['model'],daily['trend'])
        if cost == .0015:
            daily_all=pd.DataFrame(daily)
            for symbol,g in test.groupby('symbol'):
                result['by_asset'][symbol]=dict(**performance(g.model_net),active_asset_days=int(g.active.sum()))
            for year,g in daily_all.groupby(daily_all.index.year):
                result['by_year'][str(year)]={name:performance(g[name]) for name in daily_all.columns}
            for regime,g in test.groupby('regime'):
                result['by_regime'][regime]=dict(n=len(g),active_asset_days=int(g.active.sum()),
                    mean_net_return=float(g.model_net.mean()),prediction=score(g.up,g.probability))
            test.to_csv(OUT/'test_predictions.csv',index=False)
    base=result['costs']['30bps_round_trip']
    gates=dict(brier_improves=result['test_prediction']['brier'] < result['prevalence_baseline']['brier'],
               positive_net=base['model']['net_return'] > 0,
               positive_stress=result['costs']['60bps_round_trip']['model']['net_return'] > 0,
               excess_ci_positive=base['model_vs_trend']['ci95'][0] > 0,
               sufficient_trades=result['active_asset_days'] >=100,
               both_years_nonnegative=all(x['model']['net_return']>=0 for x in result['by_year'].values()),
               drawdown_limit=base['model']['max_drawdown'] <= .25)
    result['gates']=gates
    result['numerical_gate']='PASS' if all(gates.values()) else 'FAIL'
    result['part3_gate']='NOT_READY: discovery, liquidity and explanation evaluation remain unproven'
    result['wall_seconds']=time.perf_counter()-started
    result['code_sha256']=digest(Path(__file__).read_bytes())
    result['protocol_sha256']=digest((ROOT/'research'/'EVALUATION_PROTOCOL.md').read_bytes())
    result['candles_sha256']=manifest['candles_sha256']
    (OUT/'metrics.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    daily_all.to_csv(OUT/'daily_portfolio_returns.csv')
    import joblib
    joblib.dump(model,OUT/'numerical_model.joblib')
    print(json.dumps(result,indent=2),flush=True)

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('action',choices=['prepare','evaluate','all'])
    args=parser.parse_args()
    if args.action in ['evaluate','all']:
        require_cloud_training()
    if args.action in ['prepare','all']:
        prepare()
    if args.action in ['evaluate','all']:
        evaluate()
