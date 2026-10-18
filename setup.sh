#!/usr/bin/env bash
# setup.sh — fresh-box bootstrap for the gcomedy film studio.
# Clones all tool repos shallow, installs runtimes, verifies the render path.
# You bring: node 22+, python 3.11+, ffmpeg, and API keys (see KEYS below).
set -euo pipefail
cd "$(dirname "$0")"

TOOLS=essay1/tools
mkdir -p "$TOOLS"
clone() { [ -d "$TOOLS/$2" ] || git clone --depth 1 "https://github.com/$1.git" "$TOOLS/$2"; }

# Proven on box (tried, working)
clone wheresryan22/anatomy anatomy
clone Yoosseph/pc-anatomy pc-anatomy
clone Leonxlnx/earshot earshot
clone howseen-ai/claude-motion-design claude-motion-design
# Render core + reference pipeline
clone heygen-com/hyperframes hyperframes
clone blixvip/MotionClone MotionClone
clone 0xpratzyy/dissect dissect
# Shot grammar + direction
clone Vincentwei1021/video-shotcraft video-shotcraft
clone lemomo-ai/lemo-opuscar lemo-opuscar
clone GTKottman/mortiflix-oss mortiflix-oss
# Studios + editing
clone Remocn/remocn-studio remocn-studio
clone 0xsline/OpenChatCut OpenChatCut
clone clipkit-video/clipkit clipkit
clone KyaniteLabs/kinocut kinocut
clone WhiteTowerAI/cut-as-code cut-as-code
clone simplexlabs/montage montage
clone gomotion-io/gomotion gomotion
# Shaders + 3D staging
clone shader-effects-inc/shaders shaders
clone storytold/artcraft artcraft
clone hypit-ai/hypit hypit
clone calesthio/OpenMontage OpenMontage
# Indexes + small skills
clone zhuyansen/awesome-claude-video-skills awesome-claude-video-skills
clone VideoZero/skills skills
clone vumichien/manim-skill manim-skill

echo "--- runtimes ---"
pip install --break-system-packages -e ./essay1/tools/earshot 2>&1 | tail -n 1
pip install --break-system-packages playwright pillow numpy 2>&1 | tail -n 1
python3 -m playwright install chromium 2>&1 | tail -n 1 || true

echo "--- verify ---"
node --version; ffmpeg -version 2>/dev/null | head -n 1
ls "$TOOLS" | wc -l | xargs echo "tool repos:"
echo "KEYS NEEDED (never commit): OPENCODE_GO_API_KEY (pi agents), OPENROUTER_API_KEY (Jev, Jev-only), FISH_API_KEY (voices), FAL_API_KEY (Mirelo, ask-first)"
echo "FIRST RENDER: cd essay1/film/laptop-film && node build-scene-03a.mjs && npx -y hyperframes render . -c compositions/scene-03a.html -f 24"
