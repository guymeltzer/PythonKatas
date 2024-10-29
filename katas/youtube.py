import os
from pytubefix import YouTube


def youtube_download(url):
    """
    The function receives a valid YouTube URL and downloads the audio only to the current workdir, in a mp3 format (must end with .mp3).

    Note: the function uses the `pytube` package

    :param url: video url
    :return: None
    """
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    output_file = audio_stream.download()
    base, _ = os.path.splitext(output_file)
    new_file = f"{base}.mp3"
    os.rename(output_file, new_file)
    print(f"Downloaded and saved as: {new_file}")


if __name__ == '__main__':
    youtube_download('https://www.youtube.com/watch?v=xhud_6AHKfo')
