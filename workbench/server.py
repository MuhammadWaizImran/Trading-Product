"""Run with python -m workbench.server. Binds only to localhost; no cloud calls."""
import argparse
from decimal import Decimal
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from urllib.parse import urlparse, parse_qs
from workbench.core import ROOT, Library, load_candles, snapshot
from workbench.answers import answer_request
from scripts.research_math import position_size, payoff, orderbook_imbalance


def create_handler(root=ROOT):
    library = Library(root)
    assets = load_candles(root/'data/candles.csv')
    web = root/'workbench/web'

    class Handler(BaseHTTPRequestHandler):
        def reply(self, value, status=200, mime='application/json; charset=utf-8'):
            data = value if isinstance(value, bytes) else json.dumps(value, default=str, allow_nan=False).encode()
            self.send_response(status)
            self.send_header('Content-Type',mime)
            self.send_header('Content-Length',str(len(data)))
            self.send_header('Cache-Control','no-store')
            self.send_header('X-Content-Type-Options','nosniff')
            self.send_header('Content-Security-Policy',"default-src 'self'; script-src 'self'; style-src 'self'; object-src 'none'; frame-ancestors 'none'")
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self):
            # Reject DNS-rebinding hostnames; no credential, filesystem-write or order APIs.
            host = self.headers.get('Host','').split(':')[0]
            if host not in ('localhost','127.0.0.1'):
                return self.reply({'error':'Localhost access only'},403)
            u = urlparse(self.path)
            q = {k:v[0] for k,v in parse_qs(u.query).items()}
            try:
                if u.path in ('/','/workbench','/app.js','/answers.js','/style.css','/chat.css','/chat.js','/orb.js','/visuals.js','/intro-controller.js','/assets/mountains.jpg'):
                    name = 'chat.html' if u.path=='/' else ('index.html' if u.path=='/workbench' else u.path[1:])
                    mime = {'html':'text/html; charset=utf-8','js':'text/javascript; charset=utf-8','css':'text/css; charset=utf-8','jpg':'image/jpeg'}[name.rsplit('.',1)[-1]]
                    return self.reply((web/name).read_bytes(),mime=mime)
                if u.path=='/api/status':
                    return self.reply({'stage':'Part 2: evaluation', 'ready':False,'training_location':'Kaggle only',
                        'library_examples':len(library.rows),'library_sources':len(library.sources),
                        'models':'Qwen3-8B adapters have not demonstrated reliable improvement.',
                        'assets':[{'symbol':k,'first':v[0]['date'],'last':v[-1]['date']} for k,v in sorted(assets.items())],
                        'sources':[{'id':sid,'file':path.name} for sid,path in sorted(library.sources.items())],
                        'next':'Source scope and exact price rules integrated; model-generated answers remain unapproved.',
                        'scope':'Private offline evaluation. No live agents or orders.'})
                if u.path=='/api/search':
                    return self.reply({'results':library.search(q.get('q','')),'method':'Keyword search of reviewed adaptations; not a generated answer.'})
                if u.path=='/api/snapshot':
                    return self.reply(snapshot(assets,q.get('symbol',''),q.get('through','')))
                if u.path=='/api/answer':
                    return self.reply(answer_request(library,q))
                if u.path=='/api/calculate':
                    kind=q.get('kind')
                    if kind=='position': value=position_size(q['account'],q['risk'],q.get('stop'),q.get('entry'))
                    elif kind=='payoff': value=payoff(q['win'],q['loss'],q.get('probability'),q.get('cost',0))
                    elif kind=='imbalance': value=orderbook_imbalance(q['ask'],q['bid'],q['convention'])
                    else: raise ValueError('Unknown calculator')
                    return self.reply(value)
                if u.path.startswith('/source/'):
                    source=library.sources.get(u.path.rsplit('/',1)[-1])
                    if source is not None: return self.reply(source.read_bytes(),mime='application/pdf')
                if u.path=='/api/reports':
                    names=['PDF_SOURCE_SCOPE_007_RESULTS.md','PDF_SFT_009_RESULTS.md','PDF_SFT_008_RESULTS.md','CURRENT_PROGRESS.md']
                    return self.reply([{'name':n,'text':(root/'research'/n).read_text(encoding='utf8')} for n in names])
                self.reply({'error':'Not found'},404)
            except (ValueError,KeyError,ArithmeticError) as error:
                self.reply({'error':str(error)},400)

        def log_message(self, *_):
            pass

    return Handler


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--port',type=int,default=8765)
    args=parser.parse_args()
    server=ThreadingHTTPServer(('127.0.0.1',args.port),create_handler())
    print(f'Private evaluation workbench: http://127.0.0.1:{args.port}',flush=True)
    server.serve_forever()


if __name__=='__main__': main()
