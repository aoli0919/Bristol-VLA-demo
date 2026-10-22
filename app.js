/* Video sources are optional. Empty entries keep the designed placeholders. */
(async () => {
  if (window.location.protocol === "file:") return;

  const safeMediaUrl = (value) => {
    if (typeof value !== "string" || !value.trim()) return null;
    try {
      const url = new URL(value.trim(), document.baseURI);
      return ["https:", "http:"].includes(url.protocol) ? url.href : null;
    } catch {
      return null;
    }
  };

  try {
    const response = await fetch(new URL("videos.json", document.baseURI));
    if (!response.ok) throw new Error(`Video manifest: HTTP ${response.status}`);
    const sources = await response.json();

    document.querySelectorAll("[data-video-slot]").forEach((slot) => {
      const entry = sources[slot.dataset.videoSlot];
      const src = safeMediaUrl(entry?.src);
      if (!src) return;

      const video = document.createElement("video");
      video.controls = true;
      video.playsInline = true;
      video.preload = "metadata";
      video.setAttribute("aria-label", `${slot.dataset.videoTitle}视频`);
      const poster = safeMediaUrl(entry.poster);
      if (poster) video.poster = poster;
      video.src = src;

      video.addEventListener("error", () => {
        video.remove();
        slot.querySelector(".media-placeholder").hidden = false;
        const notice = document.createElement("p");
        notice.className = "media-error";
        notice.setAttribute("role", "status");
        notice.textContent = "视频暂时无法加载，请稍后再试。";
        slot.append(notice);
      }, { once: true });

      slot.querySelector(".media-placeholder").hidden = true;
      slot.append(video);
    });
  } catch (error) {
    // The page remains usable when the optional video list cannot be loaded.
    console.warn("Bristol-VLA: video placeholders retained.", error.message);
  }
})();
