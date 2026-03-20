import cairosvg

# Normal mole SVG
normal_svg = '''<svg viewBox="0 0 100 150" width="300" height="450" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="bodyG" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#A0714B"/>
      <stop offset="100%" stop-color="#6B3D18"/>
    </radialGradient>
    <radialGradient id="faceG" cx="38%" cy="32%" r="65%">
      <stop offset="0%" stop-color="#FDEBD0"/>
      <stop offset="60%" stop-color="#F5C78A"/>
      <stop offset="100%" stop-color="#E8A056"/>
    </radialGradient>
    <radialGradient id="earInG" cx="40%" cy="35%" r="60%">
      <stop offset="0%" stop-color="#FFBFA0"/>
      <stop offset="100%" stop-color="#F0846A"/>
    </radialGradient>
  </defs>
  <path d="M 18 150 C 18 82, 82 82, 82 150 Z" fill="url(#bodyG)"/>
  <ellipse cx="12" cy="100" rx="13" ry="8" fill="#C8875A" transform="rotate(-20,12,100)"/>
  <ellipse cx="88" cy="100" rx="13" ry="8" fill="#C8875A" transform="rotate(20,88,100)"/>
  <ellipse cx="2"  cy="96" rx="3.2" ry="4" fill="#A06030" transform="rotate(-20,2,96)"/>
  <ellipse cx="7"  cy="93" rx="3.2" ry="4" fill="#A06030" transform="rotate(-20,7,93)"/>
  <ellipse cx="13" cy="92" rx="3.2" ry="4" fill="#A06030" transform="rotate(-20,13,92)"/>
  <ellipse cx="98" cy="96" rx="3.2" ry="4" fill="#A06030" transform="rotate(20,98,96)"/>
  <ellipse cx="93" cy="93" rx="3.2" ry="4" fill="#A06030" transform="rotate(20,93,93)"/>
  <ellipse cx="87" cy="92" rx="3.2" ry="4" fill="#A06030" transform="rotate(20,87,92)"/>
  <circle cx="50" cy="50" r="44" fill="url(#faceG)" stroke="#D4894A" stroke-width="2.5"/>
  <circle cx="17" cy="14" r="14" fill="#C8845A"/>
  <circle cx="83" cy="14" r="14" fill="#C8845A"/>
  <circle cx="17" cy="14" r="9"  fill="url(#earInG)"/>
  <circle cx="83" cy="14" r="9"  fill="url(#earInG)"/>
  <ellipse cx="32" cy="26" rx="10" ry="11" fill="white"/>
  <ellipse cx="68" cy="26" rx="10" ry="11" fill="white"/>
  <circle  cx="34" cy="28" r="7.5" fill="#1C1008"/>
  <circle  cx="70" cy="28" r="7.5" fill="#1C1008"/>
  <circle cx="38" cy="22" r="3"   fill="white"/>
  <circle cx="74" cy="22" r="3"   fill="white"/>
  <circle cx="32" cy="31" r="1.4" fill="white" opacity=".55"/>
  <circle cx="68" cy="31" r="1.4" fill="white" opacity=".55"/>
  <ellipse cx="50" cy="41" rx="5.5" ry="4.5" fill="#E06870"/>
  <ellipse cx="50" cy="39.5" rx="3.5" ry="2.5" fill="#F09090"/>
  <text x="50" y="70" font-family="sans-serif" font-size="36" font-weight="bold"
        fill="#CC2200" text-anchor="middle">ㄅ</text>
  <path d="M 40 78 Q 50 87 60 78" stroke="#B04030" stroke-width="2.2" fill="none" stroke-linecap="round"/>
  <ellipse cx="15" cy="57" rx="11" ry="8" fill="#FF7070" opacity=".22"/>
  <ellipse cx="85" cy="57" rx="11" ry="8" fill="#FF7070" opacity=".22"/>
  <line x1="4"  y1="50" x2="33" y2="55" stroke="#B07840" stroke-width="1.1" opacity=".4" stroke-linecap="round"/>
  <line x1="4"  y1="58" x2="33" y2="59" stroke="#B07840" stroke-width="1.1" opacity=".4" stroke-linecap="round"/>
  <line x1="96" y1="50" x2="67" y2="55" stroke="#B07840" stroke-width="1.1" opacity=".4" stroke-linecap="round"/>
  <line x1="96" y1="58" x2="67" y2="59" stroke="#B07840" stroke-width="1.1" opacity=".4" stroke-linecap="round"/>
</svg>'''

# Hit mole SVG
hit_svg = '''<svg viewBox="0 0 100 150" width="300" height="450" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="bodyG2" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#A0714B"/>
      <stop offset="100%" stop-color="#6B3D18"/>
    </radialGradient>
    <radialGradient id="faceG2" cx="38%" cy="32%" r="65%">
      <stop offset="0%" stop-color="#E8FFE0"/>
      <stop offset="60%" stop-color="#C8F0A0"/>
      <stop offset="100%" stop-color="#8DC858"/>
    </radialGradient>
  </defs>
  <path d="M 18 150 C 18 82, 82 82, 82 150 Z" fill="url(#bodyG2)"/>
  <ellipse cx="12" cy="100" rx="13" ry="8" fill="#C8875A" transform="rotate(-20,12,100)"/>
  <ellipse cx="88" cy="100" rx="13" ry="8" fill="#C8875A" transform="rotate(20,88,100)"/>
  <circle cx="50" cy="50" r="44" fill="url(#faceG2)" stroke="#5CB840" stroke-width="3"/>
  <circle cx="17" cy="14" r="14" fill="#C8845A"/>
  <circle cx="83" cy="14" r="14" fill="#C8845A"/>
  <circle cx="17" cy="14" r="9"  fill="#FFBFA0"/>
  <circle cx="83" cy="14" r="9"  fill="#FFBFA0"/>
  <path d="M 23 28 Q 32 20 41 28" stroke="#1C1008" stroke-width="3.5" fill="none" stroke-linecap="round"/>
  <path d="M 59 28 Q 68 20 77 28" stroke="#1C1008" stroke-width="3.5" fill="none" stroke-linecap="round"/>
  <ellipse cx="50" cy="41" rx="5.5" ry="4.5" fill="#E06870"/>
  <text x="50" y="70" font-family="sans-serif" font-size="36" font-weight="bold"
        fill="#3A9020" text-anchor="middle">ㄅ</text>
  <path d="M 36 78 Q 50 90 64 78" stroke="#2A7010" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <ellipse cx="15" cy="57" rx="11" ry="8" fill="#FF7070" opacity=".22"/>
  <ellipse cx="85" cy="57" rx="11" ry="8" fill="#FF7070" opacity=".22"/>
</svg>'''

cairosvg.svg2png(bytestring=normal_svg.encode(), write_to='/home/user/my-docusaurus/mole_normal.png', scale=2)
cairosvg.svg2png(bytestring=hit_svg.encode(), write_to='/home/user/my-docusaurus/mole_hit.png', scale=2)
print("done")
