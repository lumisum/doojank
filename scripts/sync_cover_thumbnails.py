"""Refresh homepage cover thumbnails for explicitly selected article slugs."""

import argparse
import hashlib
import json
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageOps

from export_wechat import parse_frontmatter


ROOT = Path(__file__).resolve().parents[1]


def sync(slugs: list[str]) -> None:
    mapping_path = ROOT / "_data/doojank_covers.json"
    mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
    destination = ROOT / "assets/doojank/essay-thumbs"
    updates = []
    for slug in slugs:
        if Path(slug).name != slug or slug in {".", ".."}:
            raise ValueError("Provide article directory names, not paths.")
        sources = {
            "zh-CN": ROOT / "articles" / slug / "article.md",
            "en": ROOT / "en/articles" / slug / "index.md",
        }
        for lang, source in sources.items():
            if not source.exists():
                continue
            metadata, _ = parse_frontmatter(source.read_text(encoding="utf-8"))
            cover = metadata.get("cover", "").split("?", 1)[0]
            if not cover.startswith("/") or "://" in cover:
                raise ValueError(f"Local cover required: {source}")
            cover_path = (ROOT / cover.lstrip("/")).resolve()
            if not cover_path.is_relative_to(ROOT):
                raise ValueError(f"Cover is outside the repository: {source}")
            with Image.open(cover_path) as image:
                thumbnail = ImageOps.exif_transpose(image).convert("RGB")
                thumbnail.thumbnail((1000, 450), Image.Resampling.LANCZOS)
                data = BytesIO()
                thumbnail.save(data, format="WEBP", quality=85, method=6)
            payload = data.getvalue()
            version = hashlib.sha256(payload).hexdigest()[:12]
            name = f"{slug}-{lang}-{version}.webp"
            mapping.setdefault(slug, {})[lang] = f"/assets/doojank/essay-thumbs/{name}"
            updates.append((destination / name, payload))
    destination.mkdir(parents=True, exist_ok=True)
    for path, payload in updates:
        path.write_bytes(payload)
        print(path.relative_to(ROOT))
    mapping_path.write_text(json.dumps(mapping, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slugs", nargs="+", help="Only refresh these article directories.")
    sync(parser.parse_args().slugs)
