# YouTube Playlist Downloader

This project is a web application that allows users to download YouTube playlists as MP3 files. It uses Flask for the backend, SocketIO for real-time progress updates, and a simple HTML/CSS/JavaScript frontend with a particle animation background.

## Features

- Download entire YouTube playlists as MP3 files
- Real-time progress updates
- Interactive particle animation background
- Easy-to-use web interface

## Requirements

- Python 3.7+
- Flask
- Flask-SocketIO
- yt-dlp
- FFmpeg (for audio conversion)

## Building an Executable

This project includes PyInstaller configuration for building a standalone executable:

1. Ensure PyInstaller is installed:
   ```
   pip install pyinstaller
   ```

2. Build the executable:
   ```
   pyinstaller --name=YouTubePlaylistDownloader --onefile --add-data "templates:templates" --add-data "static:static" YT_download.py
   ```

