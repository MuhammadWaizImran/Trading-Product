"""Post-test execution diagnostic. Does not change experiment 001 or select a model."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
from experiment import performance, bootstrap_difference

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results'/'experiment_001'
p=pd.read_csv(OUT/'test_predictions.csv',parse_dates=['entry'])
r=p.pivot(index='entry',columns='symbol',values='future_return').sort_index()

def held_portfolio(signal,cost):
    """Two independent initial 50% sleeves; no daily between-asset rebalance.

    A sleeve stays fully invested while its signal is on. Charge only on
    transitions and final liquidation. This is a diagnostic assumption, not
    a claim that actual exchange spreads equal the constant cost.
    """
    wealth=np.ones(r.shape[1])*.5
    previous=np.zeros(r.shape[1])
    series=[]
    for i,(_,returns) in enumerate(r.iterrows()):
        active=signal.iloc[i].to_numpy(dtype=float)
        buys=(active > previous)
        sells=(active < previous)
        wealth *= np.where(buys,1/(1+cost),1)
        wealth *= np.where(sells,1-cost,1)
        wealth *= 1+active*returns.to_numpy()
        if i==len(r)-1:
            wealth *= np.where(active > 0,1-cost,1)
        series.append(wealth.sum())
        previous=active
    equity=pd.Series(series,index=r.index)
    daily=equity.pct_change(fill_method=None)
    daily.iloc[0]=equity.iloc[0]-1
    return daily

result={'status':'Post-test execution sensitivity only; not used for model selection or original gate',
        'convention':'Independent 50% starting sleeves; carry consecutive positions; costs only on transitions and liquidation',
        'costs':{}}
for cost in [.0015,.003]:
    signals={name:p.pivot(index='entry',columns='symbol',values=col).sort_index()
             for name,col in [('model','active'),('trend','trend')]}
    signals['buy_hold']=pd.DataFrame(1,index=r.index,columns=r.columns)
    returns={name:held_portfolio(signal,cost) for name,signal in signals.items()}
    key=f'{cost*20000:.0f}bps_round_trip'
    result['costs'][key]={name:performance(value) for name,value in returns.items()}
    result['costs'][key]['model_vs_trend']=bootstrap_difference(returns['model'],returns['trend'])
    pd.DataFrame(returns).to_csv(OUT/f'carry_positions_{key}.csv')
(OUT/'execution_diagnostic.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
