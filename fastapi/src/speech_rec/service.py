from functools import lru_cache

from faster_whisper import WhisperModel


class Transcriber:
    """
    Transcriber class to transcribe audio file to text using pretrained Faster Whisper.
    """

    def __init__(self):
        self.load_model()

    @lru_cache(maxsize=1)
    def load_model(self):
        self.model = WhisperModel('base', device="cpu", compute_type="float32")

    def transcribe(self, audio_path):
        """
        This function transcribes an audio file and returns the information and transcripts.

        Args:
          audio_path: The path to the audio file that needs to be transcribed.

        Returns:
          The function `transcribe` returns a dictionary with information and transcripts.
        """
        segments, info = self.model.transcribe(audio_path)
        result = {
            'info': {
                'language': info.language,
                'language_probability': info.language_probability,
            },
            'segments': [
                {'start': segment.start, 'end': segment.end, 'text': segment.text}
                for segment in segments
            ],
        }
        return result
