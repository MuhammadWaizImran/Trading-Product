import sys
import unittest
from pathlib import Path
import numpy as np
import pandas as pd
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from experiment import features, FEATURES, audit, net_returns, performance

def sample():
    n=150
    c=np.arange(n,dtype=float)+100
    return pd.DataFrame(dict(date=pd.date_range('2020-01-01',periods=n),open=c,high=c+2,
                            low=c-2,close=c+1,volume=np.ones(n)*100,symbol='BTCUSDT'))

class Checks(unittest.TestCase):
    def test_future_candles_do_not_change_features(self):
        a=sample(); b=a.copy()
        b.loc[101:,'close']*=4
        pd.testing.assert_frame_equal(features(a).loc[:100,FEATURES],features(b).loc[:100,FEATURES])
    def test_prefix_features_match(self):
        a=sample()
        pd.testing.assert_frame_equal(features(a).loc[:100,FEATURES],features(a.iloc[:101]).loc[:,FEATURES])
    def test_execution_delay_and_label(self):
        f=features(sample())
        self.assertEqual(f.entry.iloc[80],f.date.iloc[82])
        self.assertEqual(f.exit.iloc[80],f.date.iloc[83])
        self.assertAlmostEqual(f.future_return.iloc[80],183/182-1)
    def test_missing_day_fails(self):
        with self.assertRaises(ValueError): audit(sample().drop(index=80))
    def test_impossible_ohlc_fails(self):
        f=sample(); f.loc[80,'high']=1
        with self.assertRaises(ValueError): audit(f)
    def test_flat_roundtrip_loses_cost_cash_does_not(self):
        f=pd.DataFrame(dict(future_return=[0.,0.]))
        r=net_returns(f,[1,0],.0015)
        self.assertLess(r[0],0); self.assertEqual(r[1],0)
        self.assertAlmostEqual(r[0],.9985/1.0015-1)
    def test_drawdown_includes_initial_loss(self):
        self.assertAlmostEqual(performance([-.2,.1])['max_drawdown'],.2)

if __name__=='__main__': unittest.main()
