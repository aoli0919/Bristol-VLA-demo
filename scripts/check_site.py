"""Validate the static demo's local assets, anchors, and video configuration."""

from __future__ import annotations

import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

SITE = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.slots = []
        self.lang = None

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "html":
            self.lang = attributes.get("lang")
        if "id" in attributes:
            self.ids.append(attributes["id"])
        for name in ("src", "href"):
            if attributes.get(name):
                self.links.append(attributes[name])
        if "data-video-slot" in attributes:
            self.slots.append(attributes["data-video-slot"])


def check_url(value):
    parts = urlsplit(value)
    if parts.scheme or parts.netloc:
        assert parts.scheme in {"http", "https"}, f"Unsupported URL: {value}"
        return
    if parts.path:
        assert not parts.path.startswith("/"), f"Use a relative site path: {value}"
        target = (SITE / unquote(parts.path)).resolve()
        assert target.is_relative_to(SITE), f"Path outside site: {value}"
        assert target.exists(), f"Missing site asset: {value}"


def main():
    assert SITE.is_dir(), "Missing site directory"
    videos = json.loads((SITE / "videos.json").read_text(encoding="utf-8"))
    for filename, language in (("index.html", "en"), ("zh.html", "zh-CN")):
        page = Page()
        page.feed((SITE / filename).read_text(encoding="utf-8"))
        assert page.lang == language, f"Incorrect page language: {filename}"
        assert len(page.ids) == len(set(page.ids)), f"Duplicate HTML IDs: {filename}"
        assert len(page.slots) == len(set(page.slots)), f"Duplicate video slots: {filename}"
        assert set(videos) == set(page.slots), f"Video slots do not match: {filename}"
        for link in page.links:
            check_url(link)
            parts = urlsplit(link)
            if not parts.path and parts.fragment:
                assert parts.fragment in page.ids, f"Missing page anchor in {filename}: {link}"

    for slot, entry in videos.items():
        assert isinstance(entry, dict), f"Invalid video entry: {slot}"
        for key in ("src", "poster"):
            value = entry.get(key)
            assert isinstance(value, str), f"{slot}.{key} must be a string"
            if value.strip():
                check_url(value.strip())
    print(f"PASS: 2 language pages, site assets and anchors, {len(videos)} video slots.")


if __name__ == "__main__":
    main()
