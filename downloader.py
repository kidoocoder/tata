from yt_dlp import YoutubeDL
import os

def download_audio(query: str):
    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'noplaylist': True,
        'quiet': True,
        'default_search': 'ytsearch1',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'opus',
            'preferredquality': '192',
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=True)
        title = info.get("title")
        filename = ydl.prepare_filename(info).replace(".webm", ".opus").replace(".m4a", ".opus")
        return filename, title
