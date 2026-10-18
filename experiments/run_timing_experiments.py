#!/usr/bin/env python3
"""
First-principles experiments on the timing-is-composition thesis.

Hypotheses (from THESIS-timing-is-composition.md):

H1 (DPV temporal signature at laughs):
  Measured laughs are preceded by longer-than-baseline pauses.
  The laugh fires at the temporal violation.

H2 (Speech-rate drop before laughs):
  Speech rate in the 2s before a laugh is slower than baseline.
  The punch is a "held note" — the tempo drops, then recovers.

H3 (Punch slower or faster? Norrick vs DPV):
  Two competing predictions:
  - Norrick 2001: punch delivered FASTER than setup.
  - DPV 2026:   punch preceded by EXTENDED pause (slower approach).
  Test both on Louis Road Rage + Norm Moth measured punch candidates.

H4 (Content coupling, paper-scored n=29,617):
  benign_violation (the BV sweet spot) correlates with the
  product incongruity × surprise more than with either alone.
  Coupling predicts punch_pos.

H5 (Punch compression — Seinfeld's syllable-shaving):
  Punch candidates have fewer syllables per word / are more
  compressed than their setups, in text-based bit analysis.

Data:
- Measured timing: characters2/theory/scribe/ word-level + laugh timestamps
- Punch candidates: characters2/theory/analysis/*.json
- Paper scores: characters2/theory/transcripts/bits_theory.json
- Bit text: characters2/theory/transcripts/bits_annotated/
"""

import json, math, glob, os, statistics, random
from collections import defaultdict

random.seed(42)
SCRIBE = "/root/characters2/theory/scribe"
ANALYSIS = "/root/characters2/theory/analysis"
BITS_THEORY = "/root/characters2/theory/transcripts/bits_theory.json"
BITS_ANN = "/root/characters2/theory/transcripts/bits_annotated"

results = {}

# ---------- helpers ----------

def word_gaps(words):
    """Gaps between consecutive word-type words (silences)."""
    ws = [w for w in words if w.get("type") == "word"]
    gaps = []
    for i in range(len(ws) - 1):
        gap = ws[i + 1]["start"] - ws[i]["end"]
        gaps.append((ws[i]["end"], gap))  # (gap_onset_time, gap_duration)
    return ws, gaps

def speech_rate(words, t0, t1):
    """Syllables per second in window [t0,t1] (approx: words/sec * 1.5)."""
    ws = [w for w in words if w.get("type") == "word" and t0 <= w["start"] < t1]
    if not ws:
        return None
    # approximate syllables: 1.5 per English word
    duration = t1 - t0
    if duration <= 0:
        return None
    return (len(ws) * 1.5) / duration

def nearest_gap(gaps, t, window=3.0):
    """Largest gap within window of time t (the pause just before t)."""
    candidates = [(abs(g[0] - t), g[1]) for g in gaps if 0 <= t - g[0] <= window]
    if not candidates:
        return None
    return max(candidates, key=lambda x: x[1])[1]

# ---------- H1 + H2: laugh temporal signature (measured KT sets) ----------

print("=" * 70)
print("H1+H2: LAUGH TEMPORAL SIGNATURE (measured word-timing + laugh timestamps)")
print("=" * 70)

pairs = [
    ("kt728_jamesbond", 4),
    ("kt704_passport", 9),
    ("kt715_ep715", 14),
    ("kt715_walking", 6),
    ("kt728_diversifying", 11),
]

all_pauses_before_laugh = []
all_baseline_pauses = []
all_rate_drops = []
per_set = []

for name, _ in pairs:
    try:
        wd = json.load(open(f"{SCRIBE}/{name}.json"))
        ld = json.load(open(f"{SCRIBE}/{name}_laughs.json"))
    except Exception as e:
        print(f"  SKIP {name}: {e}")
        continue
    words = wd.get("words", [])
    laughs = [l["t"] for l in ld.get("laughs", []) if "t" in l]
    if len(words) < 20 or len(laughs) < 2:
        continue
    ws, gaps = word_gaps(words)
    if not gaps:
        continue
    baseline = [g[1] for g in gaps]
    # exclude gaps that are themselves right before a laugh (contaminated)
    laugh_times = set(round(l, 1) for l in laughs)
    clean_baseline = [g[1] for g in gaps
                      if not any(abs(g[0] - lt) < 0.3 for lt in laughs)]

    pauses_before = []
    rate_drops = []
    for lt in laughs:
        pg = nearest_gap(gaps, lt, window=2.0)
        if pg is not None:
            pauses_before.append(pg)
        # rate: 2s before vs 2s after
        r_pre = speech_rate(ws, lt - 2.0, lt)
        r_post = speech_rate(ws, lt, lt + 2.0)
        r_all = speech_rate(ws, ws[0]["start"], ws[-1]["end"])
        if r_pre is not None and r_post is not None and r_all is not None and r_all > 0:
            rate_drops.append((r_pre / r_all, r_post / r_all))

    all_pauses_before_laugh.extend(pauses_before)
    all_baseline_pauses.extend(clean_baseline)
    all_rate_drops.extend(rate_drops)

    if pauses_before and clean_baseline:
        mb = statistics.mean(pauses_before)
        mbase = statistics.mean(clean_baseline)
        per_set.append((name, len(laughs), mb, mbase))
        print(f"  {name:25s} laughs={len(laughs):2d}  "
              f"pause_before_laugh={mb:.3f}s  baseline={mbase:.3f}s  "
              f"ratio={mb/mbase:.2f}x")

