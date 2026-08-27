import os
from concurrent.futures import ThreadPoolExecutor
import yt_dlp

def download_single_mp3(url):
    """Downloads a single URL and extracts audio to MP3."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': True,
        'no_warnings': True,
    }

    try:
        print(f"[+] Starting: {url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"[✔] Finished: {url}")
    except Exception as e:
        print(f"[✘] Error downloading {url}: {e}")

def load_urls_from_file(file_path="links.txt"):
    """Reads URLs line-by-line from a text file."""
    if not os.path.exists(file_path):
        print(f"Error: '{file_path}' not found. Please create it and add your links.")
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        # Strip whitespace, ignore blank lines and comments
        urls = [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]
    
    return urls

def download_batch_multithreaded(url_list, max_workers=3):
    """Downloads multiple URLs concurrently."""
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(download_single_mp3, url_list)

if __name__ == "__main__":
    links_file = "links.txt"
    urls = load_urls_from_file(links_file)

    if urls:
        print(f"Loaded {len(urls)} link(s) from {links_file}.")
        print("Starting multi-threaded download...")
        download_batch_multithreaded(urls, max_workers=3)
        print("All downloads completed!")
    else:
        print("No valid URLs found to download.")