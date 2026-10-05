#!/usr/bin/env python3
"""Credits Reel, exam-paper style (Oct 5, 2026).
A real-looking exam sheet on a dark desk: printed questions with [marks],
answers written in blue ink, the teacher's red pen circling and ticking.
No exam-board logos (IB / College Board / Cambridge rules); names in text only.
Usage: python3 exam.py stills | video | cover"""
import base64, pathlib, sys, os, json
sys.path.insert(0, '../v2'); import gen15 as g
b = lambda p: base64.b64encode(pathlib.Path(p).read_bytes()).decode()
FD = pathlib.Path('../fbcover/node_modules/@fontsource')
def face(name, pkg, ws, style='normal'):
    s = ''
    for w in ws:
        for sub, r in g.RNG.items():
            f = FD/pkg/'files'/f'{pkg}-{sub}-{w}-{style}.woff2'
            if f.exists():
                s += "@font-face{font-family:%s;font-style:%s;font-weight:%d;unicode-range:%s;src:url(data:font/woff2;base64,%s)}\n" % (name, style, w, r, b(f))
    return s
CSS = face('M', 'montserrat', (700, 800, 900)) + face('S', 'literata', (400, 600, 700)) + face('H', 'caveat', (600, 700))
s0 = open('sat.py').read()
bcss = s0[s0.index('.brand{{'):s0.index('\n', s0.index('.brand .bt small svg'))].replace('{{', '{').replace('}}', '}')
bhtml = s0[s0.index('<div class="brand">'):s0.index('</div></div>', s0.index('<div class="brand">'))+12].replace('{LG}', 'data:image/png;base64,'+b('../fbcover/logo_t.png')).replace('{{', '{').replace('}}', '}')
W, H, FPS = 1080, 1920, 30
ST = [0, 2.6, 6.2, 10.0, 14.2, 17.6, 20.6, 23.6, 26.6]; DUR = 29.6

def circ(id_, w=150, h=96):
    # a hand-drawn ellipse (red pen) around a box
    return f'<svg class="pen" id="{id_}" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><path d="M{w*.5},{h*.08} C{w*.93},{h*.02} {w*1.0},{h*.62} {w*.62},{h*.92} C{w*.22},{h*1.05} {-w*.04},{h*.62} {w*.1},{h*.3} C{w*.2},{h*.08} {w*.45},{h*.04} {w*.6},{h*.1}" pathLength="1"/></svg>'
TICK = '<svg class="pen tick" width="70" height="60" viewBox="0 0 70 60"><path d="M6 32 L26 52 L64 6" pathLength="1"/></svg>'
CROSS = '<svg class="pen tick" width="64" height="64" viewBox="0 0 64 64"><path d="M8 8 L56 56 M56 8 L8 56" pathLength="1"/></svg>'
def boxes(vals, hit):
    return '<div class="bx">' + ''.join(f'<span class="b{" hit" if v in hit else ""}">{v}{circ("c"+v.replace("*","s")) if v in hit else ""}</span>' for v in vals) + '</div>'

