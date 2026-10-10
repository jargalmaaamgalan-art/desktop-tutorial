"""Words-in-Context post: Cacao and Maize (answer D, confirm). Content from the owner's own explainer (Cacao_and_Maize_Explainer.html).
Model: gen30/gen34. Run: python3 gen35.py [--video]"""
import sys, shutil
import gen30, gen29
from gen30 import frame
from gen18 import E, HERE

AC, SOFT, TINT = '#c2410c', '#fde6d8', '#fff8f3'   # orange: not used by any scheduled post

EXTRA = """
.hk{background:#fde68a;color:#1e1e1e;padding:0 6px;border-radius:8px;font-weight:700}
.cl{display:flex;gap:16px;align-items:center;padding:12px 0;border-top:2px dashed #f3d3c0}
.cl:first-child{border-top:0}
.cl .no{flex:none;width:50px;height:50px;border-radius:50%;background:@AC@;color:#fff;font-size:28px;font-weight:900;display:flex;align-items:center;justify-content:center}
.cl .ph{flex:none;width:330px;font-family:S,serif;font-size:29px;font-weight:700;background:#fde68a;border-radius:10px;padding:4px 10px;line-height:1.3}
.cl .ms{font-size:27px;font-weight:700;color:#334;line-height:1.3}
.vc{background:#fff;border-radius:22px;padding:14px 24px 16px;border:2.5px solid @SOFT@}
.vc.tp{border:3px solid #c62828}
.vc .top2{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap}
.vc .wd{font-family:S,serif;font-size:40px;font-weight:700;color:#c62828}
.vc .pr{font-size:24px;font-weight:700;color:#667}
.vc .tg{font-size:20px;font-weight:800;letter-spacing:1px;background:#c62828;color:#fff;border-radius:20px;padding:3px 14px}
.vc .why{font-size:31px;font-weight:600;color:#223;line-height:1.35;margin-top:4px}
.vc .ex{font-family:S,serif;font-style:italic;font-size:29px;color:#556;margin-top:4px}
.trio{display:flex;gap:12px}
.trio span{flex:1;text-align:center;background:#fff;border:2.5px solid @AC@;border-radius:18px;padding:12px 6px;font-family:S,serif;font-size:34px;font-weight:700;color:@AC@}
.trio span.on{background:@AC@;color:#fff}
""".replace('@AC@', AC).replace('@SOFT@', SOFT)
_css = gen30.css
gen30.css = lambda a, s, t: _css(a, s, t) + EXTRA

def page(C, n, T, body, tag):
    return f'''<!doctype html><html lang="mn"><head><meta charset="utf-8"><style>{C}</style></head><body><div class="pg">
<div class="top"><img src="{gen29.LOGO}"><span>{n:02d} / {T:02d}</span></div>
<div class="mn">{body}</div>
<div class="ft"><span>SAT R&amp;W · ҮГИЙН УТГА</span><span>{"Гүйлгээд үз →" if n < T else "@globalmathprep"}</span></div></div></body></html>'''
gen30.page = page

S1 = 'Domesticated thousands of years ago by Indigenous people in South America, cacao, the plant from which chocolate is made, deviates structurally from the wild plant it is descended from.'
S2 = 'Maize (corn), another crop domesticated by Indigenous Americans, shows so little resemblance to any wild plant that genetic research was necessary to ______ teosinte grass as its ancestor.'
CH = ['acquire', 'develop', 'attract', 'confirm']
PR = 'Which choice completes the text with the most logical and precise word or phrase?'
PASS = f'<span style="font-size:27px;line-height:1.5;display:block">{S1} {S2}</span>'

# 1 cover
cov = gen30.cover('SAT R&amp;W · ҮГИЙН УТГА', '<span class="blue">Эрдэнэ шиш</span><br>өвөг дээдсээ<br>огт санагдуулдаггүй',
                  'Тэгвэл эрдэмтэд түүний өвөг хэн гэдгийг яаж мэдсэн бэ? SAT-ийн нэг үгийн асуулт.',
                  ['Words in Context', '4 сонголт', '1 түлхүүр'], '1f331')

# 2 question
p2 = f'''<div class="pill">ДАСГАЛ · ЭХЛЭЭД ӨӨРӨӨ БОД</div>{frame(1, PASS, CH, prompt=PR)}
<div class="card big" style="padding:16px 24px">Хоосон зайд аль үг тохирох вэ? Хариугаа бодоод дараагийн слайд руу гүйлгээрэй.</div>'''

