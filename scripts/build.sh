#!/usr/bin/env bash
# Build English (pdflatex+SNmono) and Chinese (xelatex+ctex) Chapter 8 PDFs.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "== sync_check =="
python3 scripts/sync_check.py

build_en() {
  echo "== EN (pdflatex + SNmono shell) =="
  cd "$ROOT/latex/en"
  pdflatex -interaction=nonstopmode book_ch08.tex >/tmp/ch08_en_1.log || true
  bibtex book_ch08 >/tmp/ch08_en_bib.log 2>&1 || true
  # Springer index style when .idx is non-empty
  if [[ -s book_ch08.idx ]]; then
    makeindex -s svind.ist book_ch08 >/tmp/ch08_en_idx.log 2>&1 || true
  fi
  pdflatex -interaction=nonstopmode book_ch08.tex >/tmp/ch08_en_2.log || true
  pdflatex -interaction=nonstopmode book_ch08.tex >/tmp/ch08_en_3.log
  pages=$(pdfinfo book_ch08.pdf 2>/dev/null | awk '/Pages/{print $2}')
  echo "EN PDF: latex/en/book_ch08.pdf pages=${pages:-?}"
  grep -E '^! |Output written|Emergency stop' /tmp/ch08_en_3.log | tail -8 || true
}

build_cn() {
  echo "== CN (xelatex) =="
  cd "$ROOT/latex/cn"
  xelatex -interaction=nonstopmode book_ch08.tex >/tmp/ch08_cn_1.log || true
  bibtex book_ch08 >/tmp/ch08_cn_bib.log 2>&1 || true
  xelatex -interaction=nonstopmode book_ch08.tex >/tmp/ch08_cn_2.log || true
  xelatex -interaction=nonstopmode book_ch08.tex >/tmp/ch08_cn_3.log
  pages=$(pdfinfo book_ch08.pdf 2>/dev/null | awk '/Pages/{print $2}')
  echo "CN PDF: latex/cn/book_ch08.pdf pages=${pages:-?}"
  grep -E '^! |Output written' /tmp/ch08_cn_3.log | tail -5 || true
}

# parallel builds
build_en &
PID_EN=$!
build_cn &
PID_CN=$!
wait $PID_EN
wait $PID_CN
echo "== done =="