if all_pauses_before_laugh and all_baseline_pauses:
    # permutation test: are pauses before laughs > baseline?
    obs = statistics.mean(all_pauses_before_laugh)
    base = statistics.mean(all_baseline_pauses)
    # bootstrap/permutation
    combined = all_pauses_before_laugh + all_baseline_pauses
    n_pre = len(all_pauses_before_laugh)
    null_diffs = []
    for _ in range(5000):
        random.shuffle(combined)
        null_diffs.append(statistics.mean(combined[:n_pre]) - statistics.mean(combined[n_pre:]))
    p_one_tail = sum(1 for d in null_diffs if d >= (obs - base)) / len(null_diffs)
    print(f"\n  POOLED: pause before laugh={obs:.3f}s  baseline={base:.3f}s  "
          f"diff={obs-base:+.3f}s")
    print(f"  permutation p (one-tail, H1: pause>baseline): {p_one_tail:.4f}")
    results["H1"] = {
        "n_laughs_with_pause": n_pre,
        "n_baseline_gaps": len(all_baseline_pauses),
        "mean_pause_before_laugh": round(obs, 4),
        "mean_baseline_pause": round(base, 4),
        "diff": round(obs - base, 4),
        "permutation_p_one_tail": round(p_one_tail, 4),
        "supported": p_one_tail < 0.05 and obs > base,
    }

if all_rate_drops:
    pre_ratios = [r[0] for r in all_rate_drops]
    post_ratios = [r[1] for r in all_rate_drops]
    mean_pre = statistics.mean(pre_ratios)
    mean_post = statistics.mean(post_ratios)
    # paired test: pre < post?
    diffs = [r[0] - r[1] for r in all_rate_drops]
    obs_d = statistics.mean(diffs)
    null_d = []
    d_copy = diffs[:]
    for _ in range(5000):
        signs = [random.choice([-1, 1]) for _ in d_copy]
        null_d.append(statistics.mean([s * d for s, d in zip(signs, d_copy)]))
    p_pre_slower = sum(1 for d in null_d if d <= obs_d) / len(null_d)
    print(f"\n  POOLED rate: pre-laugh={mean_pre:.3f}x baseline  "
          f"post-laugh={mean_post:.3f}x baseline")
    print(f"  sign-flip p (H2: pre slower than post): {p_pre_slower:.4f}")
    results["H2"] = {
        "n": len(all_rate_drops),
        "mean_rate_pre_over_baseline": round(mean_pre, 4),
        "mean_rate_post_over_baseline": round(mean_post, 4),
        "mean_diff_pre_minus_post": round(obs_d, 4),
        "sign_flip_p_one_tail": round(p_pre_slower, 4),
        "supported": p_pre_slower < 0.05 and obs_d < 0,
    }

# ---------- H3: punch slower or faster (Louis + Norm measured) ----------

print("\n" + "=" * 70)
print("H3: PUNCH RATE — Norrick (faster) vs DPV (extended pause)")
print("=" * 70)

h3_rows = []
for name in ["louis_roadrage", "norm_moth"]:
    try:
        ad = json.load(open(f"{ANALYSIS}/{name}.json"))
        wd = json.load(open(f"{SCRIBE}/{name}.json"))
    except Exception as e:
        print(f"  SKIP {name}: {e}")
        continue
    punches = ad.get("punch_candidates", [])
    words = wd.get("words", [])
    ws, gaps = word_gaps(words)
    if not punches or not ws:
        continue
    overall_rate = speech_rate(ws, ws[0]["start"], ws[-1]["end"])
    print(f"\n  {name}: {len(punches)} punch candidates, baseline rate={overall_rate:.2f} syl/s")
    for p in punches:
        t = p["t_start_s"]
        pb = p.get("pause_before_s", None)
        r_pre = speech_rate(ws, t - 1.5, t)
        r_post = speech_rate(ws, t, t + 1.5)
        row = {
            "set": name, "t": t, "pause_before": pb,
            "rate_pre": round(r_pre, 3) if r_pre else None,
            "rate_post": round(r_post, 3) if r_post else None,
            "rate_overall": round(overall_rate, 3),
            "fp": p.get("fingerprint", "")[:40],
        }
        h3_rows.append(row)
        print(f"    t={t:6.1f}  pause_before={pb:.2f}s  "
              f"pre={r_pre:.2f}  post={r_post:.2f}  "
              f"fingerprint={row['fp']}")

