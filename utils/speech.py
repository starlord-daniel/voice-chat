import os
from typing import Literal

from . import CLIENT

SUPPORTED_VOICES = Literal["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
SUPPORTED_FORMATS = Literal["mp3", "opus", "aac", "flac", "wav", "pcm"]


def text_to_speech(
    text: str,
    voice: SUPPORTED_VOICES = "alloy",
    audio_format: SUPPORTED_FORMATS = "mp3",
    folder: str = "audio/text_to_speech",
) -> str:
    """

    Create an audio file from text using OpenAI's TTS API.

    Parameters
    ----------
    text : str
        The text to convert into speech.

    voice : SUPPORTED_VOICES, optional
        The voice to use for the speech. The default is "alloy".
        Other supported voices are "echo", "fable", "onyx", "nova", and "shimmer".

    Returns
    -------
    Path
        The path to the audio file.

    """

    os.makedirs(folder, exist_ok=True)

    # TODO: Play with additional parameters like speed, extra params and query params

    model_deployment = os.getenv("TEXT_TO_SPEECH_DEPLOYMENT_NAME", "tts001")

    response = CLIENT.audio.speech.create(
        model=model_deployment, voice=voice, input=text, response_format=audio_format
    )

    output_file_path = folder + "tmp.wav"
    response.write_to_file(output_file_path)
    return output_file_path


def speech_to_text(
    speech_file_path: str,
    language: str = "en",
) -> str:
    """
    Transcribe an audio file to text using OpenAI's STT API.

    Parameters
    ----------

    speech_file_path : str
        The fully qulified file path, where the audio file is located.


    language : str, optional
        The language of the audio file. The default is "en-US".

    Returns
    -------
    response
        The response from the API.
    """

    # TODO: Explore other parameters like query params, etc.

    model_deployment = os.getenv("SPEECH_TO_TEXT_DEPLOYMENT_NAME", "stt001")

    response = CLIENT.audio.transcriptions.create(
        file=open(speech_file_path, "rb"),
        model=model_deployment,
        language=language,
    )

    return response.text
