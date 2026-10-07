#!/usr/bin/env python3
"""Campus-style Reel (Oct 7, 2026): real campus video, hard cuts, a big white title box
and numbered pills that pop in one by one (the format of the viral list Reels the owner shared).
No university logos: names in text only. Each clip is labelled with the real place it shows.
Usage: python3 campus.py bg | stills | frames | all"""
import base64, pathlib, sys, os, json, subprocess
sys.path.insert(0, '../v2'); import gen15 as g
b = lambda p: base64.b64encode(pathlib.Path(p).read_bytes()).decode()
FD = pathlib.Path('../fbcover/node_modules/@fontsource')
def face(name, pkg, ws):
    s = ''
    for w in ws:
        for sub, r in g.RNG.items():
            f = FD/pkg/'files'/f'{pkg}-{sub}-{w}-normal.woff2'
            if f.exists(): s += "@font-face{font-family:%s;font-weight:%d;unicode-range:%s;src:url(data:font/woff2;base64,%s)}\n" % (name, w, r, b(f))
    return s
CSS = face('M', 'montserrat', (600, 700, 800, 900)) + face('S', 'literata', (700,))
# each school's name on a card in its own colour (text only, no logos or seals)
SCHOOL = {'Harvard': '#A51C30', 'MIT': '#5A5D61', 'Yale': '#00356B', 'Princeton': '#E77500', 'Stanford': '#8C1515', 'Cornell': '#B31B1B', 'Columbia': '#1D4F91'}
s0 = open('sat.py').read()
bcss = s0[s0.index('.brand{{'):s0.index('\n', s0.index('.brand .bt small svg'))].replace('{{', '{').replace('}}', '}')
bhtml = s0[s0.index('<div class="brand">'):s0.index('</div></div>', s0.index('<div class="brand">'))+12].replace('{LG}', 'data:image/png;base64,'+b('../fbcover/logo_t.png')).replace('{{', '{').replace('}}', '}')
W, H, FPS = 1080, 1920, 30
U = '/root/.claude/uploads/7b9b247d-7185-5faa-ae2d-e13a2742cc61/'
COL = U + '5254c3d3-4301307-hd_1920_1080_30fps.mp4'      # Columbia University, New York (landscape)
LAWN = U + 'b75e1901-6145396-uhd_2160_3840_24fps.mp4'    # students on a campus lawn (unnamed)
BOS = U + 'e675abc3-14902158_2160_3840_30fps.mp4'        # Boston across the Charles River
RIV = U + '9aa53a46-15029439_2160_3840_30fps.mp4'        # Charles River boathouses, Boston
GRAD = U + 'b27941e3-7970447-uhd_3840_2160_30fps.mp4'     # graduates putting on hoods (no university named)

QUAD = U + '13c3cd35-11951225_3840_2160_25fps.mp4'       # sandstone quad, red roofs (not named: identity not confirmed)
COFFEE = U + '1a71d79f-6145404-uhd_2160_3840_24fps.mp4'   # students with coffee on a lawn (unnamed)
STAIRS = U + '1357ef54-7683445-hd_1080_1920_30fps.mp4'    # students walking down campus stairs (unnamed)
# (clip, start, length, crop-x for landscape as a fraction of width, place label)
SHOTS = [
 (QUAD, 0.3, 3.4, 0.42, ''),
 (BOS, 0.0, 4.4, None, 'Boston · Charles River'),
 (COFFEE, 1.0, 6.4, None, ''),
 (RIV, 1.0, 4.8, None, 'Boston · Charles River'),
 (STAIRS, 3.0, 4.6, None, ''),
 (GRAD, 2.0, 4.6, 0.45, ''),
]
ST = []; t = 0
for sh in SHOTS: ST.append(round(t, 2)); t += sh[2]
DUR = round(t, 2)

