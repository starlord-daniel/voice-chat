# Voice chat based on Text to Speech, Speech to text and LLMs

## Introduction

This project is a voice chat application that uses Text to Speech (TTS), Speech to Text (STT) and Language Models (LMs) to enable voice communication between a user and the application.
The application is built using Python.

## Architecture

The application is built using the following components:

- OpenAI API (Text to Speech, Speech to Text, Language Models)
- Python Sound Processing Libraries
- CLI Interface

This is a high-level diagram of the application's flow:

```mermaid
sequenceDiagram
    participant User as User
    participant SpeechChatApp as Speech Chat App
    participant OpenAIAPI as OpenAI API

    User->>SpeechChatApp: Record audio
    SpeechChatApp->>OpenAIAPI: Transcribe Audio
    OpenAIAPI-->>SpeechChatApp: Transcribed Text
    SpeechChatApp->>OpenAIAPI: Request LLM answer
    OpenAIAPI-->>SpeechChatApp: LLM Answer
    SpeechChatApp->>OpenAIAPI: Generate Audio
    OpenAIAPI-->>SpeechChatApp: Generated Audio
    SpeechChatApp->>User: Play audio
```

## Requirements

The following libraries are required to run the application:

- `openai` - OpenAI's Python library

## Other interesting libraries

- `openai` - OpenAI's Python library
- `pydub` - Audio manipulation library
- `pyaudio` - Audio I/O library
- `speech_recognition` - Speech recognition library
- `sounddevice` - Sound processing library
- `wave` - WAV file processing library
- `numpy` - Numerical computing library
- `pandas` - Data manipulation library
- `matplotlib` - Data visualization library
- `scipy` - Scientific computing library
- `librosa` - Audio and music processing library
- `tensorflow` - Machine learning library
- `keras` - Deep learning library
- `nltk` - Natural language processing library

## Related Links

- [Text to Speech](https://platform.openai.com/docs/guides/text-to-speech)
- [Speech to Text](https://platform.openai.com/docs/guides/speech-to-text)
- [Text Generation](https://platform.openai.com/docs/guides/text-generation)
