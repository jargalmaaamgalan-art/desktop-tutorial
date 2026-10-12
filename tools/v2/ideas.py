import chars
from logomas import T,G,logo_mark,nest
def inner(svg): return svg.split('>',1)[1].rsplit('</svg>',1)[0]
BOOK=f'<path d="M50 330 Q120 280 200 340 Q280 280 350 330 L335 375 Q270 335 200 385 Q130 335 65 375Z" fill="{G}" stroke="{T}" stroke-width="6" stroke-linejoin="round"/><path d="M200 340 V385" stroke="{T}" stroke-width="5"/>'
GL='<g fill="none" stroke="{c}" stroke-width="7"><circle cx="200" cy="160" r="135"/><ellipse cx="200" cy="160" rx="62" ry="135"/><path d="M200 25 V295"/><path d="M75 110 Q200 150 325 110"/><path d="M75 215 Q200 255 325 215"/></g>'
def wrap(w,h,body): return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}">{body}</svg>'
def A(word):  # stand on the book, globe backdrop
    kid=chars.kid(chars.CAST[word],'sun')
    return wrap(520,440,f'<g transform="translate(60,-10) scale(1.1)">{GL.format(c=T+"55")}</g><circle cx="260" cy="150" r="148" fill="{T}" opacity=".08"/>'
        +f'<g transform="translate(50,-12) scale(1.1)" >{BOOK}</g>'+nest(kid,110,20,300))
def B(word):  # flag
    kid=chars.kid(chars.CAST[word],'out')
    flag=(f'<path d="M395 90 V400" stroke="#6b4a2b" stroke-width="10" stroke-linecap="round"/><path d="M398 92 H500 V215 L448 190 L398 215Z" fill="{T}" stroke="#fff" stroke-width="5"/>'
          f'<g transform="translate(414,104) scale(.17)">{inner(logo_mark(face=False,arms=None))}</g><text x="448" y="190" text-anchor="middle" font:="" font-size="16" font-weight="900" fill="{G}" font-family="Arial Black">GMP</text>')
    return wrap(520,440,nest(kid,20,60,340)+flag)
def C(word):  # circular badge, kid pops out
    kid=chars.kid(chars.CAST[word],'happy')
    ring=(f'<circle cx="260" cy="250" r="190" fill="{T}"/><circle cx="260" cy="250" r="172" fill="none" stroke="{G}" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>'
          f'<g transform="translate(60,70) scale(.8)" opacity=".28">{GL.format(c="#fff")}</g>')
    book=f'<g transform="translate(150,330) scale(.55)">{BOOK}</g>'
    return wrap(520,440,ring+nest(kid,110,20,300)+book+f'<rect x="170" y="395" width="180" height="36" rx="18" fill="{G}"/><text x="260" y="421" text-anchor="middle" font-size="22" font-weight="900" fill="{T}" font-family="Arial Black" letter-spacing="3">GMP CREW</text>')
def D(word):  # lanyard + stamp
    sp=dict(chars.CAST[word]); kid=chars.kid(sp,'flex')
    lan=(f'<path d="M165 255 L200 330 L235 255" stroke="{T}" stroke-width="12" fill="none"/>'
         f'<rect x="168" y="325" width="64" height="80" rx="8" fill="#fff" stroke="{T}" stroke-width="5"/><g transform="translate(176,330) scale(.19)">{inner(logo_mark(face=False,arms=None))}</g><rect x="176" y="378" width="48" height="8" fill="{G}"/><rect x="176" y="392" width="34" height="5" fill="{T}"/>')
    kidsvg=kid
    stamp=(f'<g transform="rotate(-14 410 120)"><circle cx="410" cy="120" r="70" fill="none" stroke="{T}" stroke-width="7"/><circle cx="410" cy="120" r="58" fill="none" stroke="{T}" stroke-width="3"/><text x="410" y="112" text-anchor="middle" font-size="22" font-weight="900" fill="{T}" font-family="Arial Black">GMP</text><text x="410" y="140" text-anchor="middle" font-size="17" font-weight="900" fill="{G}" stroke="{T}" stroke-width=".6" font-family="Arial Black">APPROVED</text></g>')
    k=nest(kidsvg,20,60,340)
    # lanyard drawn in kid-svg coordinates: scale 340/420
    s=340/420
    return wrap(520,440,k+f'<g transform="translate({20+10*s},{60+10*s}) scale({s})">{lan}</g>'+stamp)
if __name__=='__main__':
    jobs=[('A  Kid on the gold book, globe behind',A,'DRAW'),('B  Kid carries the GMP flag',B,'HOLD'),('C  GMP CREW round badge',C,'TRACE'),('D  Lanyard ID card + GMP APPROVED stamp',D,'ACCOUNT')]
    cells=''.join(f'<div style="background:#fbf6ec;border-radius:20px;padding:8px;text-align:center;font:700 22px Arial">{f(w)}<div>{t}</div></div>' for t,f,w in jobs)
    open('/home/claude/preview/ideas.html','w').write(f'<body style="margin:0;background:#dfe7ee;width:1150px"><div style="display:grid;grid-template-columns:repeat(2,560px);gap:12px;padding:12px">{cells}</div>')