PAGES = [
 # 0 hook: the exam cover
 f'''<div class="top"><span>КРЕДИТ · ЖИШЭЭ ХУУДАС</span><span>30 сек</span></div>
 <div class="rule"></div>
 <div class="hook">Их сургуулийн <u class="mk">эхний</u> хичээлүүдээ <span class="red">үзэхгүй</span> байж болно</div>
 <div class="hw w1" data-t="0.9" data-d="1.0" style="font-size:80px;white-space:nowrap">Яаж? → дуустал нь үз</div>''',
 # 1
 f'''<div class="q"><b>1</b><span>Кредит гэж юу вэ?</span><i>[1]</i></div>
 <div class="hw" data-t="0.3" data-d="1.1">Их сургуульд «үзсэнд тооцогдох» хичээл.</div>
 <div class="hw" data-t="1.5" data-d="1.0">Ахлах ангидаа шалгалтаар авч болно.</div>
 <div class="tk" data-t="2.8">{TICK}</div>''',
 # 2 AP
 f'''<div class="q"><b>2</b><span>AP® шалгалт (Америк). <span style="white-space:nowrap">Оноо 1–5.</span><br>Кредит авахад ихэвчлэн хэд хэрэгтэй вэ?</span><i>[2]</i></div>
 {boxes(["1","2","3","4","5"], ["4","5"])}
 <div class="hw" data-t="1.8" data-d="0.9">Ихэвчлэн 4–5</div>
 <div class="tk" data-t="2.9">{TICK}</div>''',
 # 3 IB
 f'''<div class="q"><b>3</b><span>IB HL (гүнзгий түвшин). <span style="white-space:nowrap">Оноо 1–7.</span><br>Ихэвчлэн хэд хэрэгтэй вэ?</span><i>[2]</i></div>
 {boxes(["1","2","3","4","5","6","7"], ["5","6","7"])}
 <div class="hw" data-t="1.8" data-d="0.8">Ихэвчлэн 5–7</div>
 <div class="tk" data-t="2.4">{TICK}</div>
 <div class="note" data-t="2.7">SL (энгийн түвшин) <span class="red">ихэвчлэн тооцогдохгүй</span></div>''',
 # 4 A-Level
 f'''<div class="q"><b>4</b><span>A-Level (Британи).<br>Ихэвчлэн ямар дүн хэрэгтэй вэ?</span><i>[1]</i></div>
 {boxes(["A*","A","B","C","D","E"], ["A*","A","B"])}
 <div class="hw" data-t="1.8" data-d="0.9">B ба түүнээс дээш</div>
 <div class="tk" data-t="2.8">{TICK}</div>''',
 # 5 ЭЕШ
 f'''<div class="q"><b>5</b><span>ЭЕШ-ийн оноо кредит болох уу?</span><i>[1]</i></div>
 <div class="hw big" data-t="0.35" data-d="0.7">Ихэвчлэн үгүй</div>
 <div class="tk" data-t="1.1">{TICK}</div>
 <div class="hw" data-t="1.3" data-d="1.1">Ихэвчлэн зөвхөн олон улсын шалгалт тооцогддог.</div>''',
 # 6 why
 f'''<div class="q"><b>6</b><span>Яагаад чухал вэ?</span><i>[1]</i></div>
 <div class="hw" data-t="0.3" data-d="1.0">Эхний курсийн хичээлээ алгасаад,</div>
 <div class="hw" data-t="1.4" data-d="1.0">дараагийн шатандаа эрт орж болно.</div>
 <div class="tk" data-t="2.5">{TICK}</div>''',
 # 7 Анхаар (an exam "INFORMATION" box)
 f'''<div class="info"><div class="ih">АНХААР</div>
 <p data-t="0.3">• Албан ёсны дүн шалгалтын байгууллагаас <b>шууд</b> ирэх ёстой. Сургуулийн дүнгийн хуудас хангалтгүй.</p>
 <p data-t="1.2">• Сургууль бүрийн дүрэм <b>өөр</b>. Зорьж буй сургуулийнхаа сайтыг заавал шалга.</p></div>
 <div class="src" data-t="2.0">Эх сурвалж: future.utoronto.ca · you.ubc.ca · firstyear.mit.edu</div>''',
 # 8 end
 f'''<div class="q"><b>7</b><span>Чи аль шалгалтыг өгөх вэ?</span><i></i></div>
 <div class="hw" data-t="0.3" data-d="0.9">IB? AP? A-Level?</div>
 <div class="cta" data-t="1.2"><span class="p1">Коммент бичээрэй</span><span class="p2">Хадгалаад, найздаа илгээгээрэй</span></div>
 <div class="disc" data-t="1.2">Developed independently by Global Math Prep. Not affiliated with or endorsed by the IB, the College Board or Cambridge. AP® is a trademark registered by the College Board, which is not affiliated with, and does not endorse, this content.</div>''',
]
html = ''.join(f'<div class="pg" id="p{i}">{p}<div class="foot"><span>Global Math Prep</span><span>{i+1} / 9</span></div></div>' for i, p in enumerate(PAGES))

