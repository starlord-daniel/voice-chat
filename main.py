import os
from utils.speech import text_to_speech, speech_to_text
from utils.language import generate_answer
from utils.audio import record_audio, play_audio_from_stream


AUDIO_FILE_PATH = "audio/tmp.wav"
RECORDING_DURATION = 5  # seconds


def main():

    # create the audio folder if it does not exist
    os.makedirs(AUDIO_FILE_PATH.rsplit("/", 1)[0], exist_ok=True)

    # Record audio
    input("Press Enter to start recording for 5s...")

    record_audio(AUDIO_FILE_PATH, duration=RECORDING_DURATION)

    # Send audio and transform it to text
    transcription = speech_to_text(AUDIO_FILE_PATH)

    # delete the temporary audio file
    os.remove(AUDIO_FILE_PATH)

    # # Use text to generate an answer
    answer = generate_answer(transcription, language="spanish")

    if not answer:
        print("No answer was generated.")
        return

    print("Generating voice, please wait...")

    # Generate audio from the answer
    generated_speech_path = text_to_speech(
        answer,
        audio_format="wav",
        voice="echo",
        model_deployment="tts002",
        folder=AUDIO_FILE_PATH.rsplit("/", 1)[0],
    )
    play_audio_from_stream(generated_speech_path)

    # Print the initial text and answer well formatted
    print(f"Initial Text: {transcription}")
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
