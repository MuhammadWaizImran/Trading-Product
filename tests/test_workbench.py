import json
from decimal import Decimal
import tempfile
from pathlib import Path
import threading
import unittest
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from urllib.parse import urlencode
from http.server import ThreadingHTTPServer
from workbench.core import ROOT, Library, load_candles, snapshot
from workbench.server import create_handler


class DataChecks(unittest.TestCase):
    def test_future_rows_cannot_affect_snapshot(self):
        a=load_candles(ROOT/'data/candles.csv')
        symbol=next(iter(a)); cutoff=a[symbol][100]['date']
        before=snapshot(a,symbol,cutoff)
        for row in a[symbol][101:]: row['close']*=100
        self.assertEqual(before,snapshot(a,symbol,cutoff))

    def test_unsupported_asset_abstains(self):
        with self.assertRaises(ValueError): snapshot({},'UNKNOWN','2020-01-01')

    def test_bad_candles_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'x.csv'
            for line in ['TEST,2020-01-01,10,1,8,10,1','TEST,2020-01-01,NaN,12,8,10,1']:
                p.write_text('symbol,date,open,high,low,close,volume\n'+line+'\n')
                with self.assertRaises(ValueError): load_candles(p)
            line='TEST,2020-01-01,10,12,8,10,1\n'
            p.write_text('symbol,date,open,high,low,close,volume\n'+line+line)
            with self.assertRaises(ValueError): load_candles(p)

    def test_gap_hides_change_metrics(self):
        rows=[{'date':f'2020-01-{i:02d}','open':10,'high':12,'low':8,'close':10,'volume':1} for i in range(1,25) if i!=10]
        r=snapshot({'TEST':rows},'TEST','2020-01-24')
        self.assertEqual(r['gaps_in_chart'],1)
        self.assertIsNone(r['mean20'])
        self.assertIsNone(r['change7_pct'])

    def test_library_links_only_verified_sources(self):
        library=Library()
        rows=library.search('risk budget position notional')
        self.assertTrue(rows)
        self.assertTrue(all(r['pages'] and r['source'] in library.sources for r in rows))
        self.assertEqual(library.search('qzxwvnonexistent'),[])


class HttpChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=ThreadingHTTPServer(('127.0.0.1',0),create_handler())
        cls.url=f'http://127.0.0.1:{cls.server.server_port}'
        cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown();cls.server.server_close();cls.thread.join()

    def test_local_api_end_to_end(self):
        with urlopen(self.url+'/api/calculate?kind=position&account=12000&risk=.005&stop=.03') as r:
            d=json.load(r)
            self.assertEqual(Decimal(d['notional']),Decimal(2000))
            self.assertEqual(Decimal(d['risk_budget']),Decimal(60))
        with urlopen(self.url+'/') as r:
            self.assertIn(b'chat-form',r.read())
        with urlopen(self.url+'/workbench') as r:
            self.assertIn(b'Evidence before conviction',r.read())
        with urlopen(self.url+'/api/status') as r:
            self.assertFalse(json.load(r)['ready'])

    def test_arbitrary_paths_and_bad_hosts_rejected(self):
        for path in ['/../../AGENTS.md','/source/AGENTS.md','/api/place-order']:
            with self.assertRaises(HTTPError) as ctx: urlopen(self.url+path)
            self.assertEqual(ctx.exception.code,404)
        with self.assertRaises(HTTPError) as ctx: urlopen(Request(self.url+'/',headers={'Host':'untrusted.example'}))
        self.assertEqual(ctx.exception.code,403)

    def test_missing_stop_and_zero_total(self):
        with urlopen(self.url+'/api/calculate?kind=position&account=5000&risk=.01&entry=20') as r:
            self.assertEqual(json.load(r)['status'],'insufficient_information')
        with self.assertRaises(HTTPError) as ctx: urlopen(self.url+'/api/calculate?kind=imbalance&ask=0&bid=0&convention=ask_minus_bid')
        self.assertEqual(ctx.exception.code,400)

    def answer(self, **params):
        with urlopen(self.url+'/api/answer?'+urlencode(params)) as r: return json.load(r)

    def test_unknown_source_never_guessed(self):
        r=self.answer(question='What denominator does an unnamed paper use for spread?')
        self.assertEqual(r['status'],'needs_source')
        self.assertFalse(r['model_invoked'])
        self.assertEqual(r['evidence'],[])

    def test_unknown_document_cannot_bypass_using_general_scope_or_dropdown(self):
        questions=['An unnamed report uses spread. Is its denominator midpoint?',
                   'I have not identified the article. Does its VWAP average resting levels?',
                   'Someone mentioned a survey without its title. Was its sample 1000?']
        for question in questions:
            for options in [{'scope':'general'},{'source_id':'DP19'}]:
                r=self.answer(question=question,**options)
                self.assertEqual(r['status'],'needs_source')
                self.assertEqual(r['evidence'],[])
                self.assertFalse(r['model_invoked'])

    def test_source_selection_and_general_evidence(self):
        r=self.answer(question='spread price',source_id='DP19')
        self.assertTrue(r['evidence'])
        self.assertTrue(all(e['source']=='DP19' for e in r['evidence']))
        r=self.answer(question='candlestick',scope='general')
        self.assertTrue(r['evidence'])
        self.assertFalse(r['model_invoked'])

    def test_hypothetical_limit_answer_end_to_end(self):
        sell=self.answer(kind='limit',side='sell',limit='240',fill='235')
        buy=self.answer(kind='limit',side='buy',limit='240',fill='235')
        self.assertFalse(sell['calculation']['price_constraint_satisfied'])
        self.assertTrue(buy['calculation']['price_constraint_satisfied'])
        self.assertIn('at or above 240',sell['answer'])
        self.assertFalse(sell['calculation']['execution_guaranteed'])
        self.assertEqual(sell['evidence'][0]['id'],'limit-order')

    def test_no_evidence_or_invalid_source_cannot_fallback(self):
        self.assertEqual(self.answer(question='qzxwvnonexistent',source_id='DP19')['status'],'needs_evidence')
        with self.assertRaises(HTTPError): self.answer(question='spread',source_id='DP99')
        with self.assertRaises(HTTPError): self.answer(question='spread',scope='general',source_id='DP19')


if __name__=='__main__': unittest.main()
