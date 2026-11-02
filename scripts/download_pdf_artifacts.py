"""Download final cloud artifacts with retries; deliberately skip optimizer checkpoints."""
import argparse, json, re
from pathlib import Path
import requests
from kaggle.api.kaggle_api_extended import KaggleApi
ROOT=Path(__file__).resolve().parents[1]

def main():
    p=argparse.ArgumentParser();p.add_argument('--batch',required=True);p.add_argument('--dest',type=Path,required=True);a=p.parse_args()
    assert re.fullmatch(r'\d{3}',a.batch)
    root=a.dest.resolve();assert ROOT in root.parents
    root.mkdir(parents=True,exist_ok=True)
    api=KaggleApi();api.authenticate()
    response=api.process_response(api.kernel_output_with_http_info('waizimran',f'crypto-qwen3-pdf-sft-{a.batch}'))
    records=[]
    for item in response['files']:
        name=item['fileName']
        if not name.startswith(f'pdf_sft_{a.batch}/') or '/checkpoints/' in name:continue
        target=(root/name).resolve();assert root in target.parents
        target.parent.mkdir(parents=True,exist_ok=True)
        for attempt in range(3):
            try:
                result=requests.get(item['url'],timeout=60);result.raise_for_status()
                partial=target.with_suffix(target.suffix+'.partial');partial.write_bytes(result.content);partial.replace(target)
                records.append(dict(file=name,bytes=target.stat().st_size));print(name,flush=True);break
            except Exception:
                if attempt==2:raise
    (root/'download_manifest.json').write_text(json.dumps(dict(files=records,optimizer_checkpoints_included=False),indent=2))
if __name__=='__main__':main()
