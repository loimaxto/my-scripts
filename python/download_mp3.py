# pip install yt_dlp

import yt_dlp
from concurrent.futures import ThreadPoolExecutor

def download_single_mp3(url):
    """Function to download a single URL, used by the threads."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': True,  # Keeps the terminal cleaner during multi-download
        'no_warnings': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading: {url}")
            ydl.download([url])
            print(f"Finished: {url}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def download_batch_multithreaded(url_list):

    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(download_single_mp3, url_list)

if __name__ == "__main__":
    urls = [
        "https://www.youtube.com/watch?v=example1",
        "https://www.youtube.com/watch?v=example2",
        "https://www.youtube.com/watch?v=example3",
        "https://www.youtube.com/watch?v=example4",
        "https://www.youtube.com/watch?v=example5"
    ]
    
    print("Starting multi-threaded download...")
    download_batch_multithreaded(urls)
    print("Done!")