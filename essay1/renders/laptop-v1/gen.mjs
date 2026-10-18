// Laptop exploded figure for the film prototype (SEQ 10).
// Uses the anatomy iso-kit. Emits film.html with per-part <g> groups,
// embedded label anchors, and a window.seek(t) driver (0..20s).
import { writeFileSync } from "node:fs";
import * as k from "/root/gcomedy/essay1/tools/anatomy/kit/iso-kit.mjs";

const SCALE = 3.2;
const W = 1280, H = 720;

const PARTS = [
  { id: "case",    plan: { x: -60, y: -40, w: 120, d: 80, r: 6 }, z: 0,  h: 8, lift: 0 },
  { id: "battery", plan: { x: -50, y: 8, w: 100, d: 24, r: 3 },   z: 8,  h: 4, lift: 26 },
  { id: "board",   plan: { x: -50, y: -32, w: 100, d: 56, r: 2 }, z: 8,  h: 2, lift: 52 },
  { id: "chip1",   plan: { x: -40, y: -24, w: 14, d: 14, r: 1 },  z: 10, h: 2, lift: 60 },
  { id: "chip2",   plan: { x: -20, y: -24, w: 10, d: 10, r: 1 },  z: 10, h: 2, lift: 62 },
  { id: "chip3",   plan: { x: 0, y: -24, w: 18, d: 12, r: 1 },    z: 10, h: 2, lift: 64 },
  { id: "deck",    plan: { x: -58, y: -38, w: 116, d: 76, r: 5 }, z: 10, h: 2, lift: 78 },
  { id: "screen",  plan: { x: -60, y: -46, w: 120, d: 5, r: 1 },  z: 8,  h: 74, lift: 108 },
];

// keys: 4 rows x 10 on the deck front half
const KEYS = [];
for (let r = 0; r < 4; r++)
  for (let c = 0; c < 10; c++)
    KEYS.push({ id: `key-${r}-${c}`, plan: { x: -50 + c * 10.4, y: -30 + r * 9, w: 8.4, d: 6.4, r: 1 }, z: 12, h: 1.6, lift: 104 + r * 3 });

const ALL = [...PARTS, ...KEYS];

// fit projection over closed + exploded corners
const corners = [];
for (const p of ALL) {
  corners.push(...k.boxCorners(p.plan, p.z, p.z + 2));
  corners.push(...k.boxCorners(p.plan, p.z + p.lift, p.z + p.lift + 2));
}
const P = k.fitProjection(corners, W, H, { pad: 120, headroom: 130 });
const iso = ([x, y, z]) => k.iso([x, y, z], P);
// screen dy per world dz (for JS lift animation): dy/dz = -cosE * scale * UNIT
const DZ = -Math.cos(30 * Math.PI / 180) * P.scale * Math.sqrt(1.6);

function partSVG(p) {
  const s = k.slabOf(p.plan, p.z, p.h, P);
  let out = `<g class="lp" id="p-${p.id}" data-lift="${p.lift}">`;
  out += `<path class="f" d="${s.fill}"/>`;
  s.shades.forEach((d, i) => { if (d) out += `<path class="sh sh${i}" d="${d}"/>`; });
  out += `<path class="tp" d="${s.top}"/>`;
  if (s.outline) out += `<path class="ol" d="${s.outline}"/>`;
  if (s.crease) out += `<path class="cr" d="${s.crease}"/>`;
  return out + `</g>`;
}

// bounds not needed — projection is pre-fitted to screen px.
// label anchors (world → screen px) at exploded positions
const LABELS = [
  ["screen", "display", -60, -43.5, 8 + 74 + 132],
  ["keys", "keyboard", 50, -30, 12 + 1.6 + 113],
  ["deck", "top case", 58, 0, 10 + 2 + 78],
  ["board", "logic board", -50, -32, 8 + 2 + 52],
  ["battery", "battery", 50, 20, 8 + 4 + 26],
  ["case", "bottom case", -60, 40, 0],
].map(([id, text, x, y, z]) => {
  const [wx, wy] = iso([x, y, z]);
  return { id, text, x: wx.toFixed(1), y: wy.toFixed(1) };
});

