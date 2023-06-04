import datetime
import os

from config import app_settings
from pytube import YouTube


def get_audio_file(audio_source, source_type):
    """
    The function get the bytes audio file from the audio source (YouTube link or uploaded file)

    Args:
      audio_source: The source of the audio file (YouTube link or uploaded file)
      source_type: The type of audio source, which can be either 'Youtube' or 'Upload'.

    Returns:
      an audio file in bytes format.
    """
    if source_type == 'Youtube':
        audio_name = f'{datetime.datetime.now().strftime("%Y-%m-%d_%H%M-%S")}.mp3'
        yc = YouTube(audio_source)
        yc.streams.get_audio_only().download(app_settings.PROJECT_DIR, filename=audio_name)
        with open(app_settings.PROJECT_DIR / audio_name, "rb") as f:
            audio = f.read()
        os.remove(app_settings.PROJECT_DIR / audio_name)
    elif source_type == 'Upload':
        audio = audio_source.getvalue()

    return audio
