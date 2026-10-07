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
 (QUAD, 0.3, 3.8, 0.42, ''),
 (BOS, 0.0, 5.2, None, 'Boston · Charles River'),
 (COFFEE, 1.0, 8.4, None, ''),
 (RIV, 1.0, 5.4, None, 'Boston · Charles River'),
 (STAIRS, 3.0, 4.8, None, ''),
 (GRAD, 2.0, 5.0, 0.45, ''),
]
ST = []; t = 0
for sh in SHOTS: ST.append(round(t, 2)); t += sh[2]
DUR = round(t, 2)

# scenes, one per shot: title (*word* = marker), pills [(text, offset)], big line
SC = [
 dict(tag='ГАДААДАД СУРАХ · 2027', title='Энэ өдрийг алдвал тэтгэлэг алдаж болно: *11-р сарын 1*'),
 dict(tag='EARLY ГЭЖ ЮУ ВЭ?', title='Эрт өргөдөл = *Early*', big='Энгийн хугацаанаас эрт өгч, хариугаа *эрт* авна. Олон сургуульд 11-р сарын 1-нд хаагдана.'),
 dict(tag='11-Р САРЫН 1-ЭЭС ӨМНӨ', title='Хийх *3* зүйл', pills=['Өргөдлөө илгээ', 'Тэтгэлгийн маягтаа илгээ: огноо нь өөр', 'Өргөдөл дээрээ тэтгэлэг хүсэхээ тэмдэглэ'], long=True, gap=1.4),
 dict(tag='ЖИШЭЭ', title='Маягтын огноо *өөр*', pills=['Harvard|11/1', 'MIT|11/30'], gap=0.8, note='Early үе · олон улсын сурагч'),
 dict(tag='АНХААР', title='Дараа нь хүсэх боломжгүй', big='Cornell: хугацаандаа хүсээгүй бол бакалаврын бүх хугацаанд тэтгэлэг хүсэх *эрхгүй*'),
 dict(tag='GLOBAL MATH PREP', title='Хадгалаад, *найздаа* илгээ', cta='Бүх сургуулийн огноо тайлбар хэсэгт байгаа', disc='Огноог 2026.10.06-нд албан ёсны сайтаас шалгасан, өөрчлөгдөж болно. Not affiliated with or endorsed by any university named.'),
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
    h = f'<div class="sc" id="s{i}"><div class="hd"><div class="tag">{s["tag"]}</div><div class="ttl">{words(s["title"])}</div></div>'
    if s.get('sub'): h += f'<div class="sub">{s["sub"]}</div>'
    if s.get('pills'):
        h += f'<div class="pills{" long" if s.get("long") else ""}" data-gap="{s.get("gap", 0.45)}">'
        for k, p in enumerate(s['pills']):
            name, _, date = p.partition('|')
            col = SCHOOL.get(name)
            h += f'<div class="pl{" uni" if col else ""}" data-k="{k}"' + (f' style="--c:{col}"' if col else '') + f'><i>{k+1}</i><span class="nm">{name}</span>' + (f'<span class="dt">{date}</span>' if date else '') + '</div>'
        h += '</div>'
    if s.get('note'): h += f'<div class="note">{s["note"]}</div>'
    if s.get('big'): h += f'<div class="big">{words(s["big"])}</div>'
    if s.get('cta'): h += f'<div class="cta">{s["cta"]}</div>'
    if s.get('disc'): h += f'<div class="disc">{s["disc"]}</div>'
    if SHOTS[i][4]: h += f'<div class="place"><b></b>{SHOTS[i][4]}</div>'
    return h + '</div>'

bars = ''.join(f'<div class="bar"><b id="b{i}"></b></div>' for i in range(len(SC)))
page = f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;overflow:hidden;font-family:M;background:transparent}}
{bcss}
.shade{{position:absolute;inset:0;background:linear-gradient(rgba(0,0,0,.5),rgba(0,0,0,.12) 36%,rgba(0,0,0,.05) 60%,rgba(0,0,0,.5))}}
.bars{{position:absolute;left:36px;right:36px;top:118px;display:flex;gap:8px}}
.bar{{flex:1;height:6px;border-radius:6px;background:rgba(255,255,255,.35);overflow:hidden}} .bar b{{display:block;height:100%;width:0;background:#fff}}
.sc{{position:absolute;inset:0;opacity:0}}
.hd{{position:absolute;left:70px;right:70px;top:300px}}
.tag{{display:table;font:900 28px M;letter-spacing:4px;color:#111;padding:10px 20px;border-radius:999px;background:#ffd43b;margin-bottom:18px;opacity:0;box-shadow:0 6px 18px rgba(0,0,0,.35)}}
.ttl{{display:inline-block;font:900 72px/1.12 M;color:#fff;letter-spacing:-1px;background:rgba(10,18,40,.9);border-radius:26px;padding:24px 30px 28px;box-shadow:0 16px 40px rgba(0,0,0,.4)}}
.ttl .mk{{color:#ffd43b;background:linear-gradient(#ffd43b,#ffd43b) no-repeat 0 100%/0% 8px;padding:0 2px 6px}}
.w{{display:inline-block;opacity:0;margin-right:.18em}}
.mk{{background:linear-gradient(#ffd43b,#ffd43b) no-repeat 0 88%/0% 38%;padding:0 4px}}
.sub{{position:absolute;left:70px;top:640px;font:700 40px M;color:#111;background:#fff;border-radius:999px;padding:14px 30px;opacity:0;box-shadow:0 10px 26px rgba(0,0,0,.3)}}
.pills{{position:absolute;left:70px;right:70px;top:760px;display:flex;flex-direction:column;gap:12px}}
.pl{{display:flex;align-items:center;gap:22px;background:rgba(255,255,255,.96);border-radius:22px;padding:10px 26px 10px 12px;box-shadow:0 10px 26px rgba(0,0,0,.28);opacity:0;white-space:nowrap}}
.pl i{{font-style:normal;width:60px;height:60px;border-radius:50%;background:#111;color:#ffd43b;display:flex;align-items:center;justify-content:center;font:900 34px M;flex:none}}
.pl .nm{{font:800 50px M;color:#111;flex:1}}
.pl .dt{{font:900 48px M;color:#e8590c}}
.pl.uni{{background:var(--c);padding:16px 30px 16px 14px}} .pl.uni .nm{{font:700 60px S;color:#fff;letter-spacing:1px}} .pl.uni .dt{{color:#fff;background:rgba(0,0,0,.28);padding:4px 16px;border-radius:12px}} .pl.uni i{{background:#fff;color:#111}}
.pills.long{{gap:20px}} .pills.long .pl{{padding:18px 28px 18px 14px;align-items:flex-start}} .pills.long .nm{{font:800 48px/1.2 M;white-space:normal}} .pills.long .pl i{{margin-top:2px}}
.note{{position:absolute;left:70px;top:1040px;font:800 32px M;color:#fff;letter-spacing:1px;opacity:0;background:rgba(10,18,40,.88);padding:12px 22px;border-radius:999px}}
.big{{position:absolute;left:70px;right:70px;top:700px;font:800 66px/1.18 M;color:#111;background:rgba(255,255,255,.95);border-radius:28px;padding:36px 40px;box-shadow:0 16px 40px rgba(0,0,0,.35);opacity:0}}
.cta{{position:absolute;left:70px;right:70px;top:720px;text-align:center;background:#ff9a1f;color:#111;border-radius:28px;padding:28px 34px;font:900 50px/1.2 M;opacity:0;box-shadow:0 16px 40px rgba(0,0,0,.35)}}
.disc{{position:absolute;left:70px;right:70px;top:1250px;text-align:center;font:600 27px/1.4 M;color:#fff;background:rgba(10,18,40,.88);border-radius:18px;padding:14px 20px;opacity:0}}
.place{{position:absolute;left:40px;top:1400px;display:flex;align-items:center;gap:12px;background:rgba(10,18,40,.85);color:#fff;font:800 30px M;padding:10px 22px 10px 16px;border-radius:999px}}
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
  const tg=el.querySelector('.tag'); const pt=eo(a/0.3); tg.style.opacity=pt; tg.style.transform=`translateX(${{(1-pt)*-30}}px)`;
  /* words: rise out of a soft blur, one after another */
  el.querySelectorAll('.ttl .w,.big .w').forEach((w,k)=>{{const inBig=w.closest('.big'); const st=(inBig?0.55:0.12)+0.07*k; const p=eo((a-st)/0.35);
    w.style.opacity=p; w.style.transform=`translateY(${{(1-p)*34}}px)`; w.style.filter=`blur(${{(1-p)*10}}px)`;}});
  /* highlight sweeps left to right after its word lands */
  el.querySelectorAll('.mk').forEach(m=>{{const w=m.parentElement; const k=[...el.querySelectorAll('.ttl .w,.big .w')].indexOf(w); const inBig=w.closest('.big');
    const st=(inBig?0.55:0.12)+0.07*k+0.3; m.style.backgroundSize=inBig?`${{eo((a-st)/0.4)*100}}% 38%`:`${{eo((a-st)/0.4)*100}}% 8px`;}});
  el.querySelectorAll('.pl').forEach(p=>{{const la=a-0.7-(+p.parentElement.dataset.gap)*(+p.dataset.k); const q=eo(la/0.35); p.style.opacity=q; p.style.transform=`translateX(${{(1-q)*120}}px)`;}});
  el.querySelectorAll('.sub,.note,.big,.cta,.disc').forEach(x=>{{const d={{'sub':0.8,'note':3.6,'big':0.4,'cta':0.7,'disc':1.2}}[x.className]; const q=eo((a-d)/0.4);
    x.style.opacity=q; x.style.transform=`translateY(${{(1-q)*30}}px) scale(${{0.97+0.03*q}})`;}});
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
                    '-filter_complex', '[0:v][1:v]overlay=0:0:format=auto', '-t', str(DUR), '-c:v', 'libx264', '-crf', '19', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', 'GMP-Reel-Nov1-Campus.mp4'], check=True)
print('ST', ST, 'DUR', DUR)
