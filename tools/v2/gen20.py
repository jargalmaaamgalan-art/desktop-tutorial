from gen18 import *
AC = '#d97706'; SOFT = '#fde68a'; BG = '#fffbeb'; GRID = 'rgba(217,119,6,.10)'
C = css(AC, SOFT, BG, GRID) + f"""
.qbar{{display:flex;align-items:center;gap:14px;font-family:S,serif;font-size:24px}}
.qn{{background:{INK};color:#fff;font-family:M;font-weight:800;font-size:26px;width:52px;height:48px;display:flex;align-items:center;justify-content:center;border-radius:4px}}
.stem{{font-family:S,serif;font-size:40px;line-height:1.45}}
.disp{{font-family:S,serif;font-size:52px;text-align:center;margin:10px 0 18px}}
.v{{font-style:italic}}
.ov{{text-decoration:overline}}
.chs{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:22px}}
.chx{{border:3px solid {INK};border-radius:16px;padding:16px 22px;display:flex;align-items:center;gap:16px;font-family:S,serif;font-size:36px;background:#fff}}
.chx span.l{{flex:none;width:44px;height:44px;border:2.5px solid {INK};border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:M;font-size:21px;font-weight:800}}
.tag{{display:inline-flex;align-items:center;gap:8px;border:2.5px solid {INK};border-radius:30px;padding:6px 16px;font-size:22px;font-weight:800;background:#fff}}
.tag.h{{background:{INK};color:#fff}}
"""
R2 = '<math style="margin-left:-2px"><msqrt><mn>2</mn></msqrt></math>'
BOOK = '<svg width="26" height="30" viewBox="0 0 24 28" fill="none" stroke="#16121f" stroke-width="2.4"><path d="M4 2h16v24l-8-6-8 6z"/></svg>'

def q(n, diff, dom, emo, disp, stem, choices, secs):
    tag = f'<span class="tag{" h" if diff=="Hard" else ""}">{E("1f525" if diff=="Hard" else "1f60e",32)} {diff}</span><span class="tag">{dom}</span><span class="tag">{E("23f1",30)} ~{secs}</span>'
    chs = '<div class="chs">' + ''.join(f'<div class="chx"><span class="l">{l}</span>{c}</div>' for l, c in zip('ABCD', choices)) + '</div>'
    body = (f'<div style="display:flex;align-items:center;justify-content:space-between"><div><div class="pill">АСУУЛТ {n}/5</div><div style="margin-top:14px">{tag}</div></div>{E(emo,150,"wig")}</div>'
            f'<div class="card" style="padding:28px 30px"><div class="qbar"><div class="qn">{n}</div>{BOOK}<span>Mark for Review</span></div>'
            f'<div style="height:2px;background:#e7dfcf;margin:16px 0 18px"></div>'
            + (f'<div class="disp">{disp}</div>' if disp else '') + f'<div class="stem">{stem}</div>{chs}</div>'
            f'<div class="take">{E("270d",46)}<div>Бодоод, хариугаа <b>комментод</b> бич. Хариу 7-р хуудсанд.</div></div>')
    return (body, '')

P = []
# 1 COVER
P.append((f'''<div class="pill">SAT MATH · СОРИЛ #1</div>
<h1 style="font-size:120px;line-height:.95;margin-top:10px">5 асуулт.</h1>
<h1 style="font-size:76px">Хэдийг нь<br><em>зөв бодох вэ?</em></h1>
<div style="display:flex;gap:14px;flex-wrap:wrap"><span class="tag">{E("1f60e",32)} 2 Medium</span><span class="tag h">{E("1f525",32)} 3 Hard</span><span class="tag">College Board Question Bank</span></div>
<div class="card" style="display:flex;align-items:center;gap:22px;padding:22px 28px">{E("23f1",80,"wig")}<div style="font-size:30px;font-weight:700;line-height:1.3">Цаг хэмжээд бод:<br><span style="color:{AC};font-weight:800">нэг асуултад ~95 секунд</span></div></div>
<div style="display:flex;justify-content:space-between;align-items:center">
 <div style="font-size:24px;font-weight:700;opacity:.75">Хадгалаад ав · Найздаа сорь</div>
 <div style="background:{INK};color:#fff;border-radius:34px;padding:14px 28px;font-size:28px;font-weight:800;box-shadow:6px 6px 0 {AC}">Гүйлгээд үз →</div></div>''',
 f'''<div style="position:absolute;right:70px;top:180px;z-index:1">{E("1f914",200,"fl")}</div>
<div style="position:absolute;right:300px;top:260px;z-index:1" class="pop">{E("1f9ee",110,"wig")}</div>
<div style="position:absolute;right:120px;top:430px;z-index:1">{E("1f525",110,"fl",'animation-delay:-1.4s')}</div>'''))

P.append(q(1, 'Medium', 'Algebra', '1f9e0', '(<span class="v">b</span> − 2)<span class="v">x</span> = 8',
           'In the given equation, <span class="v">b</span> is a constant. If the equation has no solution, what is the value of <span class="v">b</span>?',
           ['2', '4', '6', '10'], '95с'))
