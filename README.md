# Bristol-VLA Demo

Bristol-VLA 的公开论文展示页。研究代码保留在独立 private 仓库中。

[在线页面](https://aoli0919.github.io/Bristol-VLA-demo/)

## 本地预览

在仓库根目录运行 `python3 -m http.server 8000`，打开 <http://localhost:8000>。

## 更新内容与视频

- 在 `index.html` 替换论文标题、作者、单位、贡献脚注、Abstract 等占位内容。
- 在 `videos.json` 填写四个视频：`overview` 为主视频，`task1`、`task2`、`task3` 为三个任务视频。当前 `src`、`poster` 全部留空。
- `src` 填视频文件直链或相对路径（如 `assets/videos/overview.mp4`），`poster` 填可选封面路径；`src` 留空时保留占位。

## 检查与发布

运行 `python3 scripts/check_site.py` 检查资源、导航与视频清单。

推送到 `main` 后自动上线 GitHub Pages。
