import io
import os
import sounddevice as sd

from pydub import AudioSegment
from pydub.playback import play
from scipy.io.wavfile import write


def record_audio(
    output_file_path: str,
    duration: int = 5,
    samplerate: int = 44100,
    channels: int = 2,
):
    """
    Record audio for a given duration and save it as a WAV file.

    Parameters
    ----------
    duration : int, optional
        The duration of the recording in seconds. The default is 5.

    samplerate : int, optional
        The samplerate of the recording. The default is 44100.

    channels : int, optional
        The number of channels. The default is 2.

    Returns
    -------
    None, but saves the audio as a WAV file to the chosen location

    """
    # Set the duration of the recording in seconds
    duration = 5  # seconds

    # Choose the samplerate and the number of channels
    samplerate = 44100  # Hertz
    channels = 1

    # Record audio
    print("Recording...")
    myrecording = sd.rec(
        int(samplerate * duration), samplerate=samplerate, channels=channels
    )
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")

    # Save as a WAV file
    write(output_file_path, samplerate, myrecording)


def play_audio_from_stream(input_file_path: str):
    """
    Play audio from a given file path.

    Parameters
    ----------
    input_file_path : str
        The path to the audio file.

    Returns
    -------
    None, but plays the audio.
    """

    with open(input_file_path, "rb") as f:
        audio_bytes = io.BytesIO(f.read())

    audio = AudioSegment.from_wav(audio_bytes)
    play(audio)

    # delete the temporary audio file
    os.remove(input_file_path)
