#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

if [[ ! -f dinox/README.md ]]; then
    echo "▸ Initializing dinox submodule (sparse checkout)..."
    git submodule update --init
    cd dinox
    git sparse-checkout init --cone
    git sparse-checkout set README.md examples/DINO_Tutorial.ipynb
    cd ..
fi

# ── Pull latest from dinox main ─────────────────────────────────────────────
echo "Fetching latest dinox..."
git submodule update --remote

# ── Build combined README ────────────────────────────────────────────────────
echo "Building README.md..."
python _dev/scripts/merge_readme.py \
    --title "LazyDINO Tutorial Readme" \
    --part1-label "Part 1: DINO" \
    --part2-label "Part 2: LazyDINO" \
    dinox/README.md \
    _dev/LMVI_README.md \
    README.md

# ── Build combined notebook ─────────────────────────────────────────────────
echo "Building LazyDINO_Tutorial.ipynb..."
python _dev/scripts/merge_notebooks.py \
    --title "LazyDINO Tutorial" \
    --part1-label "Part 1: DINO" \
    --part2-label "Part 2: LazyDINO" \
    dinox/examples/DINO_Tutorial.ipynb \
    _dev/LMVI_Tutorial.ipynb \
    LazyDINO_Tutorial.ipynb

echo "Combined README.md"
echo "Combined LazyDINO_Tutorial.ipynb"
echo "  dinox pinned at: $(cd dinox && git rev-parse --short HEAD)"
