"""Read-only document extraction and rendered review aids; no model training."""
from pathlib import Path
import fitz
from PIL import Image, ImageDraw
root=Path(__file__).resolve().parents[1]
out=root/'tmp/pdfs/upload_review'
out.mkdir(parents=True,exist_ok=True)
for f in root.glob('*.pdf'):
    doc=fitz.open(f)
    folder=out/f.stem
    folder.mkdir(exist_ok=True)
    text='\n\n'.join(f'=== PDF PAGE {i+1} ===\n'+p.get_text() for i,p in enumerate(doc))
    (folder/'text.txt').write_text(text,encoding='utf-8')
    for start in range(0,len(doc),12):
        sheet=Image.new('RGB',(1200,4*450),'#cccccc')
        draw=ImageDraw.Draw(sheet)
        for k in range(start,min(start+12,len(doc))):
            page=doc[k];pix=page.get_pixmap(matrix=fitz.Matrix(1,1),alpha=False)
            im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
            im.thumbnail((390,420))
            x=((k-start)%3)*400;y=((k-start)//3)*450
            sheet.paste(im,(x,y+25));draw.text((x+5,y+5),f'PDF page {k+1}',fill='black')
        sheet.save(folder/f'sheet_{start+1:03d}.jpg')
    print(f.name,len(doc),'pages;',len(text),'characters;',folder)
