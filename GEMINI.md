# Project: my-scripts

A collection of personal utility scripts for system setup, media processing, and note management.

## Directory Overview
This repository contains independent scripts organized by their purpose. It is not a unified application but a toolkit for various automation tasks on a Linux environment.

## Key Files and Scripts

### System Setup
- **`setup.sh`**: Automates the installation of VS Code and Google Chrome on Debian/Ubuntu systems. It also configures GNOME Terminal to use `Ctrl+C` and `Ctrl+V` for copy and paste.

### Python Utilities
- **`python/download_mp3.py`**: A multithreaded script to download audio from YouTube URLs and convert them to MP3 using `yt-dlp`.
  - **Dependencies**: `yt-dlp` (`pip install yt-dlp`) and `ffmpeg` (system package).
  - **Usage**: Update the `urls` list in the script and run `python3 python/download_mp3.py`.

### Obsidian Utilities
- **`obsidian/convert-markdown-link.sh`**: Converts Obsidian-style wikilinks (`[[filename]]` or `[[filename|label]]`) into standard Markdown links.
  - **Usage**: `./obsidian/convert-markdown-link.sh <path_to_markdown_files>`

## Development Conventions
- Scripts are designed to be run independently.
- Bash scripts should be executable (`chmod +x`).
- Python scripts use `yt-dlp` for media handling.
