"""GMP explainer Reel, register-video style: hard percent problem (+x% then -x% = -4%, x = 20).
1080x1920, 6 scenes x 4 s = 24 s, 30 fps. JS timeline render(t) so every frame is exact."""
import base64, os, subprocess, sys, shutil
sys.path.insert(0, '/home/claude/desktop-tutorial/tools/v2')
sys.argv = [sys.argv[0]] + sys.argv[1:]
from gen41 import F
from playwright.sync_api import sync_playwright

D = '/home/claude/mascot'
def b(f): return 'data:image/png;base64,' + base64.b64encode(open(f, 'rb').read()).decode()
ROUND, GLOBE = b(f'{D}/gmp-round.png'), b(f'{D}/globe-cut.png')
NAME = b('/home/claude/desktop-tutorial/tools/v2/gmp-name-dark.png')
SC = 4.0
X = '<i>x</i>'
FR = lambda a: f'<span class="fr"><span>{a}</span><span>100</span></span>'

SCENES = [
 dict(big='<span class="pc">'+X+'%</span>', h1='Хувийн', h2='бодлого', it='хамгийн хэцүү нь', bub='Хариу нь 0 биш шүү!',
      body=f'''<div class="card q">Барааны үнийг {X}%-иар <b>өсгөөд</b>, дараа нь {X}%-иар <b>бууруулав</b>.
Эцсийн үнэ анхныхаасаа <b class="g">4%-иар бага</b> болсон.<div class="ask">{X} = ?</div></div>'''),
 dict(big='01', h1='Үржүүлэгч', h2='болгоно', it='хувийг нэмдэггүй', bub='Хувь бүр = үржүүлэгч',
      body=f'''<div class="pill"><span class="n">+</span><span>{X}% өсөх</span><em>× (1 + {FR(X)})</em></div>
<div class="pill"><span class="n">−</span><span>{X}% буурах</span><em>× (1 − {FR(X)})</em></div>
<div class="pill dk"><span class="n">4</span><span>4%-иар бага</span><em>× 0.96</em></div>'''),
 dict(big='02', h1='Нэг', h2='тэгшитгэл', it='хоёр үржүүлэгч = 0.96', bub='(a+b)(a−b) = a² − b²',
      body=f'''<div class="card eq"><div class="l1">(1 + {FR(X)})(1 − {FR(X)}) = 0.96</div>
<div class="arrow">↓</div><div class="l2">1 − ({FR(X)})² = 0.96</div></div>'''),
 dict(big='03', h1='Бодъё', h2='', it='алхам алхмаар', bub='Сөрөг хариу тохирохгүй',
      body=f'''<div class="card eq st"><div class="l1">({FR(X)})² = 0.04</div><div class="arrow">↓</div>
<div class="l1">{FR(X)} = 0.2</div><div class="arrow">↓</div><div class="l2 big2">{X} = 20</div></div>'''),
 dict(big='20', h1='Шалгая', h2='', it='100-аар туршъя', bub='96 = 4%-иар бага ✓',
      body='''<div class="chain"><div class="c">100</div><div class="op">× 1.20</div><div class="c">120</div><div class="op">× 0.80</div><div class="c ok">96 ✓</div></div>
<div class="card note">Олон сурагч «0%» эсвэл «4%» гэж хариулдаг. Үржүүлэгчээр бодвол 20 гарна.</div>'''),
 dict(big='<span class="sat">SAT</span>', h1='Хамт', h2='бэлдье', it='Digital SAT · Math + English', bub='Дараагийн бодлого удахгүй!',
      body='''<div class="pill"><span class="n">01</span><span>Үнэгүй түвшний тест</span></div>
<div class="pill"><span class="n">02</span><span>Коммент дээр <b>«SAT»</b> гэж бичээрэй</span></div>
<div class="pill dk"><span class="n">03</span><span>globalmathprep.academy</span></div>'''),
]
DUR = SC * len(SCENES)

scenes_html = ''.join(f'''<section class="sc" data-i="{i}">
<div class="hero"><div class="big a">{s['big']}</div><div class="ht"><div class="h1 a">{s['h1']}</div>{f'<div class="h2 a">{s["h2"]}</div>' if s['h2'] else ''}<div class="it a">{s['it']}</div></div></div>
<div class="body">{s['body']}</div>
<div class="bub a"><small>УХАА</small><span>{s['bub']}</span></div></section>''' for i, s in enumerate(SCENES))

