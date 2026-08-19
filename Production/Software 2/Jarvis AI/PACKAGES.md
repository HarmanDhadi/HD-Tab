# Packages & Dependencies

This project was developed in Python and uses the following packages.

## Core Packages

* PyQt6
* SpeechRecognition
* PyAudio
* sounddevice
* soundfile
* requests
* google-genai
* piper-tts
* python-vlc
* yt-dlp
* playsound3
* spotipy
* numpy
* onnxruntime

## Install Python Dependencies

Install all required Python packages using:

```bash
pip install -r requirements.txt
```

## System Dependencies

Depending on your operating system, you may also need:

* VLC Media Player
* FFmpeg
* Piper TTS
* PortAudio (required for PyAudio)
* Deno (recommended for the latest versions of yt-dlp)

## Notes

* This repository does **not** include the Piper voice models because they are too large for GitHub.
* Download the required Piper voice model separately before running the assistant.
* Store your Gemini API key securely (for example in a `.env` file or as an environment variable). Never commit API keys to GitHub.
