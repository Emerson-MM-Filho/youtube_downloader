import os
from pytube import YouTube

DEFAULT_DOWNLOAD_PATH_WINDOWS = os.path.expanduser('~') + "\\Downloads\\"

def download(output_path: str, url: str, file_extension: str) -> YouTube:
    youtube = YouTube(url)
    streams = youtube.streams.get_highest_resolution()
    streams.download(output_path=output_path, filename=f"{youtube.title}.{file_extension}")
    return youtube

if __name__ == "__main__":
    url = input("Insert the url: ")
    output_path = input(f"Insert the download path (or \"enter\" for default - \"{DEFAULT_DOWNLOAD_PATH_WINDOWS}\"): ")
    file_extension = input("Insert the file extension (\"mp3\" or \"mp4\"): ")
    download(output_path or DEFAULT_DOWNLOAD_PATH_WINDOWS, url, file_extension)