const svg = `<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}">` +
  ALL.map(partSVG).join("") + `</svg>`;

const labels = LABELS.map(l =>
  `<div class="lbl" id="lbl-${l.id}" data-x="${l.x}" data-y="${l.y}"><span>${l.text}</span></div>`).join("");

const html = `<!DOCTYPE html><html><head><meta charset="utf-8"><style>
html,body{margin:0;width:${W}px;height:${H}px;background:#07070a;overflow:hidden}
#stage{position:absolute;inset:0}
svg{position:absolute;inset:0}
.f{fill:#1a1a22}.sh0{fill:#23232d}.sh1{fill:#2b2b36}.sh2{fill:#34343f}.sh3{fill:#3f3f4b}
.tp{fill:#2e2e38}.ol{fill:none;stroke:#45454f;stroke-width:.8px;vector-effect:non-scaling-stroke}
.cr{fill:none;stroke:#45454f;stroke-width:.5px;vector-effect:non-scaling-stroke;opacity:.6}
#p-screen .f{fill:#101018}#p-screen .tp{fill:#16161f}
#p-chip1 .tp,#p-chip2 .tp,#p-chip3 .tp{fill:#7a1020}
#p-battery .tp{fill:#2b1d06}
.lp{transition:none}
#ghost .lp{opacity:1}
h1{position:absolute;top:70px;width:100%;text-align:center;color:#f3f1ec;font:700 84px 'Inter Tight',system-ui,sans-serif;margin:0;letter-spacing:.01em}
h1 b{color:#e8102e}
#word{position:absolute;top:300px;width:100%;text-align:center;color:#f3f1ec;font:400 120px Anton,Impact,sans-serif;margin:0;letter-spacing:.06em;opacity:0;text-shadow:0 0 60px rgba(232,16,46,.45)}
.lbl{position:absolute;transform:translate(-50%,-50%);opacity:0;font:500 22px 'Inter Tight',system-ui,sans-serif;color:#f5c76b;white-space:nowrap}
.lbl span{border-left:2px solid #f5c76b;padding-left:10px}
</style></head><body><div id="stage">
${svg}
<h1 id="title">where is the <b>laptop</b>?</h1>
<div id="word">laptop</div>
${labels}
</div><script>
var DZ=${DZ};
var SCALE=${SCALE};
window.seek=function(t){
  function e(a,b){return Math.min(1,Math.max(0,(t-a)/(b-a)));}
  var open=e(3,5), wave=e(5,11), lab=e(11,15), ghost=e(15,18), back=e(18,20);
  var ex = wave<1 ? wave : (1-back);
  // staggered wave: each part ramps within the wave window
  document.querySelectorAll('.lp').forEach(function(g){
    var lift=parseFloat(g.dataset.lift);
    var start=lift/140, local=Math.min(1,Math.max(0,(ex-start)/(1-start+0.001)));
    var dy=lift*local*DZ;
    // screen opens first
    if(g.id==='p-screen') dy=132*open*DZ;
    g.setAttribute('transform','translate(0,'+dy.toFixed(1)+')');
    g.style.opacity = ghost<1 ? 1 : (1-ghost*0.82);
  });
  document.getElementById('title').style.opacity = t<0.5 ? t/0.5 : (back>0 ? 1-back : 1);
  document.getElementById('word').style.opacity = ghost*(1-back*0.3);
  document.querySelectorAll('.lbl').forEach(function(l){
    l.style.left=l.dataset.x+'px'; l.style.top=l.dataset.y+'px';
    l.style.opacity = (lab*(1-back)).toFixed(2);
  });
};
</script></body></html>`;

writeFileSync("/tmp/laptop_seq/film.html", html);
console.log("wrote film.html, parts:", ALL.length, "labels:", LABELS.length);
