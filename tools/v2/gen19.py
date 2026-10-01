from gen18 import *
AC = '#7c3aed'; SOFT = '#ddd0ff'; BG = '#fbf9ff'; GRID = 'rgba(124,58,237,.09)'
C = css(AC, SOFT, BG, GRID) + f"""
.wc .w{{font-size:44px;font-weight:800;letter-spacing:-.5px}}
.wc .pos{{font-size:19px;font-weight:700;color:{AC};border:2px solid {AC};border-radius:14px;padding:2px 10px;margin-left:10px;vertical-align:middle}}
.wc .d{{font-size:25px;font-weight:600;margin-top:8px;line-height:1.3}}
.wc .mnl{{font-size:25px;font-weight:700;margin-top:8px;color:{AC}}}
.wc .ex{{font-family:S,serif;font-style:italic;font-size:24px;line-height:1.35;margin-top:12px;padding-top:12px;border-top:2px dashed #cfc6e6}}
.wc .ex b{{font-style:normal;font-family:M,sans-serif;font-weight:800;background:{SOFT};padding:0 4px;border-radius:4px}}
"""

def wc(w, pos, d, mn, ex):
    return f'<div class="card wc"><div><span class="w"><span class="hl">{w}</span></span><span class="pos">{pos}</span></div><div class="d">{d}</div><div class="mnl">🇲🇳 {mn}</div><div class="ex">{ex}</div></div>'.replace('🇲🇳 ', 'МН · ')

def group(n, title_a, title_b, emo, words, tip):
    return (f'<div style="display:flex;align-items:center;justify-content:space-between"><div><div class="pill">{n}-Р БҮЛЭГ · 4 ҮГ</div><h1 style="margin-top:16px;font-size:70px">{title_a}<br><em>{title_b}</em></h1></div>{E(emo,170,"fl")}</div>'
            + '<div class="grid">' + ''.join(wc(*w) for w in words) + '</div>'
            + f'<div class="take">{E("1f4a1",46)}<div>{tip}</div></div>', '')

P = []
# 1 COVER (animated)
P.append((f'''<div class="pill">SAT VOCAB · ЦУВРАЛ #1</div>
<div style="display:flex;align-items:flex-end;gap:10px;margin-top:6px">
 <div style="font-size:300px;font-weight:800;line-height:.8;letter-spacing:-14px;color:{AC};margin-right:24px" class="pulse">16</div>
 <div style="font-size:64px;font-weight:800;line-height:1.05;padding-bottom:10px">SAT-д<br>гардаг үг</div></div>
<h1 style="font-size:62px">Жагсаалт биш,<br><em>жишээ өгүүлбэрээр</em> нь сур</h1>
<div><span class="chip">Англи тайлбар</span><span class="chip">Монгол утга</span><span class="chip">Жишээ өгүүлбэр</span></div>
<div style="display:flex;justify-content:space-between;align-items:center;margin-top:10px">
 <div style="font-size:24px;font-weight:700;opacity:.75">Хадгалаад ав · Найздаа илгээ</div>
 <div style="background:{AC};color:#fff;border:3px solid {INK};border-radius:34px;padding:14px 28px;font-size:28px;font-weight:800;box-shadow:6px 6px 0 {INK}">Гүйлгээд үз →</div></div>''',
 f'''<div style="position:absolute;right:70px;top:190px;z-index:1">{E("1f92f",190,"fl")}</div>
<div style="position:absolute;right:300px;top:330px;z-index:1;animation-delay:.4s" class="pop">{E("1f4da",120,"wig")}</div>
<div style="position:absolute;right:90px;top:470px;z-index:1">{E("1f9e0",130,"fl",'animation-delay:-1.2s')}</div>
<div style="position:absolute;left:40px;bottom:120px;z-index:1;opacity:.9">{E("1f4a1",90,"wig",'animation-delay:-.6s')}</div>'''))

# 2 METHOD
bad = ['500 үг жагсаалтаар цээжлэх', 'Жишээ өгүүлбэргүй', 'Хурдан мартагдана']
good = ['SAT-д гардаг үгсээ сонгох', 'Өгүүлбэр дотор нь сурах', 'Уншлагатайгаа хамт давтах']
col = lambda head, emo, items, ic: f'<div class="card" style="flex:1"><div style="display:flex;align-items:center;gap:12px">{E(emo,70)}<div style="font-size:36px;font-weight:800">{head}</div></div>' + ''.join(f'<div style="display:flex;align-items:center;gap:12px;margin-top:18px;font-size:27px;font-weight:700;line-height:1.25">{E(ic,40)}<span>{t}</span></div>' for t in items) + '</div>'
P.append((f'<div class="pill">ЭХЛЭЭД АРГАА ЗӨВ СОНГО</div><h1>Үг цээжлэх<br><em>2 арга</em></h1>'
          f'<div style="display:flex;gap:20px">{col("Удаан арга","1f422",bad,"274c")}{col("Ухаалаг арга","1f680",good,"2705")}</div>'
          f'<div class="card" style="font-family:S,serif;font-size:29px;line-height:1.45">Despite years of criticism, the scientist’s theory was eventually <b style="font-family:M;background:{SOFT};padding:0 6px;border-radius:6px">corroborated</b> by new fossil evidence.<div style="font-family:M;font-size:23px;font-weight:700;color:{AC};margin-top:10px">Өгүүлбэрээс утгыг нь тааж болно: “нотлогдсон, батлагдсан”</div></div>'
          f'<div class="take">{E("1f3af",46)}<div>SAT үгийн утгыг <b>өгүүлбэр дотор нь</b> шалгадаг.</div></div>', ''))