P.append(q(2, 'Medium', 'Advanced Math', '1f633' if False else '1f62e', '<span class="v">x</span><sup>2</sup> = −841',
           'How many distinct real solutions does the given equation have?',
           ['Exactly one', 'Exactly two', 'Infinitely many', 'Zero'], '95с'))
P.append(q(3, 'Hard', 'Advanced Math', '1f9d0', '<span class="v">f</span>(<span class="v">x</span>) = (<span class="v">x</span> − 44)(<span class="v">x</span> − 46)',
           'The function <span class="v">f</span> is defined by the given equation. For what value of <span class="v">x</span> does <span class="v">f</span>(<span class="v">x</span>) reach its minimum?',
           ['46', '45', '44', '−1'], '95с'))
P.append(q(4, 'Hard', 'Advanced Math', '1f92f', '<span class="v">f</span>(<span class="v">x</span>) = 4<span class="v">x</span><sup>2</sup> + 64<span class="v">x</span> + 262',
           'The function <span class="v">g</span> is defined by <span class="v">g</span>(<span class="v">x</span>) = <span class="v">f</span>(<span class="v">x</span> + 5). For what value of <span class="v">x</span> does <span class="v">g</span>(<span class="v">x</span>) reach its minimum?',
           ['−13', '−8', '−5', '−3'], '95с'))
P.append(q(5, 'Hard', 'Geometry &amp; Trig', '1f4d0', '',
           f'The perimeter of an isosceles right triangle is <span style="white-space:nowrap">18 + 18{R2}</span> inches. What is the length, in inches, of the hypotenuse of this triangle?',
           ['9', f'9{R2}', '18', f'18{R2}'], '95с'))

# 7 ANSWERS
ans = [('A', '2', '<i>b</i> = 2 үед (<i>b</i> − 2) = 0 болж, 0 = 8 гарна. Энэ хэзээ ч үнэн биш.'),
       ('D', 'Zero', 'Бодит тооны квадрат сөрөг байж чадахгүй.'),
       ('B', '45', 'Парабол тэгш хэмтэй: орой нь 44 ба 46-ийн яг дунд.'),
       ('A', '−13', '<i>f</i>-ийн орой <i>x</i> = −64 ÷ 8 = −8. Тэгэхээр <i>x</i> + 5 = −8, <i>x</i> = −13.'),
       ('C', '18', f'Катет <i>a</i> бол 2<i>a</i> + <i>a</i>√2 = 18 + 18√2, <i>a</i> = 9√2. Гипотенуз = <i>a</i>√2 = 18.')]
rows = ''.join(f'<div style="display:flex;align-items:center;gap:18px;padding:14px 0;{"border-top:2px dashed #e7dfcf;" if i else ""}"><div style="flex:none;width:44px;font-size:30px;font-weight:800">{i+1}</div><div style="flex:none;background:{AC};color:#fff;border:3px solid {INK};border-radius:14px;padding:6px 14px;font-size:26px;font-weight:800;min-width:118px;text-align:center">{l}) {v}</div><div style="font-size:25px;font-weight:600;line-height:1.3">{w}</div></div>' for i, (l, v, w) in enumerate(ans))
score = ''.join(f'<div class="card" style="flex:1;text-align:center;padding:16px 8px;box-shadow:5px 5px 0 {INK}">{E(c,60)}<div style="font-size:28px;font-weight:800;margin-top:4px">{s}</div><div style="font-size:21px;font-weight:700;opacity:.75">{t}</div></div>' for c, s, t in [('1f3c6', '5/5', 'Гайхалтай!'), ('1f4aa', '3–4', 'Бараг боллоо'), ('1f331', '0–2', 'Хамт бэлдье')])
P.append((f'<div style="display:flex;align-items:center;justify-content:space-between"><div><div class="pill">ХАРИУ</div><h1 style="margin-top:14px">Хэдийг нь<br><em>зөв бодсон бэ?</em></h1></div>{E("1f4af",150,"fl")}</div>'
          f'<div class="card" style="padding:14px 26px">{rows}</div><div style="display:flex;gap:18px">{score}</div>', ''))

# 8 END
P.append((end_page(AC, SOFT, 'Math-ыг', 'бодож сурна', 'GMP-ийн асуултын санд <b>3,904 Math асуулт</b>, бүгд алхам алхмаар тайлбартай.',
                   sched_cell('MATH', 'Да · Лх · Ба', AC) + sched_cell('АНГЛИ (R&amp;W)', 'Мя · Пү · Бя', AC, True),
                   [('1f9ee', '3,904 Math асуулт'), ('1f4dd', 'Долоо хоног бүр сорил'), ('1f331', 'Үнэгүй түвшин тогтоох тест')]), ''))

if __name__ == '__main__':
    render(C, P, HERE / 'out20', 'GMP-SAT-Math', video_first=True)
