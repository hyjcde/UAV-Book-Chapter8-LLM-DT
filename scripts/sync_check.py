#!/usr/bin/env python3
"""Check EN/CN Chapter 8 section-label parity from SECTION_MAP.yaml."""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "latex" / "SECTION_MAP.yaml"
EN = ROOT / "latex" / "en" / "ch08.tex"
CN = ROOT / "latex" / "en" / "cn" / "ch08_cn.tex"


def load_ids() -> list[str]:
    text = MAP.read_text(encoding="utf-8")
    if yaml is not None:
        data = yaml.safe_load(text)
        return [s["id"] for s in data["sections"]]
    # minimal fallback without PyYAML
    return re.findall(r"^\s*-\s*id:\s*(\S+)", text, flags=re.M)


def labels_in(path: Path) -> set[str]:
    t = path.read_text(encoding="utf-8")
    return set(re.findall(r"\\label\{([^}]+)\}", t))


def main() -> int:
    ids = load_ids()
    en = labels_in(EN)
    cn = labels_in(CN)
    missing_en = [i for i in ids if i not in en]
    missing_cn = [i for i in ids if i not in cn]
    print(f"SECTION_MAP ids: {len(ids)}")
    print(f"EN labels: {len(en)} | CN labels: {len(cn)}")
    ok = True
    if missing_en:
        ok = False
        print("MISSING in EN:", ", ".join(missing_en))
    if missing_cn:
        ok = False
        print("MISSING in CN:", ", ".join(missing_cn))
    if ok:
        print("OK: all mapped section labels present in EN and CN.")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
