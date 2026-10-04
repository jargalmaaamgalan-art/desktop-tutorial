"""SAT R&W: a sentence = subject + conjugated verb, even when it sounds odd. One post, 6 slides.
Content verbatim from sat-writing-fragments-lesson.html (GMP module, Ch 3 Sentences and Fragments):
section 01 question 1 (Louis Armstrong), section 03 (The tomato grows / Go!), section 04 (pronouns as subjects)."""
import subprocess, shutil, sys
import gen29, gen30
from gen18 import HERE
from playwright.sync_api import sync_playwright

AC, SOFT, TINT = '#c2410c', '#fbe6da', '#fff8f3'   # burnt orange (not used by recent posts)
GREEN = '#15803d'; RED = '#c62828'

EXTRA = """
.okrow .ok{font-size:40px!important}
.pr{display:flex;gap:10px;flex-wrap:wrap}
.pr span{background:#fff;border:2.5px solid %(AC)s;color:%(AC)s;border-radius:14px;padding:6px 16px;font-family:S,serif;font-size:30px;font-weight:700}
.tag{display:inline-block;border-radius:10px;padding:3px 12px;font-size:20px;font-weight:800;color:#fff;margin-bottom:8px;letter-spacing:1px}
.map .n.hot small{color:#ffe9dc!important}
.tag.y{background:%(G)s} .tag.n{background:%(R)s}
""" % dict(AC=AC, G=GREEN, R=RED)

def css():
    return gen30.css(AC, SOFT, TINT) + EXTRA

PROMPT = 'Which choice completes the text so that it conforms to the conventions of Standard English?'
PASSAGE = ('In the decades after the legendary trumpeter Louis Armstrong retired from performing, his fame continued to grow. '
           'Jazz fans and scholars now unanimously celebrate him as one of the greatest jazz musicians of the twentieth ______ '
           'him to be among the greatest jazz musicians of all time.')
CH = ['century, many consider', 'century many consider', 'century. Many consider', 'century; many considering']

PAGES = [
    # 1. cover
    gen30.cover('SAT R&amp;W · БҮТЭН ӨГҮҮЛБЭР',
                '“Many consider…”<br><span class="blue">бүтэн<br>өгүүлбэр үү?</span>',
                'Сонин сонсогдох нь шалгуур биш. Олон хүн яг энд алддаг.',
                ['Эзэн', '+ Үйл үг', '= Өгүүлбэр'], '1f50d').replace('font-size:104px', 'font-size:90px'),
    # 2. the idea
    f'''<div class="pill">ГОЛ САНАА</div><div class="h" style="font-size:76px">Өгүүлбэрт<br><span class="blue">ердөө 2 зүйл</span> хэрэгтэй</div>
<div class="card fam"><div class="disc">1</div><div><div class="t">Эзэн (subject)</div><div class="d">Хэн эсвэл юу?</div><div class="w">The tomato</div></div></div>
<div class="card fam"><div class="disc">2</div><div><div class="t">Хувирсан үйл үг (verb)</div><div class="d">Эзэн юу хийж байна?</div><div class="w">grows</div></div></div>
<div class="card"><div class="sen"><b>The tomato grows.</b> &nbsp;·&nbsp; <b>Go!</b></div><div class="big" style="font-size:26px;margin-top:6px">Go! ч бас өгүүлбэр: эзэн нь <i>you</i>, далд байна.</div></div>
<div class="rule">Эзэн + үйл үг байвал утга нь ойлгомжгүй байсан ч бүтэн өгүүлбэр</div>''',
    # 3. question
    gen30.qslide(gen30.frame(1, PASSAGE, CH, prompt=PROMPT),
                 'Хоосон зайны дараах хэсэгт эзэн, үйл үг байна уу? Тэгэхээр энэ 1 өгүүлбэр үү, 2 өгүүлбэр үү?'),
    # 4. answer
    gen30.aslide('C) century. Many consider', 'Цэг', [('ЭЗЭН', 'Many'), ('ҮЙЛ ҮГ', 'consider')],
                 [('A) , many', 'Урхи. 2 бүтэн өгүүлбэрийг зөвхөн таслалаар холбосон (comma splice).'),
                  ('B) many', '2 өгүүлбэрийн хооронд ямар ч тэмдэг алга (run-on).'),
                  ('D) ; considering', 'considering бол хувирсан үйл үг биш. Цэгтэй таслалын ард бүтэн өгүүлбэр байх ёстой, энд бүтэн биш.')],
                 'Many consider him… бүтэн өгүүлбэр тул өмнө нь цэг тавина', sep='+'),
    # 5. pronouns as subjects
    f'''<div class="pill">ХАДГАЛААРАЙ</div><div class="h" style="font-size:72px">Эдгээр үг<br><span class="blue">ганцаараа ч эзэн</span> болно</div>
<div class="card"><div class="pr"><span>Many</span><span>Most</span><span>Some</span><span>Few</span><span>Several</span><span>Both</span><span>All</span><span>Others</span><span>Each</span><span>None</span><span>One</span><span>They</span></div></div>
<div class="card"><div class="tag y">БҮТЭН ӨГҮҮЛБЭР</div><div class="sen" style="font-size:33px"><b>Most</b> believe that the tomato is a vegetable.</div>
<div class="big" style="font-size:25px;margin-top:4px">“Хэний ихэнх нь?” гэж гайхаж болох ч эзэн (Most), үйл үг (believe) хоёулаа байна.</div></div>
<div class="card"><div class="tag n">БҮТЭН БИШ</div><div class="sen" style="font-size:33px">Most <b>of whom</b> believe that the tomato is a vegetable</div>
<div class="big" style="font-size:25px;margin-top:4px">whom, which зэрэг w- үг нэмэгдвэл бүтэн биш, хамааралтай хэсэг болно.</div></div>''',
    # 6. end
    gen30.endp('Шинэ сэдэв удахгүй'),
]


def page(C, n, T, body):
    return f'''<!doctype html><html lang="mn"><head><meta charset="utf-8"><style>{C}</style></head><body><div class="pg">
<div class="top"><img src="{gen29.LOGO}"><span>{n:02d} / {T:02d}</span></div>
<div class="mn">{body}</div>
<div class="ft"><span>SAT R&amp;W · БҮТЭН ӨГҮҮЛБЭР</span><span>{"Гүйлгээд үз →" if n < T else "@globalmathprep"}</span></div></div></body></html>'''


def render(video, key='Sentence-Subject-Verb', prefix='GMP-SAT-Sentence-Subject-Verb', pages=PAGES, cssf=css, pagef=page):
    out = HERE / ('out-' + key); out.mkdir(exist_ok=True)
    for f in out.glob('*'): f.unlink() if f.is_file() else shutil.rmtree(f)
    C = cssf(); T = len(pages)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        for i, body in enumerate(pages, 1):
            pg.set_content(pagef(C, i, T, body)); pg.wait_for_timeout(400)
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
