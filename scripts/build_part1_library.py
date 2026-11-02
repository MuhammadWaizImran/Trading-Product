"""Build the Part 1 research catalogue; never trains or fits a model."""
import csv, json, hashlib
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'research' / 'part1_library'
OUT.mkdir(parents=True, exist_ok=True)
DATE = '2026-09-20'
with (ROOT/'research/SOURCE_REGISTER.csv').open(encoding='utf-8-sig') as f:
    rows = [r for r in csv.DictReader(f) if r['id'][0] in 'ED']
for r in rows:
    r['review_depth'] = 'Prior source and rights review; not exhaustive full-text analysis'

def add(i, title, author, url, coverage, limitation, version='Living resource; date not established', rights='Free reading verified; no indexing or training license established', rights_url=None, depth='Official page or selected sections reviewed'):
    rows.append(dict(id=i,title=title,publisher_authors=author,publication_version=version,url=url,rights_url=rights_url or url,coverage=coverage,cost_access='Free official reading; see limitations',rights_assessment=rights,proposed_use='Human research and source-linked notes; ingestion held unless license cleared',evidence_quality='Primary educational source; not proof of trading profitability',limitations=limitation,checked_at_utc=DATE,review_depth=depth))

add('R01','Bitcoin and Cryptocurrency Technologies','Narayanan; Bonneau; Felten; Miller; Goldfeder','https://bitcoinbook.cs.princeton.edu/','Consensus; cryptography; mining; privacy; security','Free prepublication draft differs from published edition','2016')
add('R02','Mastering Ethereum, second edition','Antonopoulos; Wood; Parisi; Mazza; Pozzolini','https://github.com/ethereumbook/ethereumbook','Ethereum architecture; contracts; security','Edition publication date and license transition must be resolved','Second edition; mutable repository','Repository specifies CC BY-NC-ND for first 12 months then CC BY-SA; transition not established')
add('R03','Forecasting: Principles and Practice, third edition','Hyndman; Athanasopoulos','https://otexts.com/fpp3/','Uncertainty; temporal evaluation; forecasting baselines','General forecasting; no cryptocurrency edge established','2021; site updated 2026-09-16')
add('R04','OpenIntro Statistics','Diez; Cetinkaya-Rundel; Barr','https://www.openintro.org/book/os/','Sampling; uncertainty; inference; regression','Free PDF with optional donation; restricted teacher resources excluded','Fourth edition','Open textbook; specific downloaded edition license verification pending')
add('R05','Bitcoin: A Peer-to-Peer Electronic Cash System','Satoshi Nakamoto','https://bitcoin.org/bitcoin.pdf','Original Bitcoin mechanism','Historical design, not investment valuation','2008')
add('R06','Varsity Technical Analysis, 22 chapters','Zerodha; Karthik Rangappa','https://zerodha.com/varsity/module/technical-analysis/','Candles; patterns; trends; volume; indicators; checklist','Equity teaching examples must not be treated as crypto validation',rights='All rights reserved; reproduction prohibited. Reading only',rights_url='https://zerodha.com/terms-and-conditions')
add('R07','Technical Indicator Guide','Fidelity','https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide','Indicator reference','Dynamic guide did not expose every entry; individual entries not all reviewed',depth='Landing page reviewed')
add('R08','Getting Started with Technical Analysis','Fidelity; Charles D. Kirkpatrick II','https://www.fidelity.com/bin-public/060_www_fidelity_com/documents/learning-center/Getting-Started-Tech-Analysis.pdf','Chart construction; trends; support and resistance','42-page slide deck; not a crypto study')
add('R09','Understanding Indicators and Oscillators','Fidelity','https://www.fidelity.com/bin-public/060_www_fidelity_com/documents/learning-center/Understanding-Indicators-TA.pdf','Trend; momentum; volume indicators','43-page teaching deck; parameter sensitivity matters')
add('R10','ChartSchool','StockCharts','https://chartschool.stockcharts.com/','Chart patterns; indicators; technical vocabulary','Chart examples are copyrighted; no bulk collection',rights='Reading only; scraping and commercial copying restricted',rights_url='https://help.stockcharts.com/learning-more/policies-and-limitations/terms-of-service')
add('R11','Chart Patterns catalogue','Thomas N. Bulkowski','https://www.thepatternsite.com/chartpatterns.html','Pattern definitions; failure statistics; pattern taxonomy','Primarily historical stock studies; statistics cannot transfer directly to crypto',rights_url='https://www.thepatternsite.com/Copyright.html',depth='Catalogue discovered and selected pages reviewed; intermittent access failures')
add('R12','Technical Analysis: Modern Perspectives','Gordon Scott; Michael Carr; Mark Cremonie / CFA Institute','https://rpc.cfainstitute.org/research/foundation/2017/technical-analysis','Technical analysis research and interpretation','Review of methods; not independent validation of our product','2016 page date; 2017 publication URL')
add('R13','TA-Lib function list and implementation','TA-Lib contributors','https://ta-lib.org/functions/','Reproducible indicators and candlestick recognizers','Pattern detection is not predictive validation; pin version and defaults',rights='BSD source license; retain notices and check asset exceptions',rights_url='https://github.com/TA-Lib/ta-lib/blob/main/LICENSE')
add('R14','What Is Technical Analysis?','Binance Academy','https://www.binance.com/en/academy/articles/what-is-technical-analysis','Technical analysis assumptions and limitations','Exchange education has commercial incentives')
add('R15','A Beginner\'s Guide to Classical Chart Patterns','Binance Academy','https://www.binance.com/en/academy/articles/a-beginners-guide-to-classical-chart-patterns','Continuation; reversal; bilateral patterns','Pattern interpretation is conditional; examples are not performance evidence','Updated 2026-08-12')
add('R16','7 Common Mistakes in Technical Analysis','Binance Academy','https://www.binance.com/en/academy/articles/7-common-mistakes-in-technical-analysis-ta','Risk; overtrading; uncertainty','General education; no success rate established')
add('R17','Risk/Reward Ratio','Binance Academy','https://www.binance.com/en/academy/articles/what-is-the-risk-reward-ratio-and-how-to-use-it','Conditional payoff and loss planning','Ratio alone does not establish positive expected returns')
add('R18','Candlestick Charts and Patterns course lesson','Binance Academy','https://www.binance.com/en/academy/courses/track/intermediate-track/crypto-trading-deep-dive/candlestick-charts-and-patterns','Candlestick structure and interpretation','Course lesson, not a licensed chart dataset',depth='Course page discovered; no full video-content review')
add('R19','Crypto trading chart patterns','Kraken Learn','https://www.kraken.com/learn/crypto-trading-chart-patterns','Crypto chart-pattern terminology','Exchange educational material; require failed examples')
add('R20','Crypto technical indicators','Kraken Learn','https://www.kraken.com/learn/crypto-technical-indicators','Crypto indicator concepts','Correlated indicators do not create independent confirmation')
add('R21','Candlestick chart patterns','Kraken Learn','https://www.kraken.com/learn/candlestick-chart-patterns','Candlestick educational reference','Discovery-level review; copyrighted diagrams',depth='Official search result verified; full page review pending')
add('R22','Repainting','TradingView Pine Script documentation','https://www.tradingview.com/pine-script-docs/concepts/repainting/','Historical/live differences; future leakage; confirmation','Platform-specific behavior must be reproduced carefully')
add('R23','Foundations of Technical Analysis','Andrew W. Lo; Harry Mamaysky; Jiang Wang / NBER','https://www.nber.org/papers/w7613','Pattern formalization; statistical inference','US stock historical sample, not crypto evidence','2000 working paper')
add('R24','Technical trading and cryptocurrencies','Robert Hudson; Andrew Urquhart','https://doi.org/10.1007/s10479-019-03357-1','Large technical-rule study in crypto','Repository full text encountered bot challenge; abstract findings not independently replicated','2019 online; 2021 journal',depth='Publisher/repository metadata and abstract; full text pending')
add('R25','Decentralized Finance: On Blockchain- and Smart Contract-Based Financial Markets','Fabian Schar / Federal Reserve Bank of St. Louis','https://files.stlouisfed.org/files/htdocs/publications/review/2021/04/15/decentralized-finance-on-blockchain-and-smart-contract-based-financial-markets.pdf','DeFi architecture; composability; smart-contract risks','Historical overview; government hosting does not establish third-party public domain','2021')
add('R26','The crypto ecosystem: key elements and risks','Bank for International Settlements','https://www.bis.org/publications/crypto-ecosystem-key-elements-and-risks','Concentration; fragmentation; structural risk','Institutional perspective; distinguish evidence from policy judgments','2023')
add('R27','Maximal extractable value','Ethereum.org contributors','https://ethereum.org/developers/docs/mev/','Transaction ordering; sandwiching; execution risk','Protocol source; empirical costs require venue-specific measurement',rights='Ethereum.org CC BY 4.0 default; check exceptions',rights_url='https://ethereum.org/terms-of-use/')
add('R28','Downloadable CSV data overview and samples','Tardis.dev','https://docs.tardis.dev/downloadable-csv-files/overview','Order-book and trades sample availability','Free samples cover first day of month; incomplete history; paid full archive',rights='Free sample access; commercial reuse rights not established')
add('R29','Coin Metrics metric documentation','Coin Metrics','https://docs.coinmetrics.io/getting-started','Metric definitions and interpretation','Documentation rights and data rights are separate')
add('R30','Free crypto and blockchain research','Kaiko','https://www.kaiko.com/products/instantly-access-kaiko-crypto-and-blockchain-research-for-free','Liquidity; market structure; institutional research','Some content requires signup; not a free full historical dataset',depth='Offering page reviewed')

