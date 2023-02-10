import os
from pytube import YouTube

DEFAULT_DOWNLOAD_PATH_WINDOWS = os.path.expanduser('~') + "\\Downloads\\"

def download(output_path: str, url: str, file_extension: str) -> YouTube:
    youtube = YouTube(url)
    streams = youtube.streams.get_highest_resolution()
    streams.download(output_path=output_path, filename=f"{youtube.title}.{file_extension}")
    return youtube

if __name__ == "__main__":
    url = input("Enter the youtube video url: ")
    file_extension = input("Choose the format you want to download (\"mp3\" or \"mp4\"): ")
    output_path = input(f"Enter the output path, or leave blank (\"enter\") for the default path (\"{DEFAULT_DOWNLOAD_PATH_WINDOWS}\"): ")
    download(output_path or DEFAULT_DOWNLOAD_PATH_WINDOWS, url, file_extension)
