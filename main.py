import os
from pytube import YouTube

DEFAULT_DOWNLOAD_PATH_WINDOWS = os.path.expanduser('~') + "\\Downloads\\"

def download(output_path: str, url: str, file_extension: str) -> YouTube:
    youtube = YouTube(url)
    streams = youtube.streams.get_highest_resolution()
    streams.download(output_path=output_path, filename=f"{youtube.title}.{file_extension}")
    return youtube

