"""GMP mascot 'Saraa' (working name): modern flat-vector teen student, real GMP round logo on hoodie.
Writes char.svg (static, animatable groups). Animation is done with CSS in the page that embeds it."""
import base64

LOGO = 'data:image/png;base64,' + base64.b64encode(open('/home/claude/mascot/gmp-round.png', 'rb').read()).decode()

SKIN, SKIN_D, SKIN_L = '#f3c9a2', '#e2ad84', '#f9dcc0'
HAIR, HAIR_L = '#1c1830', '#3a3358'
NAVY, NAVY_D, NAVY_L = '#16285e', '#0d1a42', '#24398a'
GOLD, GOLD_D = '#f2a51f', '#d4860c'


def svg(mood='happy'):
    mouth = ('<path d="M366,430 C380,462 420,462 434,430 Z" fill="#7a2233"/>'
             '<path d="M370,431 C385,440 415,440 430,431 L430,434 C415,442 385,442 370,434Z" fill="#fff"/>'
             '<path d="M384,452 C394,446 406,446 416,452 C408,458 392,458 384,452Z" fill="#e2687a"/>') if mood == 'happy' else \
            '<path d="M372,436 C388,446 412,446 428,436" stroke="#7a2233" stroke-width="7" fill="none" stroke-linecap="round"/>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 1000" width="840" height="1000">
<defs>
 <linearGradient id="hood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{NAVY_L}"/><stop offset=".55" stop-color="{NAVY}"/><stop offset="1" stop-color="{NAVY_D}"/></linearGradient>
 <linearGradient id="sleeve" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="{NAVY}"/><stop offset="1" stop-color="{NAVY_L}"/></linearGradient>
 <radialGradient id="face" cx=".45" cy=".4" r=".7"><stop offset="0" stop-color="{SKIN_L}"/><stop offset=".7" stop-color="{SKIN}"/><stop offset="1" stop-color="{SKIN_D}"/></radialGradient>
 <linearGradient id="hair" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{HAIR_L}"/><stop offset=".6" stop-color="{HAIR}"/></linearGradient>
 <radialGradient id="iris" cx=".5" cy=".4" r=".6"><stop offset="0" stop-color="#6b4a2e"/><stop offset="1" stop-color="#241a2e"/></radialGradient>
 <clipPath id="lc"><circle cx="400" cy="770" r="78"/></clipPath>
 <filter id="soft" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#0d1a42" flood-opacity=".28"/></filter>