P.append(group(1, 'Судалгаа,', 'нотолгооны үгс', '1f9ea', [
    ('corroborate', 'verb', 'to support with more evidence', 'нотолгоогоор батлах', 'New fossils <b>corroborate</b> the theory that birds came from dinosaurs.'),
    ('refute', 'verb', 'to prove that something is wrong', 'буруу гэж нотлох, няцаах', 'The new data <b>refute</b> the old claim.'),
    ('hypothesize', 'verb', 'to suggest a possible explanation to test', 'таамаглал дэвшүүлэх', 'Scientists <b>hypothesize</b> that bees use color to find flowers.'),
    ('infer', 'verb', 'to figure something out from clues', 'нөхцөлөөс нь дүгнэх', 'From her tone, we can <b>infer</b> that she disagrees.')],
    'Science passage-д хамгийн их гардаг үгс.'))

P.append(group(2, 'Зохиогчийн', 'байр суурь', '1f5e3', [
    ('contend', 'verb', 'to argue or claim', 'гэж баталж маргах', 'The author <b>contends</b> that cities need more trees.'),
    ('concede', 'verb', 'to admit something, often unwillingly', 'хүлээн зөвшөөрөх', 'She <b>concedes</b> that the study was small.'),
    ('advocate', 'verb', 'to publicly support an idea', 'дэмжин сурталчлах', 'Many doctors <b>advocate</b> more sleep for teens.'),
    ('dismiss', 'verb', 'to treat as not important', 'ач холбогдолгүй гэж үзэх', 'Critics <b>dismissed</b> the idea at first.')],
    '<b>concede</b> = “тийм ээ, гэхдээ...” гэсэн өнгө аяс.'))

P.append(group(3, 'Өөрчлөлт', 'ба нөлөө', '1f4c9', [
    ('mitigate', 'verb', 'to make less severe', 'зөөлрүүлэх, багасгах', 'Trees can <b>mitigate</b> the effects of heat waves.'),
    ('alleviate', 'verb', 'to make a problem or pain easier', 'хөнгөвчлөх', 'The new bus line <b>alleviated</b> traffic.'),
    ('impede', 'verb', 'to slow down or block', 'саад болох', 'Heavy snow <b>impeded</b> the rescue team.'),
    ('foster', 'verb', 'to help something grow or develop', 'дэмжиж хөгжүүлэх', 'Group projects <b>foster</b> teamwork.')],
    '<b>mitigate</b> ба <b>alleviate</b> ойролцоо утгатай: хоёулаа “багасгах”.'))

P.append(group(4, 'Үнэлгээний', 'үгс', '2696', [
    ('negligible', 'adj.', 'so small that it does not matter', 'өчүүхэн, тооцохгүй', 'The price change was <b>negligible</b>: one cent.'),
    ('robust', 'adj.', 'strong and reliable', 'бат бөх, найдвартай', 'The results were <b>robust</b> in all five tests.'),
    ('plausible', 'adj.', 'seeming reasonable or likely', 'үнэмшилтэй', 'Both explanations are <b>plausible</b>.'),
    ('novel', 'adj.', 'new and original', 'шинэлэг (роман биш!)', 'The team found a <b>novel</b> way to recycle plastic.')],
    'Урхи: SAT-д <b>novel</b> ихэвчлэн “шинэлэг” гэсэн утгатай.'))

# 7 QUIZ
ch = [('A', 'fostered'), ('B', 'refuted'), ('C', 'corroborated'), ('D', 'mitigated')]
chh = '<div class="grid" style="gap:16px">' + ''.join(f'<div class="card" style="padding:18px 22px;display:flex;align-items:center;gap:16px;font-size:30px;font-weight:700;box-shadow:5px 5px 0 {INK}"><span style="flex:none;width:48px;height:48px;border:3px solid {INK};border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:24px;font-weight:800">{l}</span>{t}</div>' for l, t in ch) + '</div>'
P.append((f'<div style="display:flex;align-items:center;justify-content:space-between"><div><div class="pill">ШАЛГААД ҮЗ</div><h1 style="margin-top:16px">Аль үг<br><em>тохирох вэ?</em></h1></div>{E("1f914",180,"wig")}</div>'
          f'<div class="card" style="font-family:S,serif;font-size:36px;line-height:1.45">The new data did not support the old theory; in fact, the data ______ it completely.</div>' + chh +
          f'<div class="take">{E("1f447",46)}<div>Хариугаа <b>комментод</b> бичээрэй!</div></div>'
          f'<div style="text-align:center;font-size:22px;font-weight:700;opacity:.6;transform:rotate(180deg)">Хариу: B) refuted</div>', ''))

# 8 END
P.append((end_page(AC, SOFT, 'Өдөрт 20 үг,', 'сард 600 үг', 'GMP Vocab Hub-д <b>3,717 үг</b> англи тайлбар, жишээтэйгээ бэлэн.',
                   sched_cell('АНГЛИ (R&amp;W)', 'Мя · Пү · Бя', AC) + sched_cell('MATH', 'Да · Лх · Ба', AC, True),
                   [('1f4da', '3,717 үгтэй Vocab Hub'), ('1f4dd', 'Долоо хоног бүр сорил'), ('1f331', 'Үнэгүй түвшин тогтоох тест')]), ''))

if __name__ == '__main__':
    render(C, P, HERE / 'out19', 'GMP-SAT-Vocab', video_first=True)
