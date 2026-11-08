"""Before/after: today's M003 cover rebuilt with the suggested fixes, same brand colours."""
import pathlib, subprocess
from playwright.sync_api import sync_playwright
H = pathlib.Path(__file__).resolve().parent; T = H.parent
inter = T / 'fonts2/fontsource-inter-5.3.0/package/files'
ser = T / 'poster/fonts/serif/package/files'
ff = ''
for w in (600, 700, 800, 900):
    for sub in ('latin', 'cyrillic'):
        ff += f"@font-face{{font-family:I;font-weight:{w};src:url('{(inter / f'inter-{sub}-{w}-normal.woff2').as_uri()}')}}\n"
for sub in ('latin',):
    for st in ('normal', 'italic'):
        ff += f"@font-face{{font-family:S;font-weight:600;font-style:{st};src:url('{(ser / f'source-serif-4-{sub}-600-{st}.woff2').as_uri()}')}}\n"
LOGO = (T / 'v2/hdr_logo.png').as_uri()
NAVY = '#0d1f4f'; GOLD = '#f6a821'
css = f"""{ff}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;font-family:I,sans-serif;background:{NAVY};color:#fff;position:relative}}
.glow{{position:absolute;right:-220px;top:-160px;width:760px;height:760px;border-radius:50%;background:radial-gradient(circle,#1f3f9a 0%,transparent 70%)}}
.logo{{position:absolute;left:60px;top:54px;height:66px}}
.tag{{position:absolute;left:60px;top:176px;display:flex;gap:12px}}
.tag span{{padding:12px 20px;border-radius:10px;font-weight:800;font-size:26px;letter-spacing:1.5px}}
.t1{{background:{GOLD};color:{NAVY}}} .t2{{border:2.5px solid #6f86c9;color:#cfd9f5}}
.h{{position:absolute;left:60px;right:60px;top:258px;font-weight:900;font-size:94px;line-height:1.02;letter-spacing:-2.5px}}
.h b{{color:{GOLD}}}
.card{{position:absolute;left:60px;right:60px;top:620px;background:#fff;color:#14213d;border-radius:28px;padding:36px 38px 34px}}
.q{{font-family:S,serif;font-size:42px;line-height:1.32}}
.opts{{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:14px;margin-top:28px}}
.o{{border:3px solid #d6dcea;border-radius:18px;padding:16px 0;display:flex;flex-direction:column;align-items:center;gap:6px}}
.o b{{font-weight:800;font-size:24px;color:#6b7690}}
.o span{{font-family:S,serif;font-size:52px;color:{NAVY}}}
.cta{{position:absolute;left:60px;right:60px;top:1120px;display:flex;align-items:center;gap:20px;font-weight:800;font-size:36px}}
.cta s{{text-decoration:none;background:{GOLD};color:{NAVY};padding:12px 22px;border-radius:14px;font-weight:900}}
.foot{{position:absolute;left:60px;right:60px;bottom:44px;display:flex;justify-content:space-between;align-items:center;font-weight:700;font-size:26px;color:#9fb0dc}}
.sw{{background:#fff;color:{NAVY};padding:14px 26px;border-radius:999px;font-weight:800;font-size:26px}}
"""
opts = ''.join(f"<div class='o'><b>{a}</b><span>{v}</span></div>" for a, v in zip('ABCD', ('16', '18', '20', '24')))
body = f"""<div class='glow'></div><img class='logo' src='{LOGO}'>
<div class='tag'><span class='t1'>SAT MATH #003</span><span class='t2'>ХЯЛБАР · 60 СЕК</span></div>
<div class='h'>36 сурагч,<br>харьцаа <b>4 : 5</b>.<br>Охид хэд вэ?</div>
<div class='card'><div class='q'>The ratio of boys to girls in a class of 36 students is 4 : 5. How many girls are in the class?</div><div class='opts'>{opts}</div></div>
<div class='cta'><s>A B C D</s> Хариугаа коммент дээр бич</div>
<div class='foot'><span>@globalmathprep · 1/5</span><span class='sw'>Бодолт →</span></div>"""
html = H / 'm003_fixed.html'
html.write_text(f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>")
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    pg.goto(html.as_uri()); pg.wait_for_timeout(400); pg.screenshot(path=str(H / 'out/M003-cover-fixed.png')); b.close()
html.unlink()
