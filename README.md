# Bristol-VLA Demo

Bristol-VLA 的公开项目展示页。本仓库只存放静态页面与部署文件，研究代码仍在独立私有仓库中。

[在线页面](https://aoli0919.github.io/Bristol-VLA-demo/)

## 本地预览

在仓库根目录运行 `python3 -m http.server 8000`，打开 <http://localhost:8000>。

## 更新内容与视频

- 页面文字：`index.html`；样式：`styles.css`。
- 四个视频位置在 `videos.json` 中配置，当前全部留空。
- 视频可放入 `assets/videos/`，例如将 `overview.src` 填为 `assets/videos/overview.mp4`，也可使用 HTTPS 视频直链。
- `src` 留空时显示占位；`poster` 为可选封面图片路径。
- 视频需使用文件直链，不能使用 GitHub 的 blob 页面链接。大视频建议放外部存储。
- 页面内容为公开信息，更新时仅提交准备对外展示的材料。

## 检查与发布

运行 `python3 scripts/check_site.py` 检查资源、导航与视频清单。

推送到 `main` 后自动部署 GitHub Pages，也可在 Actions 手动运行 `Deploy demo page`。部署只上传网页及 `assets/`。
