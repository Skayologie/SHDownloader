# 🚀 SHDownloader

> A lightweight, zero-headache CLI tool to download YouTube videos and audio streams directly from your terminal.

Built with **Python** and powered by **yt-dlp**.

---

## 📦 Quick Installation (One-Liner)

No manual folder downloads. No environment variable headaches.

### 🪟 Windows (PowerShell)

```powershell
irm https://www.jawadboulmal.com/SHDownload/install.ps1 | iex
```

#### What happens during installation?

1. Creates a safe directory at `%LOCALAPPDATA%\vdDownloader`
2. Syncs your Python environment dependencies (`yt-dlp`)
3. Permanently mounts the installation folder into your user `PATH` so the command is available globally

> ⚠️ **Important:** Once installation finishes, **close your current terminal and open a new one** to let Windows refresh your PATH changes.

---

### 🍎 macOS / Linux (Terminal)

```bash
curl -fsSL https://www.jawadboulmal.com/SHDownload/install.sh | bash
```

#### What happens during installation?

1. Downloads the latest version of the script
2. Installs required dependencies (`yt-dlp`)
3. Makes the `shDownload` command available globally in your shell

> ⚠️ **Important:** Once installation finishes, **close your current terminal and open a new one** to refresh execution paths, or run `source ~/.zshrc`.

---

## 💻 Usage

Run the downloader from **any directory** on your machine. You can pass a video URL, a full playlist URL, or use flags to manage the utility directly.

### Syntax

```bash
shDownload <URL_OR_FLAG>
```

### Global Commands & Flags

| Command | Action |
|---|---|
| `shDownload <YOUTUBE_URL>` | Launch downloader for a single video or video-with-playlist link |
| `shDownload <PLAYLIST_URL>` | Launch downloader explicitly parsed for a full playlist stream |
| `shDownload --update` | Instantly check for and deploy system updates directly via CLI |
| `shDownload --help` | Display the internal helper guide and implementation documentation |

---

## 🎛️ Dynamic Interactive Menus

The interface dynamically shifts depending on the type of link you pass into the program.

### Scenario A — You provide a Video Link (or Video with playlist tags)

The program automatically cleans trailing tracking queries and displays the single video manager:

```
--- YouTube Video Downloader 🎬 ---
1. Single Video (MP4)
2. Single Audio (M4A)
3. Update Downloader Script 🔄

Choose an option :
```

Choosing **Option 1** unlocks the resolution selection menu:

```
--- Select Video Quality ---
1. 1080p (Full HD)
2. 720p  (HD)
3. 480p  (Standard)
4. 360p  (Low/Fast)
```

### Scenario B — You provide a dedicated Playlist Link

The script detects the structure instantly, bypasses single-file menus, and takes you straight to the bulk-download manager:

```
--- YouTube Playlist Downloader 📂 ---
1. Full Playlist (MP4 Videos)
2. Full Playlist (M4A Audio)
3. Update Downloader Script 🔄

Choose an option :
```

---

## 💾 File & Folder Management

| Property | Behavior Details |
|---|---|
| **Download Target Location** | Routes natively to your platform user's default Downloads directory |
| **Single Video / Audio** | Dropped loosely into the core Downloads folder |
| **Playlist Collections** | Automatically creates a subfolder named after the playlist title, prefixing tracks dynamically by order index (e.g., `1 - Title.mp4`, `2 - Title.mp4`) |
| **Format Containers** | Coded exclusively for streamlined MP4 (Video) and M4A (Audio) bundles |

> 🛠️ **Error Shielding:** The framework handles network handshake hiccups automatically with up to 3 retries. If an item in a playlist is private, deleted, or region-locked, it skips the item cleanly without crashing the pipeline queue.

---

## 🔄 Updating

You never have to copy-paste the installation scripts again. When a new feature drops, update cleanly using either method:

**Option A** — Type the update flag directly into your shell:

```bash
shDownload --update
```

**Option B** — Run a normal link and select **option 3** (or 5 depending on context layout) from the active interactive selection menu.

---

## 🧰 Requirements

| Requirement | Details |
|---|---|
| **Supported OS** | Windows 10/11, macOS Mojave or newer, Linux |
| **Core Environment** | Python 3.10+ installed and exposed globally in your system PATH |

---

## 📄 License

This project is open source. See [LICENSE](LICENSE) for details.