# Aggregate: is pause_before at punches > baseline mean pause?
all_pb = [r["pause_before"] for r in h3_rows if r["pause_before"] is not None]
if all_pb:
    # compare to the set's mean pause from analysis timing
    print(f"\n  punch pause_before: mean={statistics.mean(all_pb):.3f}s "
          f"median={statistics.median(all_pb):.3f}s max={max(all_pb):.3f}s")
    results["H3_pause"] = {
        "n_punches": len(all_pb),
        "mean_pause_before_punch": round(statistics.mean(all_pb), 4),
        "median_pause_before_punch": round(statistics.median(all_pb), 4),
        "note": "DPV predicts these pauses exceed setup baseline; Norrick predicts rate speed-up at punch",
    }

# rate_pre vs rate_post at punches
rp = [(r["rate_pre"], r["rate_post"]) for r in h3_rows
      if r["rate_pre"] and r["rate_post"]]
if rp:
    mean_pre = statistics.mean(x[0] for x in rp)
    mean_post = statistics.mean(x[1] for x in rp)
    # normalize by overall
    print(f"\n  rate at punches: pre={mean_pre:.2f}  post={mean_post:.2f}  "
          f"post/pre={mean_post/mean_pre:.2f}x")
    results["H3_rate"] = {
        "n": len(rp),
        "mean_rate_pre": round(mean_pre, 4),
        "mean_rate_post": round(mean_post, 4),
        "post_over_pre": round(mean_post / mean_pre, 4),
        "interpretation": "post>pre supports Norrick (punch accelerates); post<pre supports DPV-style deceleration",
    }

# ---------- H4: content coupling on paper scores ----------

print("\n" + "=" * 70)
print("H4: CONTENT COUPLING — BV sweet spot vs incongruity × surprise (n=29,617)")
print("=" * 70)

bt = json.load(open(BITS_THEORY))
rows = []
for k, v in bt.items():
    rows.append({
        "incongruity": v.get("incongruity", 0),
        "surprise": v.get("surprise", 0),
        "aab": v.get("aab", 0),
        "punch_pos": v.get("punch_pos", 0),
        "benign_violation": v.get("benign_violation", 0),
        "violation": v.get("violation", 0),
        "benign": v.get("benign", 0),
        "economy": v.get("economy", 0),
        "comic": v.get("comic", ""),
    })

def pearson(xs, ys):
    n = len(xs)
    if n < 3:
        return None
    mx, my = statistics.mean(xs), statistics.mean(ys)
    sx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    sy = math.sqrt(sum((y - my) ** 2 for y in ys))
    if sx == 0 or sy == 0:
        return None
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / n
    return cov / (sx / math.sqrt(n) * sy / math.sqrt(n))  # not used; use direct

