"""SAT Math: absolute value = distance, count both sides of zero. One post, 6 slides.
Content verbatim from sat-math/course/ch18-absolute-value.html (GMP module), lesson 18-1:
lesson text + Worked Example 1 (|x+1|<5 -> 9), guided G1 (|x|<4 -> 7), practice Q2 (|x+6|<3 -> 5)."""
import subprocess, shutil, sys
import gen29, gen30, gen24
from gen18 import E, HERE
from playwright.sync_api import sync_playwright

AC, SOFT, TINT = '#0f766e', '#d5f0ec', '#f2fbf9'   # teal (not used by recent posts)
GREEN = '#15803d'; RED = '#c62828'; INK = '#1e1e1e'

EXTRA = f"""
.m{{font-family:S,serif;font-style:normal;white-space:nowrap}} .m i{{font-style:italic}}
.steps{{display:flex;flex-direction:column;gap:0}}
.st{{display:flex;gap:20px;align-items:center;padding:14px 0;border-top:2px dashed #dfe6e4}}
.st:first-child{{border-top:0}}
.st .k{{flex:none;width:52px;height:52px;border-radius:50%;background:{AC};color:#fff;display:flex;align-items:center;justify-content:center;font-size:27px;font-weight:900}}
.st .e{{flex:none;width:330px;font-family:S,serif;font-size:36px}} .st .e i{{font-style:italic}}
.st .d{{font-size:25px;font-weight:600;color:#445;line-height:1.3}}
.ints{{display:flex;gap:10px;flex-wrap:wrap;justify-content:center}}
.ints span{{background:{AC};color:#fff;border-radius:14px;padding:8px 0;width:70px;text-align:center;font-family:S,serif;font-size:32px;font-weight:700}}
.spr{{display:flex;align-items:center;gap:16px;margin-top:22px;font-family:Arial,Helvetica,sans-serif;font-size:24px;font-weight:700}}
.spr .bxin{{width:230px;height:60px;border:2px solid #1e1e1e;border-radius:8px;display:flex;align-items:center;justify-content:center;font-family:S,serif;font-size:34px;color:{GREEN}}}
.bxs{{font-size:42px!important;margin-top:30px!important}}
.mn{{gap:34px!important}}
.st{{padding:18px 0!important}}
"""

def css():
    return gen30.css(AC, SOFT, TINT) + EXTRA

def m(t):
    return f'<span class="m">{t}</span>'

X = '<i>x</i>'

def numline(lo, hi, a, b, dots):
    """Number line lo..hi, open circles at a and b, filled dots at the integers in dots."""
    W, L, R, Y = 968, 40, 928, 70
    sx = lambda v: L + (v - lo) * (R - L) / (hi - lo)
    s = f'<svg viewBox="0 0 {W} 130" style="display:block;width:100%;height:auto">'
    s += f'<line x1="{L-20}" y1="{Y}" x2="{R+20}" y2="{Y}" stroke="{INK}" stroke-width="3"/>'
    s += f'<line x1="{sx(a)}" y1="{Y}" x2="{sx(b)}" y2="{Y}" stroke="{AC}" stroke-width="9" stroke-linecap="round" opacity=".35"/>'
    for v in range(lo, hi + 1):
        s += f'<line x1="{sx(v)}" y1="{Y-10}" x2="{sx(v)}" y2="{Y+10}" stroke="{INK}" stroke-width="2.5"/>'
        col = AC if v in dots else ('#b0b7c3' if v not in (a, b) else RED)
        s += f'<text x="{sx(v)}" y="{Y+46}" text-anchor="middle" font-family="Georgia,serif" font-size="27" font-weight="{700 if v in dots or v in (a, b) else 400}" fill="{col}">{"−" + str(-v) if v < 0 else v}</text>'
    for v in dots:
        s += f'<circle cx="{sx(v)}" cy="{Y}" r="11" fill="{AC}"/>'
    for v in (a, b):
        s += f'<circle cx="{sx(v)}" cy="{Y}" r="12" fill="#fff" stroke="{RED}" stroke-width="4"/>'
    return s + '</svg>'

def spr(qnum, stem, ans=''):
    return f'''<div class="bx"><div class="bxh"><div><div class="s1">Section 2, Module 1: Math</div><div class="s2">Directions &#8964;</div></div>
<div class="tm">31:24<br><span class="hide">Hide</span></div>
<div class="tl"><div>{gen24.ICAL}<br>Calculator</div><div>{gen24.IREF}<br>Reference</div><div>{gen24.IMORE}<br>More</div></div></div><div class="dash"></div>
<div class="bxb"><div class="qrow"><div class="n">{qnum}</div>{gen24.BOOK}<span class="mr">Mark for Review</span></div>
<div class="bxs">{stem}</div><div class="spr"><span>Answer:</span><div class="bxin">{ans}</div></div></div>
<div class="dash"></div><div class="bxf"><span>Global Math Prep</span><span class="qx">Question {qnum} of 22 &#8963;</span><div class="bt"><span>Back</span><span>Next</span></div></div></div>'''

STEM = f'How many different integer values of {m(X)} satisfy {m(f"|{X}+6|&lt;3")} ?'

