xx""Inventory user-provided PDFs for private critical review, never training."""
import hashlib,json,re
from pathlib import Path
import fitz

root=Path(__file__).resolve().parents[1]
out=root/'tmp/pdfs/data_pdf_review'
out.mkdir(parents=True,exist_ok=True)
records=[]
seen={}
for number,p in enumerate(sorted((root/'Data PDF').glob('*.pdf')),1):
    sha=hashlib.sha256(p.read_bytes()).hexdigest()
    ident=f'DP{number:02d}'
    record=dict(id=ident,file=p.name,sha256=sha,duplicate_of=seen.get(sha))
    if sha in seen:
        ref=next(r for r in records if r['id']==seen[sha])
        record.update(pages=ref['pages'],words=ref['words'],text_hash=ref['text_hash'])
    else:
        seen[sha]=ident
        doc=fitz.open(p)
        pages=[]
        for i,page in enumerate(doc):
            content=page.get_text(sort=True)
            pages.append(dict(page=i+1,text=content,words=len(content.split()),images=len(page.get_images())))
        folder=out/ident
        folder.mkdir(exist_ok=True)
        (folder/'pages.json').write_text(json.dumps(pages,ensure_ascii=False),encoding='utf-8')
        combined='\n'.join(x['text'] for x in pages)
        (folder/'text.txt').write_text('\n\n'.join(f'=== PDF PAGE {x["page"]} ===\n{x["text"]}' for x in pages),encoding='utf-8')
        record.update(pages=len(doc),words=sum(x['words'] for x in pages),image_only_pages=[x['page'] for x in pages if not x['text'].strip()],sparse_pages=[x['page'] for x in pages if x['words']<35],metadata=doc.metadata,toc=doc.get_toc(),text_hash=hashlib.sha256(re.sub(r'\s+',' ',combined).encode()).hexdigest())
    records.append(record)
    print(ident,p.name,record['pages'],record['words'],'duplicate',record['duplicate_of'],flush=True)
(out/'inventory.json').write_text(json.dumps(records,indent=2,ensure_ascii=False),encoding='utf-8')
print('TOTAL',sum(x['pages'] for x in records),'UNIQUE PAGES',sum(x['pages'] for x in records if not x['duplicate_of']),flush=True)