def pearson_r(xs, ys):
    n = len(xs)
    if n < 3:
        return None
    mx, my = statistics.mean(xs), statistics.mean(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    denx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    deny = math.sqrt(sum((y - my) ** 2 for y in ys))
    if denx == 0 or deny == 0:
        return None
    return num / (denx * deny)

inc = [r["incongruity"] for r in rows]
sur = [r["surprise"] for r in rows]
prod = [i * s for i, s in zip(inc, sur)]
bv = [r["benign_violation"] for r in rows]
pp = [r["punch_pos"] for r in rows]

r_inc_bv = pearson_r(inc, bv)
r_sur_bv = pearson_r(sur, bv)
r_prod_bv = pearson_r(prod, bv)
r_inc_pp = pearson_r(inc, pp)
r_sur_pp = pearson_r(sur, pp)
r_prod_pp = pearson_r(prod, pp)

print(f"  corr(incongruity, BV)     = {r_inc_bv:+.4f}")
print(f"  corr(surprise, BV)        = {r_sur_bv:+.4f}")
print(f"  corr(incong×surprise, BV) = {r_prod_bv:+.4f}")
print(f"  corr(incongruity, punch_pos)     = {r_inc_pp:+.4f}")
print(f"  corr(surprise, punch_pos)        = {r_sur_pp:+.4f}")
print(f"  corr(incong×surprise, punch_pos) = {r_prod_pp:+.4f}")

# BV nonzero vs zero punch_pos
bv_pos = [r["punch_pos"] for r in rows if r["benign_violation"] > 0]
bv_zero = [r["punch_pos"] for r in rows if r["benign_violation"] == 0]
if bv_pos and bv_zero:
    print(f"  punch_pos | BV>0 (n={len(bv_pos)}): mean={statistics.mean(bv_pos):.4f}")
    print(f"  punch_pos | BV=0 (n={len(bv_zero)}): mean={statistics.mean(bv_zero):.4f}")

results["H4"] = {
    "n_bits": len(rows),
    "corr_incongruity_bv": round(r_inc_bv, 4) if r_inc_bv else None,
    "corr_surprise_bv": round(r_sur_bv, 4) if r_sur_bv else None,
    "corr_product_bv": round(r_prod_bv, 4) if r_prod_bv else None,
    "corr_incongruity_punch_pos": round(r_inc_pp, 4) if r_inc_pp else None,
    "corr_surprise_punch_pos": round(r_sur_pp, 4) if r_sur_pp else None,
    "corr_product_punch_pos": round(r_prod_pp, 4) if r_prod_pp else None,
    "punch_pos_mean_bv_positive": round(statistics.mean(bv_pos), 4) if bv_pos else None,
    "punch_pos_mean_bv_zero": round(statistics.mean(bv_zero), 4) if bv_zero else None,
    "caveat": "paper-scored labels, not measured timing/laughs",
}

# ---------- H5: punch compression (text-based, bits_annotated) ----------

print("\n" + "=" * 70)
print("H5: PUNCH COMPRESSION — setup vs punch syllable density")
print("=" * 70)

VOWELS = "aeiouy"

def count_syllables(word):
    w = word.lower().strip(".,!?;:'\"-()")
    if not w:
        return 0
    count = 0
    prev_vowel = False
    for ch in w:
        is_vowel = ch in VOWELS
        if is_vowel and not prev_vowel:
            count += 1
        prev_vowel = is_vowel
    # silent e
    if w.endswith("e") and count > 1:
        count -= 1
    return max(1, count)

def text_stats(text):
    words = [w for w in text.split() if any(c.isalpha() for c in w)]
    n_words = len(words)
    n_syll = sum(count_syllables(w) for w in words)
    return n_words, n_syll

setup_syll_per_word = []
punch_syll_per_word = []
setup_total = []
punch_total = []
n_compared = 0

for comic_dir in glob.glob(f"{BITS_ANN}/*"):
    for bf in glob.glob(f"{comic_dir}/*.bits.json")[:3]:  # limit files
        try:
            bd = json.load(open(bf))
        except Exception:
            continue
        for bit in bd.get("bits", []):
            setup = bit.get("setup") or ""
            punch = bit.get("punch_candidate") or ""
            if not setup or not punch:
                continue
            sw, ss = text_stats(setup)
            pw, ps = text_stats(punch)
            if sw < 3 or pw < 2:
                continue
            setup_syll_per_word.append(ss / sw)
            punch_syll_per_word.append(ps / pw)
            setup_total.append(ss)
            punch_total.append(ps)
            n_compared += 1

if n_compared > 100:
    m_spw = statistics.mean(setup_syll_per_word)
    m_ppw = statistics.mean(punch_syll_per_word)
    m_syll_s = statistics.mean(setup_total)
    m_syll_p = statistics.mean(punch_total)
    # paired: punch fewer syllables/word?
    diffs = [p - s for s, p in zip(setup_syll_per_word, punch_syll_per_word)]
    obs = statistics.mean(diffs)
    null = []
    d_copy = diffs[:]
    for _ in range(3000):
        signs = [random.choice([-1, 1]) for _ in d_copy]
        null.append(statistics.mean([s * d for s, d in zip(signs, d_copy)]))
    p_punch_less = sum(1 for d in null if d <= obs) / len(null)
    print(f"  n bits compared: {n_compared}")
    print(f"  syllables/word: setup={m_spw:.3f}  punch={m_ppw:.3f}  "
          f"diff={m_ppw-m_spw:+.3f}")
    print(f"  total syllables: setup={m_syll_s:.1f}  punch={m_syll_p:.1f}")
    print(f"  sign-flip p (H5: punch has FEWER syl/word): {p_punch_less:.4f}")
    results["H5"] = {
        "n_bits": n_compared,
        "mean_syll_per_word_setup": round(m_spw, 4),
        "mean_syll_per_word_punch": round(m_ppw, 4),
        "diff_punch_minus_setup": round(m_ppw - m_spw, 4),
        "sign_flip_p_one_tail": round(p_punch_less, 4),
        "supported": p_punch_less < 0.05 and obs < 0,
        "caveat": "text-based syllable estimate, not measured audio",
    }

# ---------- save ----------

out = "/root/gcomedy/experiments/results/timing_experiments.json"
with open(out, "w") as f:
    json.dump(results, f, indent=2)
print("\n" + "=" * 70)
print(f"RESULTS SAVED: {out}")
print(json.dumps(results, indent=2))
print("=" * 70)