STYLE = f'''{CSS}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;overflow:hidden;font-family:S;background:#1f2733}}
.desk{{position:absolute;inset:0;background:radial-gradient(ellipse 90% 60% at 50% 45%,#34404f,#1a2029 80%)}}
{bcss}
.paper{{position:absolute;left:56px;right:56px;top:300px;bottom:250px;background:#fbfaf6;border-radius:6px;
 box-shadow:0 30px 60px rgba(0,0,0,.45),0 0 0 1px rgba(0,0,0,.08);overflow:hidden}}
.paper:before{{content:"";position:absolute;inset:0;background:repeating-linear-gradient(transparent 0 69px,rgba(40,90,160,.10) 69px 70px);pointer-events:none}}
.margin{{position:absolute;top:0;bottom:0;left:96px;width:2px;background:rgba(220,60,60,.35)}}
.pg{{position:absolute;inset:0;padding:70px 100px 0 130px;opacity:0}}
.top{{display:flex;justify-content:space-between;font:700 30px M;letter-spacing:2px;color:#2a2f38}}
.rule{{height:4px;background:#2a2f38;margin:18px 0 60px}}
.hook{{font:700 112px/1.12 S;color:#141820}}
.hook .red{{color:#d6332c}}
.mk{{text-decoration:none;background:linear-gradient(transparent 62%,rgba(255,196,0,.75) 62%)}}
.q{{display:grid;grid-template-columns:76px 1fr auto;gap:10px;align-items:start;font:600 64px/1.24 S;color:#141820;margin-top:30px}}
.q b{{font:800 64px S}} .q i{{font:400 48px S;font-style:normal;color:#555;padding-top:8px}}
.hw{{font:700 96px/1.18 H;color:#1f3fa6;margin-top:64px;clip-path:inset(0 100% 0 0)}}
.hw.big{{font-size:124px;color:#1f3fa6}}
.bx{{display:flex;gap:18px;margin-top:80px}}
.b{{position:relative;flex:1 1 0;max-width:140px;aspect-ratio:1;border:4px solid #141820;display:flex;align-items:center;justify-content:center;font:700 70px S;color:#141820}}
.b .pen{{position:absolute;left:-16%;top:-6%;width:132%;height:112%}}
.pen path{{fill:none;stroke:#d6332c;stroke-width:7;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:1;stroke-dashoffset:1}}
.tk{{position:relative;height:0;opacity:0}} .tk .pen{{position:absolute;left:-128px;top:-100px;width:104px;height:90px}} .tk.x{{display:inline-block;height:auto;vertical-align:middle;margin-left:30px}} .tk.x .pen{{position:static;width:150px;height:150px}}
.note{{font:600 56px/1.3 S;color:#141820;margin-top:56px;opacity:0}} .red{{color:#d6332c}}
.info{{border:4px solid #141820;padding:36px 40px;margin-top:30px}}
.ih{{font:800 46px M;letter-spacing:4px;color:#141820;margin-bottom:20px}}
.info p{{font:400 58px/1.32 S;color:#141820;margin-top:22px;opacity:0}} .info p b{{font-weight:700;background:linear-gradient(transparent 62%,rgba(255,196,0,.75) 62%)}}
.src{{font:400 34px/1.3 S;color:#555;margin-top:50px;opacity:0}}
.cta{{margin-top:90px;display:flex;flex-direction:column;align-items:flex-start;gap:24px;opacity:0}}
.cta .p1{{background:#ff9a1f;color:#111;font:900 52px M;padding:16px 38px;border-radius:999px;text-transform:uppercase}}
.cta .p2{{background:#141820;color:#fff;font:800 32px M;padding:14px 28px;border-radius:999px;white-space:nowrap}}
.disc{{position:absolute;left:130px;right:100px;bottom:200px;font:400 27px/1.35 S;color:#666;opacity:0}}
.foot{{position:absolute;left:130px;right:64px;bottom:34px;display:flex;justify-content:space-between;font:700 24px M;letter-spacing:2px;color:#9aa0a8;text-transform:uppercase}}
'''
JS = f'''
const ST={json.dumps(ST)},DUR={DUR};
const cl=x=>Math.max(0,Math.min(1,x)); const eo=x=>1-Math.pow(1-cl(x),3);
function render(t){{
 for(let i=0;i<ST.length;i++){{
  const s=ST[i], e=(i+1<ST.length?ST[i+1]:DUR+1), a=t-s, el=document.getElementById('p'+i);
  if(a<0||t>=e){{el.style.opacity=0;continue;}}
  /* page turns: the new page slides up from below, quickly */
  const inn=i==0?1:eo(a/0.28); el.style.opacity=i==0?1:cl(a/0.12); el.style.transform=`translateY(${{(1-inn)*120}}px)`;
  el.querySelectorAll('.hw').forEach(h=>{{const p=cl((a-(+h.dataset.t))/(+h.dataset.d)); h.style.clipPath=`inset(0 ${{(1-p)*100}}% 0 0)`;}});
  el.querySelectorAll('.b.hit .pen path').forEach((p,k)=>{{p.style.strokeDashoffset=1-eo((a-0.8-0.25*k)/0.35);}});
  el.querySelectorAll('.tk').forEach(x=>{{const p=a-(+x.dataset.t); x.style.opacity=p>0?1:0; x.querySelectorAll('path').forEach(q=>q.style.strokeDashoffset=1-eo(p/0.3));}});
  el.querySelectorAll('.note,.src,.cta,.disc').forEach(x=>{{const p=cl((a-(+x.dataset.t))/0.25); x.style.opacity=p; x.style.transform=`translateY(${{(1-p)*16}}px)`;}});
  el.querySelectorAll('.info p').forEach(x=>{{const p=cl((a-(+x.dataset.t))/0.25); x.style.opacity=p;}});
 }}
}}'''
page = f'<!doctype html><html><head><meta charset="utf-8"><style>{STYLE}</style></head><body><div class="desk"></div><div class="paper"><div class="margin"></div>{html}</div>{bhtml}<script>{JS}</script></body></html>'

