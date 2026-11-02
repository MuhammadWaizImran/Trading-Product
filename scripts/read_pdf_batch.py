"""Display complete page text or render pages for the review; no fitting."""
import argparse,json
from pathlib import Path
import fitz
from PIL import Image,ImageDraw
ap=argparse.ArgumentParser();ap.add_argument('id');ap.add_argument('start',type=int);ap.add_argument('end',type=int);ap.add_argument('--render',action='store_true');args=ap.parse_args()
root=Path(__file__).resolve().parents[1];base=root/'tmp/pdfs/data_pdf_review'
record=next(r for r in json.loads((base/'inventory.json').read_text(encoding='utf8')) if r['id']==args.id)
folder=base/(record['duplicate_of'] or args.id)
if not args.render:
    pages=json.loads((folder/'pages.json').read_text(encoding='utf8'))
    for page in pages[args.start-1:args.end]:
        cleaned='\n'.join(line.strip() for line in page['text'].splitlines() if line.strip())
        print(f'\n=== {args.id} PDF PAGE {page["page"]} ===\n{cleaned}')
else:
    d=fitz.open(root/'Data PDF'/record['file'])
    for i in range(args.start-1,min(args.end,len(d))):
        pix=d[i].get_pixmap(matrix=fitz.Matrix(1.6,1.6),alpha=False)
        pix.save(str(folder/f'page_{i+1:03d}.png'))
    print('Rendered',args.id,args.start,args.end)
