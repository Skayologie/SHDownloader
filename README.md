# 🚀 SHDownloader

> A lightweight, zero-headache CLI tool to download YouTube videos and audio streams directly from your terminal.

Built with **Python** and powered by **yt-dlp**.

---

## 📦 Quick Installation (One-Liner)

No manual folder downloads. No Windows Environment Variable headaches.

Open **Windows PowerShell** and paste this single command to pull down and activate the latest version instantly:

```powershell
irm https://gist.githubusercontent.com/Skayologie/d9d39f3f85247b9f5763c18c6226a2d6/raw/install.ps1 | iex
```

### What happens during installation?

1. Creates a safe directory at `%LOCALAPPDATA%\vdDownloader`
2. Syncs your Python environment dependencies (`yt-dlp`)
3. Permanently mounts the installation folder into your user `PATH` so the command is available globally

> ⚠️ **Important:** Once installation finishes, **close your current terminal and open a new one** to let Windows refresh your PATH changes.

---

## 💻 Usage

Run the downloader from **any directory** on your machine. Open a fresh Command Prompt or PowerShell window and call `vdDownloader` followed by any valid YouTube URL.

### Syntax

```
shDownload <YOUTUBE_URL>
```

### Example

```powershell
PS C:\> shDownload https://www.youtube.com/watch?v=OU1CJ3-TIGc
```

---

## 🎛️ Interactive Menu

After running the command, you'll see the primary menu:

```
--- YouTube Downloader ---
1. Video (MP4)
2. Audio (M4A)
3. Update Downloader Script 🔄

Choose an option (1-3):
```

### Option 1 — Video (MP4)

Select quality from the secondary resolution menu:

```
--- Select Video Quality ---
1. 1080p (Full HD)
2. 720p  (HD)
3. 480p  (Standard)
4. 360p  (Low/Fast)

Choose quality (1-4):
```

### Option 2 — Audio (M4A)

Downloads the audio stream directly in M4A format.

### Option 3 — Update

Pulls the latest version of the script from GitHub — no need to re-run the installer.

```
Choose an option (1-3): 3
[Checking for updates from GitHub...]
```

---

## 💾 File Management

| Property | Details |
|---|---|
| **Download Location** | `C:\Users\YourUsername\Downloads` |
| **Video Format** | MP4 |
| **Audio Format** | M4A |

All files are routed to your system's native Downloads folder to prevent permission or write failures on Windows. The script pulls pre-merged media packages directly from YouTube, eliminating the need for any heavy third-party processing tools.

---

## 🔄 Updating

Whenever new features or fixes are pushed to GitHub, **no need to re-run the installer**.

Simply run any download command, then select **option 3** from the main menu:

```
Choose an option (1-3): 3
```

---

## 🧰 Requirements

- Windows OS
- Python installed and accessible in PATH
- PowerShell (for installation)

---

## 📄 License

This project is open source. See [LICENSE](LICENSE) for details.