PAGES = [
    # 1. cover
    gen30.cover('SAT MATH · ABSOLUTE VALUE',
                f'{m(f"|{X}|&lt;4")}<br>хэдэн бүхэл тоо?<br><span class="blue">3 гэвэл буруу.</span>',
                'Олон хүн тэгийн нөгөө талыг мартдаг. Тэгвэл хариу бараг 2 дахин багасна.',
                ['|x| = зай', 'Тэгийн 2 тал'], '1f4cf'),
    # 2. the idea
    f'''<div class="pill">ГОЛ САНАА</div><div class="h" style="font-size:76px">{m(f"|{X}|")} бол<br><span class="blue">тэг хүртэлх зай</span></div>
<div class="lead">Зай чиглэлгүй. Тиймээс {m("|5|=5")}, {m("|−5|=5")}. Тэгээс 4-өөс бага зайтай тоо <b class="hl">2 талд</b> бий.</div>
<div class="card" style="padding:18px 24px"><div class="lab" style="font-size:34px;letter-spacing:0">{m(f"|{X}|&lt;4")} &nbsp;→&nbsp; {m(f"−4&lt;{X}&lt;4")}</div>{numline(-5, 5, -4, 4, range(-3, 4))}</div>
<div class="rule">Бүхэл тоо: −3, −2, −1, 0, 1, 2, 3 → <span style="font-size:36px">7</span><br><span style="font-weight:600;font-size:25px">Зөвхөн эерэгийг тоолбол 3, тэгийг мартвал 6 гарна.</span></div>''',
    # 3. worked example
    f'''<div class="pill">ЖИШЭЭ · АЛХАМ АЛХМААР</div><div class="h" style="font-size:66px">{m(f"|{X}+1|&lt;5")}<br><span class="blue">хэдэн бүхэл тоо?</span></div>
<div class="card" style="padding:8px 26px"><div class="steps">
<div class="st"><div class="k">1</div><div class="e">−5 &lt; <i>x</i>+1 &lt; 5</div><div class="d">Зай 5-аас бага: 2 тийшээ 5 хүртэл</div></div>
<div class="st"><div class="k">2</div><div class="e">−6 &lt; <i>x</i> &lt; 4</div><div class="d">Гурван талаас нь 1-ийг хас</div></div>
<div class="st"><div class="k">3</div><div class="e">−5, −4, …, 3</div><div class="d">Тэмдэг нь &lt; тул −6, 4 орохгүй</div></div>
<div class="st"><div class="k">4</div><div class="e" style="color:{AC};font-weight:700">9</div><div class="d">3 − (−5) + 1 = 9</div></div></div></div>
<div class="rule">Тоолохоосоо өмнө <i>x</i>-ээ гаргаж ав</div>''',
    # 4. question
    f'''<div class="pill">ДАСГАЛ · ЭХЛЭЭД ӨӨРӨӨ БОД</div>{spr(2, STEM)}
<div class="card big" style="padding:16px 24px">Энэ удаад интервал тэгийг агуулахгүй. Эхлээд <i>x</i>-ийн мужийг ол, дараа нь тоол.</div>''',
    # 5. answer
    f'''<div class="pill">ХАРИУ</div>
<div class="okrow"><div class="ok">5</div><div class="h" style="font-size:56px">бүхэл тоо</div></div>
<div class="card" style="padding:8px 26px"><div class="steps">
<div class="st"><div class="k">1</div><div class="e">−3 &lt; <i>x</i>+6 &lt; 3</div><div class="d">Давхар тэнцэтгэл биш болгож бич</div></div>
<div class="st"><div class="k">2</div><div class="e">−9 &lt; <i>x</i> &lt; −3</div><div class="d">Гурван талаас нь 6-г хас</div></div></div>
{numline(-10, -2, -9, -3, range(-8, -3))}</div>
<div class="ints"><span>−8</span><span>−7</span><span>−6</span><span>−5</span><span>−4</span></div>
<div class="rule">Интервал тэгийг агуулах албагүй</div>''',
    # 6. end
    gen30.endp('Шинэ сэдэв удахгүй'),
]


def page(C, n, T, body):
    return f'''<!doctype html><html lang="mn"><head><meta charset="utf-8"><style>{C}</style></head><body><div class="pg">
<div class="top"><img src="{gen29.LOGO}"><span>{n:02d} / {T:02d}</span></div>
<div class="mn">{body}</div>
<div class="ft"><span>SAT MATH · ABSOLUTE VALUE</span><span>{"Гүйлгээд үз →" if n < T else "@globalmathprep"}</span></div></div></body></html>'''


def render(video):
    out = HERE / 'out31-Absolute-Value'; out.mkdir(exist_ok=True)
    for f in out.glob('*'): f.unlink() if f.is_file() else shutil.rmtree(f)
    C = css(); T = len(PAGES); prefix = 'GMP-Math-Absolute-Value'
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        for i, body in enumerate(PAGES, 1):
            pg.set_content(page(C, i, T, body)); pg.wait_for_timeout(400)
            pg.evaluate("()=>document.getAnimations().forEach(a=>{a.pause();a.currentTime=2500})")
            ov = pg.evaluate("()=>{const m=document.querySelector('.mn');let t=1e9,b=0;for(const c of m.children){const r=c.getBoundingClientRect();t=Math.min(t,r.top);b=Math.max(b,r.bottom)}return [Math.round(t),Math.round(b),m.scrollWidth>m.clientWidth+2]}")
            fn = out / f'{prefix}-{i:02d}-of-{T:02d}.png'; pg.screenshot(path=str(fn))
            print(fn.name, ov, 'OK' if ov[0] >= 130 and ov[1] <= 1240 and not ov[2] else 'OVERFLOW', flush=True)
            if video:
                fr = out / '_f'; fr.mkdir(exist_ok=True)
                for k in range(150):
                    pg.evaluate(f"()=>document.getAnimations().forEach(a=>{{a.pause();a.currentTime={k*1000/30}}})"); pg.screenshot(path=str(fr / f'{k:04d}.png'))
                subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', '30', '-i', str(fr / '%04d.png'), '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '19', '-movflags', '+faststart', str(fn.with_suffix('.mp4'))], check=True)
                shutil.rmtree(fr)
        br.close()

if __name__ == '__main__':
    render('--video' in sys.argv)