</defs>
<g id="all" filter="url(#soft)">
 <g id="pony">
  <path d="M452,178 C545,118 655,150 662,268 C668,352 628,414 596,446 C612,372 602,306 566,258 C536,220 500,204 468,200Z" fill="url(#hair)"/>
  <path d="M520,170 C580,170 630,210 640,280" stroke="{HAIR_L}" stroke-width="6" fill="none" stroke-linecap="round" opacity=".7"/>
 </g>
 <g id="body">
  <path d="M244,610 C228,548 286,500 348,506 L452,506 C514,500 572,548 556,610Z" fill="{NAVY}"/>
  <path d="M300,540 C330,512 470,512 500,540" stroke="{NAVY_D}" stroke-width="5" fill="none" opacity=".5"/>
  <path d="M400,530 C330,530 262,548 222,592 C186,632 178,720 176,1000 L624,1000 C622,720 614,632 578,592 C538,548 470,530 400,530Z" fill="url(#hood)"/>
  <path d="M400,560 L400,1000" stroke="{NAVY_D}" stroke-width="3" opacity=".35"/>
  <path d="M232,905 C300,880 500,880 568,905 L580,1000 L220,1000Z" fill="{NAVY_D}" opacity=".35"/>
  <rect x="368" y="470" width="64" height="80" rx="28" fill="{SKIN_D}"/>
  <path d="M296,552 C322,516 478,516 504,552 C478,596 322,596 296,552Z" fill="{NAVY_L}"/>
  <path d="M334,546 C362,580 438,580 466,546 C448,566 352,566 334,546Z" fill="{NAVY_D}"/>
  <path d="M372,580 C368,620 364,650 360,680" stroke="{GOLD}" stroke-width="7" fill="none" stroke-linecap="round"/>
  <path d="M428,580 C432,620 436,650 440,680" stroke="{GOLD}" stroke-width="7" fill="none" stroke-linecap="round"/>
  <rect x="352" y="676" width="16" height="26" rx="6" fill="{GOLD_D}"/><rect x="432" y="676" width="16" height="26" rx="6" fill="{GOLD_D}"/>
  <circle cx="400" cy="770" r="86" fill="#ffffff"/>
  <image href="{LOGO}" x="322" y="692" width="156" height="156" clip-path="url(#lc)"/>
 </g>
 <g id="arm">
  <path d="M572,598 C632,592 686,560 706,502 L768,524 C752,606 690,680 600,700Z" fill="url(#sleeve)"/>
  <path d="M706,500 L770,524 L760,552 L697,528Z" fill="{GOLD}"/>
  <g id="hand">
   <path d="M694,446 C690,424 708,414 728,416 L762,416 C784,416 794,434 792,456 L790,490 C788,510 772,520 752,518 L716,516 C698,514 690,500 692,484Z" fill="{SKIN}"/>
   <path d="M760,440 C774,440 786,444 790,452 M762,464 C776,464 788,468 791,476 M758,488 C772,488 784,492 788,500" stroke="{SKIN_D}" stroke-width="4" fill="none" stroke-linecap="round"/>
   <rect x="704" y="336" width="44" height="106" rx="22" fill="{SKIN}" transform="rotate(-8 728 430)"/>
   <path d="M716,350 C722,342 738,342 744,350" stroke="{SKIN_L}" stroke-width="5" fill="none" stroke-linecap="round" transform="rotate(-8 728 430)"/>
  </g>
 </g>
 <g id="head">
  <ellipse cx="250" cy="350" rx="22" ry="32" fill="{SKIN_D}"/><ellipse cx="550" cy="350" rx="22" ry="32" fill="{SKIN_D}"/>
  <circle cx="250" cy="380" r="7" fill="{GOLD}"/><circle cx="550" cy="380" r="7" fill="{GOLD}"/>
  <path d="M252,322 C252,222 320,172 400,172 C480,172 548,222 548,322 C548,420 488,492 400,496 C312,492 252,420 252,322Z" fill="url(#face)"/>
  <path d="M232,362 C220,200 300,132 400,132 C500,132 580,200 568,362 C560,300 548,250 520,222 C480,196 320,196 280,222 C252,250 240,300 232,362Z" fill="url(#hair)"/>
  <path d="M254,312 C266,224 338,186 424,190 C494,194 538,232 550,306 C516,258 470,240 428,244 C386,266 324,284 254,312Z" fill="url(#hair)"/>
  <path d="M300,232 C340,205 400,196 450,204" stroke="{HAIR_L}" stroke-width="7" fill="none" stroke-linecap="round" opacity=".8"/>
  <path d="M256,300 C240,360 246,420 270,452 C262,400 266,350 280,310Z" fill="url(#hair)"/>
  <path d="M544,300 C560,360 554,420 530,452 C538,400 534,350 520,310Z" fill="url(#hair)"/>
  <circle cx="462" cy="172" r="14" fill="{GOLD}"/>
  <path d="M312,296 C328,286 352,286 368,294" stroke="{HAIR}" stroke-width="8" fill="none" stroke-linecap="round"/>
  <path d="M432,294 C448,286 472,286 488,296" stroke="{HAIR}" stroke-width="8" fill="none" stroke-linecap="round"/>
  <g id="eyes">
   <ellipse cx="342" cy="350" rx="25" ry="31" fill="url(#iris)"/><ellipse cx="458" cy="350" rx="25" ry="31" fill="url(#iris)"/>
   <circle cx="351" cy="338" r="9" fill="#fff"/><circle cx="467" cy="338" r="9" fill="#fff"/>
   <circle cx="334" cy="362" r="4" fill="#fff" opacity=".8"/><circle cx="450" cy="362" r="4" fill="#fff" opacity=".8"/>
  </g>
  <circle cx="342" cy="350" r="50" fill="#ffffff" fill-opacity=".08" stroke="{GOLD_D}" stroke-width="6"/>
  <circle cx="458" cy="350" r="50" fill="#ffffff" fill-opacity=".08" stroke="{GOLD_D}" stroke-width="6"/>
  <path d="M392,346 C396,338 404,338 408,346" stroke="{GOLD_D}" stroke-width="6" fill="none"/>
  <path d="M292,340 L262,330 M508,340 L538,330" stroke="{GOLD_D}" stroke-width="5" stroke-linecap="round"/>
  <path d="M396,392 C392,404 398,410 406,408" stroke="{SKIN_D}" stroke-width="5" fill="none" stroke-linecap="round"/>
  <ellipse cx="306" cy="414" rx="26" ry="14" fill="#f08a8a" opacity=".35"/><ellipse cx="494" cy="414" rx="26" ry="14" fill="#f08a8a" opacity=".35"/>
  {mouth}
 </g>
</g>
</svg>'''


if __name__ == '__main__':
    open('/home/claude/mascot/char.svg', 'w').write(svg())
    import subprocess
    subprocess.run(['python3', '-c', '''
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":840,"height":1000})
    pg.goto("file:///home/claude/mascot/char.svg"); pg.screenshot(path="/home/claude/mascot/char.png", omit_background=True); b.close()
'''])
    print('ok')