# the grid cover (playbook: orange label + big topic title, readable in the 4:5 crop)
COVER = f'''<!doctype html><html><head><meta charset="utf-8"><style>{STYLE}
.cv{{position:absolute;inset:0;padding:70px 64px 0 130px}}
.lab{{display:inline-block;background:#ff9a1f;color:#111;font:900 44px M;letter-spacing:2px;padding:12px 32px;border-radius:999px;margin-top:40px}}
.ttl{{font:700 96px/1.08 S;color:#141820;margin-top:40px}}
.ttl .red{{color:#d6332c}}
.sub{{font:700 70px/1.2 H;color:#1f3fa6;margin-top:40px}}
</style></head><body><div class="desk"></div><div class="paper"><div class="margin"></div><div class="cv">
<div class="top"><span>КРЕДИТ · ЖИШЭЭ ХУУДАС</span><span>7 асуулт</span></div><div class="rule"></div>
<div class="lab">IB · AP® · A-LEVEL</div>
<div class="ttl">Их сургуулийн эхний курсийн хичээлийг <span class="red">алгасах</span> арга</div>
<div class="sub">Кредит гэж юу вэ?</div></div></div>{bhtml}</body></html>'''

from playwright.sync_api import sync_playwright
mode = sys.argv[1] if len(sys.argv) > 1 else 'stills'
os.makedirs('framesX', exist_ok=True)
with sync_playwright() as p:
    br = p.chromium.launch(); pg = br.new_page(viewport={'width': W, 'height': H})
    if mode == 'cover':
        pg.set_content(COVER); pg.wait_for_timeout(800); pg.screenshot(path='exam-cover.png')
    else:
        pg.set_content(page); pg.wait_for_timeout(800)
        if mode == 'stills':
            for t in (2.3, 5.9, 9.7, 13.9, 17.3, 20.3, 23.3, 26.3, 29.4):
                pg.evaluate(f'render({t})'); pg.screenshot(path=f'ex_{t}.png')
        else:
            for i in range(int(DUR*FPS)):
                pg.evaluate(f'render({i/FPS})'); pg.screenshot(path=f'framesX/f{i:04d}.png')
    br.close()