fields=list(rows[0])
with (OUT/'RESOURCE_CATALOG.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
(OUT/'RESOURCE_CATALOG.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False),encoding='utf-8')
md=['# Part 1 resource catalogue',f'Checked {DATE}. {len(rows)} educational/data entries, including restricted and held candidates. Not {len(rows)} training-approved sources. Model and cloud references remain in the older register.','Review depth and rights are recorded separately. A course counts once, not once per chapter.']
for r in rows:
    md += [f"\n## {r['id']} — [{r['title']}]({r['url']})",f"**Author/publisher:** {r['publisher_authors']}. **Version:** {r['publication_version']}.",f"**Coverage:** {r['coverage']}. **Access:** {r['cost_access']}.",f"**Use/rights:** {r['rights_assessment']}. [Rights reference]({r['rights_url']}).",f"**Limitations:** {r['limitations']}. **Review depth:** {r['review_depth']}."]
(OUT/'RESOURCE_CATALOG.md').write_text('\n\n'.join(md),encoding='utf-8')

pdfs=[
('R01','princeton_bitcoin_book.pdf','https://d28rh4a8wq0iu5.cloudfront.net/bitcointech/readings/princeton_bitcoin_book.pdf'),
('R08','fidelity_getting_started.pdf','https://www.fidelity.com/bin-public/060_www_fidelity_com/documents/learning-center/Getting-Started-Tech-Analysis.pdf'),
('R09','fidelity_indicators.pdf','https://www.fidelity.com/bin-public/060_www_fidelity_com/documents/learning-center/Understanding-Indicators-TA.pdf'),
('R12','cfa_technical_analysis.pdf','https://rpc.cfainstitute.org/sites/default/files/-/media/documents/book/rf-publication/2017/rf-v2017-n1-full.pdf'),
('R23','lo_technical_analysis.pdf','https://www.nber.org/system/files/working_papers/w7613/w7613.pdf'),
('R25','schar_defi.pdf','https://files.stlouisfed.org/files/htdocs/publications/review/2021/04/15/decentralized-finance-on-blockchain-and-smart-contract-based-financial-markets.pdf'),
('E13','backtest_overfitting.pdf','https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf'),
('R05','bitcoin_whitepaper.pdf','https://bitcoin.org/bitcoin.pdf')]
reading=OUT/'reading_only';reading.mkdir(exist_ok=True)
def download(item):
    i,name,url=item
    rec=dict(source_id=i,url=url,file='reading_only/'+name,checked=DATE,use='Private human reading only; not a training or retrieval corpus')
    try:
        p=reading/name
        if p.exists(): data=p.read_bytes()
        else:
            r=requests.get(url,timeout=60);r.raise_for_status();data=r.content
            if not data.startswith(b'%PDF-'): raise ValueError('Response is not a PDF; no access-control workaround attempted')
            p.write_bytes(data)
        rec.update(status='downloaded',bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
    except Exception as e: rec.update(status='failed',error=str(e))
    return rec
with ThreadPoolExecutor(max_workers=4) as pool: manifest=list(pool.map(download,pdfs))
(OUT/'DOWNLOAD_MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps({'catalogue_entries':len(rows),'downloaded':sum(r['status']=='downloaded' for r in manifest),'manifest':manifest},indent=2))
