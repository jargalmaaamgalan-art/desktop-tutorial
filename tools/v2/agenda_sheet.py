import base64, sys, glob, io
sys.argv=[sys.argv[0]]
from gen41 import F
from PIL import Image
from playwright.sync_api import sync_playwright
A='/home/claude/agenda'
def th(p):
    im=Image.open(p).convert('RGB'); im.thumbnail((300,375)); b=io.BytesIO(); im.save(b,'JPEG',quality=85)
    return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
DAYS=[('Oct13','Мя','10/13','Өнөөдөр'),('Oct14','Лх','10/14',''),('Oct15','Пү','10/15',''),('Oct16','Ба','10/16',''),('Oct17','Бя','10/17',''),
('Oct18','Ня','10/18',''),('Oct19','Да','10/19',''),('Oct20','Мя','10/20',''),('Oct21','Лх','10/21',''),('Oct22','Пү','10/22','')]
SLOTS={1:('03:00','14:00'),2:('06:00','17:00'),3:('09:00','20:00')}
def posts(d):
    fs=sorted(glob.glob(f'{A}/{d}-*-01-of-*.png'))
    words=[f for f in fs if 'SATWords' in f]; other=[f for f in fs if 'SATWords' not in f]
    order=['SUPPORT','ADDRESS','FIGURE','CHARGE','MAINTAIN','TRACE','ACCOUNT','HOLD']
    words.sort(key=lambda f:[i for i,w in enumerate(order) if w in f][0])
    if words: return list(zip([1,2,3],words+other))
    return [(3,o) for o in other]
NAME={'ACCOUNT':'ACCOUNT','HOLD':'HOLD','SUPPORT':'SUPPORT','ADDRESS':'ADDRESS','FIGURE':'FIGURE','CHARGE':'CHARGE','MAINTAIN':'MAINTAIN','TRACE':'TRACE',
'Conjunction':'FANBOYS жагсаалт','Cacao':'Corn ancestor','Twin':'Twin choices','Redding':'Twigs in a river','Middle':'However (дунд)','Meanwhile':'Meanwhile','Neanderthal':'Strong or weak','As-Such':'As such','State-Taxes':'Taxes & moving','In-Fact':'In fact / That is'}
def nm(f): return next(v for k,v in NAME.items() if k in f)
rows=''
for d,wd,dt,tag in DAYS:
    cards=''.join(f'<div class="c"><img src="{th(f)}"><div class="t"><b>{SLOTS[s][0]}</b> Канад · <b>{SLOTS[s][1]}</b> УБ</div><div class="n">{nm(f)}</div></div>' for s,f in posts(d))
    rows+=f'<div class="r{" now" if tag else ""}"><div class="d"><div class="wd">{wd}</div><div class="dt">{dt}</div>{f"<div class=tg>{tag}</div>" if tag else ""}</div><div class="cs">{cards}</div></div>'
HTML=f'''<!doctype html><html><head><meta charset="utf-8"><style>{F('IN','inter',[400,600,800])}
*{{box-sizing:border-box;margin:0}}body{{width:1180px;background:#f3f7f8;font-family:IN,sans-serif;color:#0B3C49;padding:40px}}
h1{{font-size:44px;font-weight:800}}.sub{{font-size:20px;color:#55707c;margin:8px 0 28px}}
.r{{display:flex;gap:22px;background:#fff;border-radius:22px;padding:20px;margin-bottom:16px;box-shadow:0 2px 8px rgba(11,60,73,.07)}}
.r.now{{outline:4px solid #FFAD1F}}
.d{{width:110px;flex:none;text-align:center;padding-top:10px}}.wd{{font-size:40px;font-weight:800}}.dt{{font-size:20px;color:#55707c;font-weight:600}}
.tg{{margin-top:10px;background:#FFAD1F;color:#0B3C49;font-weight:800;font-size:14px;padding:6px 8px;border-radius:20px}}
.cs{{display:flex;gap:18px}}.c{{width:300px}}.c img{{width:300px;border-radius:12px;display:block;border:1px solid #e1eaed}}
.t{{font-size:16px;margin-top:10px;color:#55707c}}.t b{{color:#0B3C49;font-size:18px}}.n{{font-size:19px;font-weight:800;margin-top:2px}}
</style></head><body><h1>Постын хуваарь · 10/13 - 10/22</h1><div class="sub">Facebook + Instagram. Цаг: Канад (Атлантик) · Улаанбаатар</div>{rows}</body></html>'''
open('/home/claude/preview/agenda.html','w').write(HTML)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1180,'height':1000}); pg.goto('file:///home/claude/preview/agenda.html'); pg.wait_for_timeout(300)
    pg.screenshot(path='/home/claude/preview/agenda.png',full_page=True); b.close()
print('ok')