# scenes, one per shot: title (*word* = marker), pills [(text, offset)], big line
SC = [
 dict(kind='hook', tag='ГАДААДАД СУРАХ · 2027', hero='11/1', line='Энэ өдрийг алдвал *тэтгэлэг* алдаж болно'),
 dict(kind='early', tag='EARLY ГЭЖ ЮУ ВЭ?', title='Эрт өгвөл хариу *эрт* ирнэ', tiles=[('ӨРГӨДӨЛ ӨГӨХ','11/1'),('ХАРИУ ИРЭХ','12-р сарын дунд')], note='Yale, Princeton: хариу 12-р сарын дунд'),
 dict(kind='check', tag='11/1-ЭЭС ӨМНӨ', title='Хийх *3* зүйл', items=[('Өргөдлөө илгээх',''),('Тэтгэлгийн маягт илгээх','Ихэнх сургууль: CSS Profile'),('Тэтгэлэг хүсэх','Өргөдөл дээрээ тэмдэглэх')]),
 dict(kind='vs', tag='ЖИШЭЭ · EARLY', title='Маягтын огноо *өөр*', schools=[('Harvard','11/1'),('MIT','11/30')], note='Олон улсын сурагч · CSS Profile + IDOC'),
 dict(kind='warn', tag='АНХААР', title='Хугацаа хэтэрвэл?', school='Cornell', big='Тэтгэлэг хүсэх *эрхгүй*', sub='бакалаврын бүх хугацаанд'),
 dict(kind='end', tag='GLOBAL MATH PREP', title='Хадгалаад, *найздаа* илгээгээрэй', cta='Бүх сургуулийн огноо тайлбарт байгаа', disc='Огноог 2026.10.06-нд албан ёсны сайтаас шалгасан, өөрчлөгдөж болно. Not affiliated with or endorsed by any university named.'),
]

import re as _re
def words(txt):
    # split into words; *...* marks the highlighted phrase (kept as one unit)
    out = []
    for part in _re.split(r'(\*[^*]+\*)', txt):
        if not part: continue
        if part.startswith('*'):
            out.append(f'<span class="w"><span class="mk">{part[1:-1]}</span></span>')
        else:
            out += [f'<span class="w">{w}</span>' for w in part.split()]
    return ' '.join(out)

def scene_html(i, s):
    k = s['kind']
    h = f'<div class="sc k-{k}" id="s{i}"><div class="hd"><div class="tag">{s["tag"]}</div>'
    if s.get('title'): h += f'<div class="ttl">{words(s["title"])}</div>'
    h += '</div>'
    if k == 'hook':
        h += f'<div class="hero pop" data-d="0.15"><small>11-Р САРЫН</small><b>1</b></div><div class="line">{words(s["line"])}</div>'
    if k == 'early':
        h += '<div class="tiles">' + ''.join(f'<div class="tile pop" data-d="{0.6+0.5*j}"><small>{l}</small><b>{v}</b></div>' for j, (l, v) in enumerate(s['tiles'])) + '</div>'
    if k == 'check':
        h += '<div class="items">' + ''.join(f'<div class="it" data-k="{j}"><span class="bx"><svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></span><span class="tx"><b>{m}</b>' + (f'<small>{sub}</small>' if sub else '') + '</span></div>' for j, (m, sub) in enumerate(s['items'])) + '</div>'
    if k == 'vs':
        h += '<div class="vs">' + ''.join(f'<div class="sch pop" data-d="{0.6+0.6*j}" style="--c:{SCHOOL[n]}"><span class="nm">{n}</span><span class="lb">МАЯГТ</span><b>{d}</b></div>' for j, (n, d) in enumerate(s['schools'])) + '</div>'
    if k == 'warn':
        h += f'<div class="wbox pop" data-d="0.5" style="--c:{SCHOOL[s["school"]]}"><span class="nm">{s["school"]}</span><div class="wb">{words(s["big"])}</div><small>{s["sub"]}</small></div>'
    if s.get('note'): h += f'<div class="note">{s["note"]}</div>'
    if s.get('cta'): h += f'<div class="cta pop" data-d="0.7">{s["cta"]}</div>'
    if s.get('disc'): h += f'<div class="disc">{s["disc"]}</div>'
    if SHOTS[i][4]: h += f'<div class="place"><b></b>{SHOTS[i][4]}</div>'
    return h + '</div>'

