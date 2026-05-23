import sys
import os
import yt_dlp
import subprocess

def update_script():
    print("\n[Checking for updates from GitHub...]")
    installer_url = "https://www.jawadboulmal.com/SHDownload/install.ps1"
    powershell_command = f"powershell -Command \"irm {installer_url} | iex\""
    
    try:
        subprocess.run(powershell_command, shell=True, check=True)
        print("\n[Update completed successfully! Please restart your terminal.]")
        sys.exit(0)
    except subprocess.CalledProcessError:
        print("\n[Error: Failed to connect to GitHub. Check your internet connection.]")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Error: Please provide a YouTube URL or Playlist URL.")
        print("Usage: shDownload <url>")
        sys.exit(1)
        
    url = sys.argv[1].strip()
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    
    print("\n--- YouTube Downloader ---")
    print("1. Single Video (MP4)")
    print("2. Single Audio (M4A)")
    print("3. Full Playlist (MP4 Videos) 📂")
    print("4. Full Playlist (M4A Audio) 🎵")
    print("5. Update Downloader Script 🔄")
    main_choice = input("\nChoose an option : ").strip()
    
    base_ydl_opts = {
        'outtmpl': os.path.join(downloads_folder, '%(title)s.%(ext)s'),
        'restrictfilenames': True,
        'ignoreerrors': True,
        'retries': 3,
        'fragment_retries': 3,
    }
    
    if main_choice == "1":
        if "watch?v=" in url and "&list=" in url:
            url = url.split("&list=")[0]
            
        print("\n--- Select Video Quality ---")
        print("1. 1080p (Full HD)")
        print("2. 720p  (HD)")
        print("3. 480p  (Standard)")
        print("4. 360p  (Low/Fast)")
        
        quality_choice = input("\nChoose quality (1-4): ").strip()
        quality_map = {"1": "1080", "2": "720", "3": "480", "4": "360"}
        max_height = quality_map.get(quality_choice, "720")
        
        print(f"\n[Downloading best pre-merged MP4 up to {max_height}p...]\n")
        
        base_ydl_opts.update({
            'format': f'b[ext=mp4][height<={max_height}]/b[height<={max_height}]/best',
            'noplaylist': True,
        })
        
        try:
            with yt_dlp.YoutubeDL(base_ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            print(f"\n[Error: Video is unavailable or untransferable. Skipping...]")
            
    elif main_choice == "2":
        if "watch?v=" in url and "&list=" in url:
            url = url.split("&list=")[0]
            
        print("\n[Downloading direct M4A audio stream...]\n")
        
        base_ydl_opts.update({
            'format': 'bestaudio[ext=m4a]/bestaudio',
            'noplaylist': True,
        })
        
        try:
            with yt_dlp.YoutubeDL(base_ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            print(f"\n[Error: Audio stream is unavailable. Skipping...]")
            
    elif main_choice == "3":
        print("\n--- Select Playlist Video Quality ---")
        print("1. 1080p (Full HD)")
        print("2. 720p  (HD)")
        print("3. 480p  (Standard)")
        print("4. 360p  (Low/Fast)")
        
        quality_choice = input("\nChoose quality (1-4): ").strip()
        quality_map = {"1": "1080", "2": "720", "3": "480", "4": "360"}
        max_height = quality_map.get(quality_choice, "720")
        
        print(f"\n[Downloading full playlist as MP4 videos up to {max_height}p...]\n")
        
        base_ydl_opts.update({
            'format': f'b[ext=mp4][height<={max_height}]/b[height<={max_height}]/best',
            'outtmpl': os.path.join(downloads_folder, '%(playlist_title)s', '%(playlist_index)s - %(title)s.%(ext)s'),
            'yesplaylist': True,
        })
        
        try:
            with yt_dlp.YoutubeDL(base_ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            print(f"\n[Notice: Playlist download complete with skipped unavailable entries.]")
            
    elif main_choice == "4":
        print("\n[Downloading full playlist as M4A audio tracks...]\n")
        
        base_ydl_opts.update({
            'format': 'bestaudio[ext=m4a]/bestaudio',
            'outtmpl': os.path.join(downloads_folder, '%(playlist_title)s', '%(playlist_index)s - %(title)s.%(ext)s'),
            'yesplaylist': True,
        })
        
        try:
            with yt_dlp.YoutubeDL(base_ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            print(f"\n[Notice: Playlist download complete with skipped unavailable entries.]")
    
    elif main_choice == "5":
        update_script()
        return
            
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()