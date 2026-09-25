#!/usr/bin/env python3
"""Fill in missing UK/US pronunciation audio for every word in lessons.json.

For personal use only: audio comes from Cambridge Dictionary and must stay in
this private repository.

Usage (from the repo root):
    python3 tools/fetch_audio.py

For each word it saves audio/uk/<slug>.mp3 and audio/us/<slug>.mp3 and writes
the paths into lessons.json. Words whose audio already exists are skipped.
"""

import json
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LESSONS = ROOT / "lessons.json"
BASE = "https://dictionary.cambridge.org"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/126 Safari/537.36"


def slug(word: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", word.lower()).strip("-")


def curl(url: str, out: Path | None = None) -> bytes:
    cmd = ["curl", "-sfL", "-A", UA, url]
    if out:
        cmd += ["-o", str(out)]
    return subprocess.run(cmd, check=True, capture_output=True).stdout


def audio_urls(word: str) -> dict[str, str]:
    """Return the first UK and US mp3 URL from the word's Cambridge page."""
    html = curl(f"{BASE}/dictionary/english/{slug(word)}").decode("utf-8", "replace")
    urls = {}
    for accent in ("uk", "us"):
        m = re.search(
            rf'<span class="{accent} dpron-i[^"]*".*?src="(/media/english/{accent}_pron/[^"]+\.mp3)"',
            html,
            re.S,
        )
        if m:
            urls[accent] = BASE + m.group(1)
    return urls


def main() -> int:
    data = json.loads(LESSONS.read_text(encoding="utf-8"))
    missing = []
    for lesson in data["lessons"]:
        for w in lesson["words"]:
            audio = w.setdefault("audio", {})
            todo = [a for a in ("uk", "us") if not (audio.get(a) and (ROOT / audio[a]).exists())]
            if not todo:
                continue
            try:
                urls = audio_urls(w["en"])
            except subprocess.CalledProcessError:
                urls = {}
            for accent in todo:
                if accent not in urls:
                    audio.pop(accent, None)
                    missing.append(f"{w['en']} ({accent.upper()})")
                    continue
                path = f"audio/{accent}/{slug(w['en'])}.mp3"
                curl(urls[accent], ROOT / path)
                audio[accent] = path
                print(f"ok  {w['en']:<20} {accent.upper()}")
            time.sleep(1)  # be polite to the site

    LESSONS.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if missing:
        print("\nAudio not found:", ", ".join(missing))
    return 0


if __name__ == "__main__":
    sys.exit(main())