HTML = f'''<!doctype html><html><head><meta charset="utf-8"><style>
{F('R', 'rubik', [600, 800, 900])}{F('S', 'source-serif-4', [600, 700])}{F('N', 'nunito', [800, 900])}
*{{box-sizing:border-box;margin:0}}
:root{{--ink:#1f3b47;--gold:#f2ad3d;--bg:#eef3f5}}
body{{width:1080px;height:1920px;overflow:hidden;position:relative;font-family:R,sans-serif;color:var(--ink);
 background:linear-gradient(rgba(31,59,71,.06) 1px,transparent 1px) 0 0/54px 54px,linear-gradient(90deg,rgba(31,59,71,.06) 1px,transparent 1px) 0 0/54px 54px,radial-gradient(900px 700px at 100% 0,#dfe8ee 0,var(--bg) 60%)}}
.brand{{position:absolute;left:64px;top:110px;display:flex;align-items:center;gap:18px;z-index:5}}
.brand .r{{width:100px;height:100px;border-radius:50%;box-shadow:0 6px 16px rgba(31,59,71,.25)}}
.brand .w{{height:34px;display:block}}.brand .jg{{font-family:S,serif;font-weight:700;font-size:25px;letter-spacing:5px;color:#af7f22;margin-top:10px}}
.prog{{position:absolute;left:64px;right:64px;top:250px;height:8px;border-radius:8px;background:rgba(31,59,71,.12);z-index:5}}
.prog i{{display:block;height:100%;border-radius:8px;background:var(--gold);width:0}}
.sc{{position:absolute;inset:0;opacity:0}}
.hero{{position:absolute;left:56px;right:56px;top:330px;height:520px;display:flex;align-items:center;gap:30px}}
.big{{font-family:R,sans-serif;font-weight:900;font-size:320px;line-height:.8;color:var(--gold);letter-spacing:-18px;text-shadow:14px 14px 0 rgba(31,59,71,.12);flex:none}}
.big .sat{{font-size:230px;letter-spacing:-8px}}
.big .pc{{font-size:300px;letter-spacing:-10px}}.big i{{font-family:S,serif}}
.h1{{font-weight:800;font-size:70px;line-height:1;color:#2b6170}}
.ht{{min-width:0}}
.h2{{font-weight:900;font-size:96px;line-height:1;letter-spacing:-3px;margin-top:6px}}
.it{{font-family:S,serif;font-style:italic;font-size:46px;color:#2b6170;margin-top:18px}}
.body{{position:absolute;left:64px;right:64px;top:900px;display:flex;flex-direction:column;gap:26px;align-items:flex-start}}
.pill{{display:flex;align-items:center;gap:22px;background:#fff;border:4px solid var(--ink);border-radius:80px;padding:18px 40px 18px 18px;font-weight:800;font-size:46px;box-shadow:0 10px 24px rgba(31,59,71,.12)}}
.pill .n{{flex:none;width:82px;height:82px;border-radius:50%;background:var(--gold);display:flex;align-items:center;justify-content:center;font-weight:900;font-size:40px}}
.pill.dk .n{{background:var(--ink);color:var(--gold)}}
.pill em{{font-style:normal;font-family:S,serif;font-weight:700;color:#2b6170;margin-left:6px}}
.card{{background:#fff;border:4px solid var(--ink);border-radius:36px;padding:34px 40px;box-shadow:0 12px 28px rgba(31,59,71,.12);width:952px}}
.q{{font-weight:600;font-size:52px;line-height:1.35}}.q b{{font-weight:900}}.q .g{{color:#c47f0e;white-space:nowrap}}
.ask{{margin-top:22px;display:inline-block;background:var(--gold);border-radius:24px;padding:8px 34px;font-weight:900;font-size:72px}}
.eq{{font-family:S,serif;font-weight:600;font-size:74px;text-align:center}}.eq i{{font-style:italic}}
.eq .arrow{{font-family:R;color:var(--gold);font-size:60px;line-height:1.1}}
.eq .l2{{display:inline-block;background:#fff4dc;border-radius:20px;padding:6px 26px}}
.eq .big2{{font-size:110px;background:var(--gold)}}
.st{{font-size:58px;padding:22px 40px;width:680px}}
.st .big2{{font-size:84px}}
.fr{{display:inline-flex;flex-direction:column;vertical-align:middle;font-size:.62em;line-height:1.05;text-align:center;margin:0 4px}}
.fr span:first-child{{border-bottom:4px solid currentColor;padding:0 6px}}
.chain{{display:flex;align-items:center;gap:14px;flex-wrap:wrap}}
.chain .c{{background:#fff;border:4px solid var(--ink);border-radius:26px;padding:16px 26px;font-family:S,serif;font-weight:700;font-size:72px}}
.chain .c.ok{{background:var(--gold)}}.chain .op{{font-weight:800;font-size:40px;color:#2b6170}}
.note{{font-weight:700;font-size:44px;line-height:1.35}}
.bub{{position:absolute;left:64px;top:1560px;width:640px;background:#fff;border:4px solid var(--ink);border-radius:34px;padding:24px 34px;box-shadow:0 12px 26px rgba(31,59,71,.14)}}
.bub:after{{content:'';position:absolute;right:-30px;top:50px;border:16px solid transparent;border-left:28px solid var(--ink)}}
.bub small{{display:block;font-weight:900;font-size:26px;letter-spacing:6px;color:#2b6170}}
.bub span{{display:block;font-weight:800;font-size:46px;margin-top:6px}}
.globe{{position:absolute;left:730px;top:1440px;width:300px;z-index:4}}
.shadow{{position:absolute;left:790px;top:1735px;width:190px;height:28px;border-radius:50%;background:rgba(31,59,71,.22);filter:blur(5px)}}
.foot{{position:absolute;left:64px;right:64px;bottom:60px;display:flex;justify-content:space-between;font-family:N;font-weight:900;font-size:30px;color:#6a8590}}
</style></head><body>
<div class="brand"><img class="r" src="{ROUND}"><div><img class="w" src="{NAME}"><div class="jg">JARGALMAA AMGALAN</div></div></div>
<div class="prog"><i id="pg"></i></div>
{scenes_html}
<div class="shadow" id="sh"></div><img class="globe" id="gl" src="{GLOBE}">
<div class="foot"><span>SAT MATH · PERCENT</span><span>globalmathprep.academy</span></div>
<script>
const SC={SC*1000}, N={len(SCENES)};
const ease=t=>t<0?0:t>1?1:1-Math.pow(1-t,3);
function render(t){{
  document.getElementById('pg').style.width=(Math.min(t/(SC*N),1)*100)+'%';
  document.querySelectorAll('.sc').forEach((s,i)=>{{
    const st=i*SC, lt=t-st;
    const on=lt>=-1 && lt<SC; s.style.opacity=on?1:0; if(!on)return;
    const out=ease((lt-(SC-350))/350);
    s.querySelectorAll('.a,.body>*').forEach((e,k)=>{{
      const p=ease((lt-120-k*170)/450);
      const y=(1-p)*60 - out*40; e.style.opacity=(p*(1-out)).toFixed(3);
      e.style.transform=e.classList.contains('big')?`scale(${{.6+.4*p}}) translateY(${{-out*40}}px)`:`translateY(${{y}}px)`;
    }});
  }});
  const ph=(t%1400)/1400, j=Math.abs(Math.sin(ph*Math.PI));
  document.getElementById('gl').style.transform=`translateY(${{-70*j}}px) rotate(${{-4*j}}deg)`;
  document.getElementById('sh').style.transform=`scale(${{1-0.4*j}})`; document.getElementById('sh').style.opacity=1-0.5*j;
}}
render(0);
</script>
</body></html>'''

if __name__ == '__main__':
    open(f'{D}/pctvid.html', 'w').write(HTML)
    video = '--video' in sys.argv
    fr = f'{D}/pframes'; shutil.rmtree(fr, ignore_errors=True); os.makedirs(fr)
    times = [i * 1000 / 30 for i in range(int(DUR * 30))] if video else [k * SC * 1000 + 2600 for k in range(len(SCENES))]
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1920})
        pg.goto(f'file://{D}/pctvid.html'); pg.wait_for_timeout(500)
        for i, t in enumerate(times):
            pg.evaluate(f'render({t})')
            pg.screenshot(path=f'{fr}/{i:04d}.png')
        br.close()
    if video:
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', '30', '-i', f'{fr}/%04d.png', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', f'{D}/GMP-Explain-Percent-x20.mp4'], check=True)
    print('ok')
