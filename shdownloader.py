import sys
import yt_dlp

def update_script():
    print("\n[Checking for updates from GitHub...]")
    # The URL to your raw install.ps1 script
    installer_url = "https://gist.githubusercontent.com/Skayologie/d9d39f3f85247b9f5763c18c6226a2d6/raw/install.ps1"
    
    # This command tells PowerShell to download and run your installer silently in the background
    powershell_command = f"powershell -Command \"irm {installer_url} | iex\""
    
    try:
        # Run the installer script
        subprocess.run(powershell_command, shell=True, check=True)
        print("\n[Update completed successfully! Please restart your terminal.]")
        sys.exit(0)
    except subprocess.CalledProcessError:
        print("\n[Error: Failed to connect to GitHub. Check your internet connection.]")
        sys.exit(1)
def main():
    if len(sys.argv) < 2:
        print("Error: Please provide a YouTube URL.")
        print("Usage: shDownload <youtube_url>")
        sys.exit(1)
        
    url = sys.argv[1]
    
    print("\n--- YouTube Downloader ---")
    print("1. Video (MP4)")
    print("2. Audio (M4A)")
    print("3. Update Downloader Script 🔄")
    main_choice = input("\nChoose an option (1 or 2): ").strip()
    
    if main_choice == "1":
        print("\n--- Select Video Quality ---")
        print("1. 1080p (Full HD)")
        print("2. 720p  (HD)")
        print("3. 480p  (Standard)")
        print("4. 360p  (Low/Fast)")
        
        quality_choice = input("\nChoose quality (1-4): ").strip()
        
        # Map choices to maximum vertical resolution thresholds
        quality_map = {
            "1": "1080",
            "2": "720",
            "3": "480",
            "4": "360"
        }
        
        max_height = quality_map.get(quality_choice, "720") # Default fallback to 720p if invalid
        
        print(f"\n[Downloading best pre-merged MP4 up to {max_height}p...]\n")
        ydl_opts = {
            # This logic targets pre-merged MP4s (b) with a height capped at what the user chose.
            # If a strict pre-merged match doesn't exist, it safely falls back to the nearest available format.
            'format': f'b[ext=mp4][height<={max_height}]/b[height<={max_height}]/best',
            'outtmpl': '%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
    elif main_choice == "2":
        print("\n[Downloading direct M4A audio stream...]\n")
        ydl_opts = {
            'format': 'bestaudio[ext=m4a]/bestaudio',
            'outtmpl': '%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    
    elif main_choice == "3":
        update_script()
        return
            
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()