# 3 clues
S2h = ('Maize (corn), another crop domesticated by Indigenous Americans, shows <span class="hk">so little resemblance</span> to any wild plant that '
       '<span class="hk">genetic research was necessary</span> to ______ <span class="hk">teosinte grass as its ancestor</span>.')
cl = [('so little resemblance', 'Нүдээр харж таних боломжгүй. Бараг адилгүй.'),
      ('genetic research was necessary', 'Эрдэмтдэд баталгаа хэрэгтэй байсан.'),
      ('teosinte grass as its ancestor', 'Батлах гэж байгаа баримт.')]
rows = ''.join(f'<div class="cl"><div class="no">{i}</div><div class="ph">{a}</div><div class="ms">{b}</div></div>' for i, (a, b) in enumerate(cl, 1))
p3 = f'''<div class="pill">ТҮЛХҮҮР ҮГС</div>
<div class="h" style="font-size:72px"><span class="blue">3 түлхүүр</span> хариуг<br>заана</div>
<div class="card" style="padding:16px 24px"><div class="sen" style="font-size:31px;line-height:1.55">{S2h}</div></div>
<div class="card" style="padding:6px 24px">{rows}</div>
<div class="rule" style="font-size:27px">Нүдээр таних боломжгүй тул судалгаа хэрэгтэй болсон. Судалгаа баталгаа өгсөн.</div>'''

# 4 answer
p4 = f'''<div class="pill">ХАРИУ</div>
<div class="okrow"><div class="ok">D) confirm</div><div class="h" style="font-size:56px">= батлах</div></div>
<div class="lead" style="font-size:32px">Дуудлага: <b>kun-FURM</b>. Утга нь “зөв гэдгийг харуулах, батлах”.</div>
<div class="card" style="padding:14px 24px"><div class="lab">“СУДАЛГАА ЮУ ХИЙДЭГ ВЭ?” ГЭЖ АСУУ</div>
<div class="trio"><span>finds</span><span>proves</span><span class="on">confirms</span></div></div>
<div class="card" style="padding:14px 24px"><div class="lab">ТУРШИЖ ҮЗ</div><div class="sen" style="font-size:36px">…genetic research was necessary to <b>confirm</b> teosinte grass as its ancestor.</div></div>
<div class="rule" style="font-size:26px">Хэв маяг: <u>to ___ X as Y</u> → confirm, identify, establish<br>so … that research was necessary → баталгаа хэрэгтэй</div>'''

# 5 wrong
def vc(w, pr, mean, why, ex, trap=False):
    tag = '<span class="tg">ХАМГИЙН СЭТГЭЛ ТАТАМ</span>' if trap else ''
    return f'<div class="vc{" tp" if trap else ""}"><div class="top2"><span class="wd">{w}</span><span class="pr">{pr} · {mean}</span>{tag}</div><div class="why">{why}</div><div class="ex">{ex}</div></div>'
p5 = f'''<div class="pill">БУРУУ СОНГОЛТУУД</div>
<div class="h" style="font-size:66px">Яагаад <span class="blue">develop</span><br>урхи вэ?</div>
{vc('B) develop', 'di-VEL-up', 'бүтээх', 'Судалгаа өвөг дээдсийг бүтээж чадахгүй. Teosinte өмнө нь байсан. Шинжлэх ухаан шиг сонсогддог тул олон хүн сонгодог.', 'Scientists developed a vaccine.', True)}
{vc('A) acquire', 'uh-KWY-er', 'олж авах', 'Судалгаа өвс авдаггүй.', 'The museum acquired a painting.')}
{vc('C) attract', 'uh-TRAKT', 'өөртөө татах', 'Судалгаа өвсийг өөртөө татдаггүй.', 'Flowers attract bees.')}'''

POST = dict(key='Cacao-Maize', AC=AC, SOFT=SOFT, TINT=TINT, nxt='Шинэ SAT дасгал',
            pages=[cov, p2, p3, p4, p5, gen30.endp('Шинэ SAT дасгал')])

if __name__ == '__main__':
    gen30.render(POST, '--video' in sys.argv)
    out = HERE / ('out30-' + POST['key'])
    for f in sorted(out.glob('GMP-Transitions-*')):
        f.rename(out / f.name.replace('GMP-Transitions-Cacao-Maize', 'GMP-WordsInContext-Cacao-Maize'))
