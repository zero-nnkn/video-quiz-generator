import datetime
import os

from fastapi.responses import JSONResponse

from fastapi import APIRouter, File

from .service import Transcriber

router = APIRouter()


transcripber = Transcriber()


@router.post('/transcriptions')
def transcribe(audio_file: bytes = File()) -> JSONResponse:
    """
    The function transcribes an audio file and returns the transcripts in a JSON response.
    """
    save_name = f'{datetime.datetime.now().strftime("%Y-%m-%d_%H%M-%S")}.mp3'
    with open(save_name, 'wb') as f:
        f.write(audio_file)

    try:
        transcripts = transcripber.transcribe(save_name)
    except Exception:
        return JSONResponse(content={'message': 'transcribe error'})

    os.remove(save_name)

    return JSONResponse(
        content={
            'message': 'success',
            'transcripts': transcripts,
        }
    )
