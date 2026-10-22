# Bristol-VLA Demo

Public paper showcase for Bristol-VLA. The research code is kept in a separate private repository.

[Live site](https://aoli0919.github.io/Bristol-VLA-demo/)

## Local preview

Run `python3 -m http.server 8000` from the repository root, then open <http://localhost:8000>.

## Updating content and videos

- Replace the placeholder paper title, authors, affiliations, contribution footnotes, Abstract, and other content in `index.html`.
- Add the four videos to `videos.json`: `overview` is the main video; `task1`, `task2`, and `task3` are the three task videos. All `src` and `poster` fields are currently empty.
- Set `src` to a direct video URL or relative path (for example, `assets/videos/overview.mp4`). Set `poster` to an optional poster image path. If `src` is empty, the placeholder remains.

## Checks and publishing

Run `python3 scripts/check_site.py` to check assets, navigation, and the video manifest.

The site is published automatically to GitHub Pages when changes are pushed to `main`.
