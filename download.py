import sys
import os
import yt_dlp
from concurrent.futures import ThreadPoolExecutor, as_completed

def download_playlist(playlist_url, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'ignoreerrors': True,
        'verbose': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([playlist_url])
        except Exception as e:
            print(f"An error occurred while downloading {playlist_url}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 download_script.py <playlist_url> <output_dir>")
        sys.exit(1)

    playlist_url = sys.argv[1]
    output_dir = sys.argv[2]

    download_playlist(playlist_url, output_dir)

    print("Download complete.")