bars = ''.join(f'<div class="bar"><b id="b{i}"></b></div>' for i in range(len(SC)))
page = f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;overflow:hidden;font-family:M;background:transparent}}
{bcss}
.shade{{position:absolute;inset:0;background:linear-gradient(rgba(5,10,25,.55),rgba(5,10,25,.15) 30%,rgba(5,10,25,.25) 55%,rgba(5,10,25,.75))}}
.bars{{position:absolute;left:36px;right:36px;top:118px;display:flex;gap:8px}}
.bar{{flex:1;height:6px;border-radius:6px;background:rgba(255,255,255,.35);overflow:hidden}} .bar b{{display:block;height:100%;width:0;background:#fff}}
.sc{{position:absolute;inset:0;opacity:0}}
.hd{{position:absolute;left:64px;right:64px;top:290px}}
.tag{{display:table;font:900 28px M;letter-spacing:4px;color:#111;padding:10px 20px;border-radius:999px;background:#ffd43b;margin-bottom:18px;opacity:0;box-shadow:0 6px 18px rgba(0,0,0,.35)}}
.ttl{{display:inline-block;font:900 74px/1.1 M;color:#fff;letter-spacing:-1px;background:rgba(10,18,40,.9);border-radius:26px;padding:22px 30px 26px;box-shadow:0 16px 40px rgba(0,0,0,.4)}}
.w{{display:inline-block;opacity:0;margin-right:.18em}}
.mk{{color:#ffd43b;background:linear-gradient(#ffd43b,#ffd43b) no-repeat 0 100%/0% 8px;padding:0 2px 6px}}
.pop{{opacity:0}}
/* hook: one giant date */
.hero{{position:absolute;left:0;right:0;top:470px;text-align:center;color:#fff}}
.hero small{{display:block;font:900 64px M;letter-spacing:10px;text-shadow:0 6px 30px rgba(0,0,0,.6)}}
.hero b{{display:block;font:900 560px/0.9 M;color:#ffd43b;letter-spacing:-20px;text-shadow:0 20px 60px rgba(0,0,0,.55)}}
.line{{position:absolute;left:64px;right:64px;top:1120px;text-align:center;font:900 70px/1.15 M;color:#fff;background:rgba(10,18,40,.9);border-radius:28px;padding:26px 30px 32px;box-shadow:0 16px 40px rgba(0,0,0,.4)}}
.k-hook .hd{{top:300px}}
/* early: two stat tiles */
.tiles{{position:absolute;left:64px;right:64px;top:720px;display:grid;grid-template-columns:1fr 1fr;gap:24px}}
.tile{{background:#fff;border-radius:30px;padding:30px 28px 34px;box-shadow:0 16px 40px rgba(0,0,0,.35);min-height:300px;display:flex;flex-direction:column;justify-content:space-between}}
.tile small{{font:900 28px M;letter-spacing:3px;color:#667}}
.tile b{{font:900 92px/1.02 M;color:#111;letter-spacing:-2px}}
.tile:nth-child(2) b{{font-size:70px;color:#1d4fd8}}
/* checklist */
.items{{position:absolute;left:64px;right:64px;top:640px;display:flex;flex-direction:column;gap:22px}}
.it{{display:flex;align-items:center;gap:28px;background:#fff;border-radius:28px;padding:26px 30px;box-shadow:0 14px 34px rgba(0,0,0,.32);opacity:0}}
.bx{{flex:none;width:92px;height:92px;border-radius:22px;border:6px solid #111;display:flex;align-items:center;justify-content:center}}
.bx svg{{width:64px;height:64px;fill:none;stroke:#fff;stroke-width:3.4;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:24;stroke-dashoffset:24}}
.tx b{{display:block;font:900 58px/1.1 M;color:#111}} .tx small{{display:block;font:700 36px/1.2 M;color:#555;margin-top:6px}}
/* vs: two school tiles */
.vs{{position:absolute;left:64px;right:64px;top:700px;display:grid;grid-template-columns:1fr 1fr;gap:24px}}
.sch{{background:var(--c);border-radius:32px;padding:40px 24px 44px;text-align:center;color:#fff;box-shadow:0 18px 44px rgba(0,0,0,.4);border:4px solid rgba(255,255,255,.85)}}
.sch .nm{{display:block;font:700 76px S;letter-spacing:1px}}
.sch .lb{{display:block;font:800 26px M;letter-spacing:5px;opacity:.85;margin-top:26px}}
.sch b{{display:block;font:900 128px/1 M;letter-spacing:-4px;margin-top:6px}}
/* warn */
.wbox{{position:absolute;left:64px;right:64px;top:700px;background:#fff;border-radius:32px;overflow:hidden;box-shadow:0 18px 44px rgba(0,0,0,.4);text-align:center;padding-bottom:40px}}
.wbox .nm{{display:block;background:var(--c);color:#fff;font:700 70px S;padding:22px 0 26px;letter-spacing:1px}}
.wb{{font:900 78px/1.12 M;color:#111;margin:36px 36px 10px}}
.wb .mk{{color:#c92a2a;background-image:linear-gradient(#c92a2a,#c92a2a)}}
.wbox small{{display:block;font:800 44px M;color:#444}}
.note{{position:absolute;left:64px;right:64px;top:1150px;text-align:center;font:800 34px/1.3 M;color:#fff;opacity:0;background:rgba(10,18,40,.88);padding:16px 24px;border-radius:22px}}
.cta{{position:absolute;left:64px;right:64px;top:700px;text-align:center;background:#ffd43b;color:#111;border-radius:30px;padding:34px 34px;font:900 58px/1.2 M;box-shadow:0 16px 40px rgba(0,0,0,.35)}}
.disc{{position:absolute;left:64px;right:64px;top:1250px;text-align:center;font:600 27px/1.4 M;color:#fff;background:rgba(10,18,40,.88);border-radius:18px;padding:14px 20px;opacity:0}}
.place{{position:absolute;left:40px;top:1420px;display:flex;align-items:center;gap:12px;background:rgba(10,18,40,.85);color:#fff;font:800 30px M;padding:10px 22px 10px 16px;border-radius:999px}}
.place b{{width:12px;height:12px;border-radius:50%;background:#ff4b4b}}
</style></head><body><div class="shade"></div><div class="bars">{bars}</div>{bhtml}{"".join(scene_html(i, s) for i, s in enumerate(SC))}
<script>
const ST={json.dumps(ST)},DUR={DUR};
const cl=x=>Math.max(0,Math.min(1,x)); const eo=x=>1-Math.pow(1-cl(x),3);
function render(t){{
 for(let i=0;i<ST.length;i++){{
  const s=ST[i], e=(i+1<ST.length?ST[i+1]:DUR), a=t-s, el=document.getElementById('s'+i);
  document.getElementById('b'+i).style.width=(cl((t-s)/(e-s))*100)+'%';
  if(a<0||t>=e+(i+1<ST.length?0:1)){{el.style.opacity=0;continue;}}
  el.style.opacity=1;
  const tg=el.querySelector('.tag'); const pt=eo(a/0.25); tg.style.opacity=pt; tg.style.transform=`translateX(${{(1-pt)*-30}}px)`;
  const ws=[...el.querySelectorAll('.w')];
  ws.forEach((w,k)=>{{const inLine=w.closest('.line,.wb'); const st=(inLine?(w.closest('.wb')?1.0:0.9):0.1)+0.05*(inLine?ws.filter(x=>x.closest('.line,.wb')).indexOf(w):k); const p=eo((a-st)/0.3);
    w.style.opacity=p; w.style.transform=`translateY(${{(1-p)*30}}px)`; w.style.filter=`blur(${{(1-p)*8}}px)`;
    const m=w.querySelector('.mk'); if(m) m.style.backgroundSize=`${{eo((a-st-0.25)/0.35)*100}}% 8px`;}});
  el.querySelectorAll('.pop').forEach(x=>{{const q=cl((a-(+x.dataset.d))/0.35); const e2=q<1?1+0.7*Math.sin(q*Math.PI)*(1-q):1; x.style.opacity=eo(q*1.6); x.style.transform=`scale(${{(0.82+0.18*eo(q))*e2}})`;}});
  el.querySelectorAll('.it').forEach(x=>{{const la=a-0.6-1.15*(+x.dataset.k); const q=eo(la/0.3); x.style.opacity=q; x.style.transform=`translateX(${{(1-q)*120}}px)`;
    const c=cl((la-0.45)/0.3); x.querySelector('.bx').style.background=c>0?`rgba(43,179,95,${{c}})`:'transparent'; x.querySelector('.bx').style.borderColor=c>0.5?'#2bb35f':'#111'; x.querySelector('svg').style.strokeDashoffset=24*(1-c);}});
  el.querySelectorAll('.note,.disc').forEach(x=>{{const d=x.className=='note'?1.9:1.2; const q=eo((a-d)/0.4); x.style.opacity=q; x.style.transform=`translateY(${{(1-q)*24}}px)`;}});
 }}
}}
</script></body></html>'''


def bg():
    os.makedirs('campus_bg', exist_ok=True); parts = []
    for k, (f, s, d, cx, _) in enumerate(SHOTS):
        if cx is None:
            vf = f'scale={int(W*1.25)}:{int(H*1.25)}:force_original_aspect_ratio=increase,crop={int(W*1.25)}:{int(H*1.25)}'
        else:
            vf = f"crop=ih*9/16:ih:(iw-ih*9/16)*{cx}*1.0:0,scale={int(W*1.25)}:{int(H*1.25)}"
        n = int(d*FPS)
        vf += f",fps={FPS},zoompan=z='1+0.07*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS}"
        out = f'campus_bg/p{k}.mp4'
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(s), '-t', str(d), '-i', f, '-an', '-vf', vf + ',setsar=1', '-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p', out], check=True)
        parts.append(out)
    open('campus_bg/list.txt', 'w').write(''.join(f"file '{os.path.basename(p)}'\n" for p in parts))
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', 'campus_bg/list.txt', '-c', 'copy', 'campus_bg/bg.mp4'], check=True)

from playwright.sync_api import sync_playwright
def overlay(mode):
    os.makedirs('framesC', exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': W, 'height': H}); pg.set_content(page); pg.wait_for_timeout(800)
        if mode == 'stills':
            for k, t0 in enumerate(ST):
                e = ST[k+1] if k+1 < len(ST) else DUR
                pg.evaluate(f'render({e-0.25})'); pg.screenshot(path=f'co_{k}.png', omit_background=True)
        else:
            for i in range(int(DUR*FPS)):
                pg.evaluate(f'render({i/FPS})'); pg.screenshot(path=f'framesC/f{i:04d}.png', omit_background=True)
        br.close()

mode = sys.argv[1] if len(sys.argv) > 1 else 'stills'
if mode in ('bg', 'all'): bg()
if mode == 'stills': overlay('stills')
if mode in ('frames', 'all'): overlay('frames')
if mode == 'all':
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', 'campus_bg/bg.mp4', '-framerate', str(FPS), '-i', 'framesC/f%04d.png',
                    '-filter_complex', '[0:v][1:v]overlay=0:0:format=auto', '-t', str(DUR), '-c:v', 'libx264', '-crf', '19', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', 'GMP-Reel-Nov1-Campus-v5.mp4'], check=True)
print('ST', ST, 'DUR', DUR)
