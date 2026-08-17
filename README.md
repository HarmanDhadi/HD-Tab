# HD-Tab

**HD-Tab** is a personal smart-display project built around a **Raspberry Pi 3 Model B+**, combining an AI voice assistant, a touchscreen dashboard, media playback, and custom hardware/CAD designs.

The project is designed to function as a compact, customizable smart display with **Jarvis AI** and **MagicMirror²** working together.

---

## Features

### Jarvis AI

Jarvis is the voice assistant component of HD-Tab.

Features include:

* Gemini-powered AI responses
* Voice input
* Text-to-speech responses
* Wake-word activation
* Short microphone listening periods
* General questions and conversations
* YouTube music/video playback
* Play and pause media
* Automatically lowers media volume while Jarvis responds
* Restores the previous volume after responding
* Designed for Raspberry Pi deployment

Jarvis is written primarily in **Python**.

---

###  MagicMirror²

HD-Tab uses a customized MagicMirror² interface as its main smart-display dashboard.

The current setup includes:

* Clock
* Weather
* News
* Custom background slideshow
* Custom CSS
* Custom MagicMirror configuration
* Touchscreen support

The custom MagicMirror module currently included in the project is:

* `MMM-BackgroundSlideshow`

---

### 3D & CAD

The project also contains custom CAD designs used for the physical HD-Tab build.

These files are located in:

```text
3D CAD/
```

---

## Hardware

HD-Tab is designed around a **Raspberry Pi 3 Model B+**.

| Component                    | Vendor       |           Price |
| ---------------------------- | ------------ | --------------: |
| Raspberry Pi 3 Model B+      | Raspberry Pi |               — |
| 7-Inch Touch Display         | Waveshare    |      $55.99 CAD |
| Speaker                      | Amazon       |      $23.56 CAD |
| USB Microphone               | Amazon       |       $7.95 CAD |
| USB Power Distribution Board | Amazon       |      $19.84 CAD |
| 5V 10A Power Adapter         | Amazon       |      $21.99 CAD |
| LCD Adhesive                 | Amazon       |       $8.99 CAD |
| **Total**                    |              | **$158.72 CAD** |

The Raspberry Pi 3B+ was already owned and therefore isn't included in the project cost.

CAD Files are designed to support all listed parts. Support for unlisted products may vary.

### Display

A 7-inch Waveshare touchscreen provides the main interface for the MagicMirror dashboard and allows HD-Tab to be interacted with directly.

### Audio

A dedicated speaker is used for Jarvis responses and media playback.

A USB microphone provides voice input for the Jarvis assistant.

### Power

The system uses a USB power distribution board and a 5V 10A power adapter to provide power to the connected hardware.

---

## Software

HD-Tab uses a combination of Python, JavaScript, and existing open-source software.

### Jarvis

* Python
* Google Gemini API
* SpeechRecognition
* Piper TTS
* PyAudio
* PyQt6
* yt-dlp
* VLC

### MagicMirror

* MagicMirror²
* Node.js
* JavaScript
* HTML
* CSS
* `MMM-BackgroundSlideshow`

---

## Repository Structure

```text
HD-Tab/
│
├── Jarvis AI/
│   ├── Python/
│   │   ├── voice.py
│   │   ├── youtube_player.py
│   │   └── ...
│   │
│   ├── requirements.txt
│   └── ...
│
├── MagicMirror/
│   ├── config/
│   │   ├── config.js
│   │   └── custom.css
│   │
│   └── modules/
│       └── MMM-BackgroundSlideshow/
│
├── 3D CAD/
│   └── ...
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## Getting Started

### Jarvis AI

Navigate to the Jarvis Python directory and install the required Python packages:

```bash
pip install -r requirements.txt
```

Then run the assistant:

```bash
python voice.py
```

Jarvis requires the appropriate API credentials and hardware permissions for microphone and audio access.

### MagicMirror²

The `MagicMirror/` directory contains the custom configuration and modules used by HD-Tab.

The project uses MagicMirror² as the foundation while keeping HD-Tab's custom configuration and modules inside this repository.

---

## API Keys & Security

**Never commit API keys, passwords, tokens, or other private credentials to this repository.**

API credentials should be stored locally or through environment variables.

Example:

```text
YOUR_API_KEY_HERE
```

should be used as a placeholder in source code that is uploaded to GitHub.

Your real API key should never be committed to the repository.

---

## Python Dependencies

Python dependencies used by Jarvis are listed in:

```text
Jarvis AI/Python/requirements.txt
```

Install them with:

```bash
pip install -r requirements.txt
```

Some dependencies may be platform-specific and may require additional setup when moving the project from macOS to Raspberry Pi OS.

---

## Raspberry Pi

HD-Tab is intended to run on a **Raspberry Pi 3 Model B+**.

The development environment may differ from the final Raspberry Pi environment, particularly for:

* Audio libraries
* Text-to-speech
* Microphone drivers
* Node.js dependencies
* VLC
* Python packages

Additional setup may therefore be required when deploying the project to the Raspberry Pi.

---

##  Project Status

HD-Tab is an ongoing personal project.

The core Jarvis AI and MagicMirror components have been developed and tested during development, with Raspberry Pi deployment being the intended final platform.

Developed Components: Jarvis AI (Voice Recognition, Voice Model (Piper TTS Engine), Text Responses, Music/Podcast via Youtube and UI)
                      MagicMirror (UI, News Feed( CBC News, Toronto ON), Weather & Forecast(Brampton ON), Custom Calendar(via custom ics.)
                      Logo & Art (Splash Screen, On Screen Button & Desktop Background)

Features and hardware may change as the project continues to evolve.

---

##  License

This project is licensed under the **MIT License**.

See [`LICENSE`](LICENSE) for the full license text.

---

##  Author

### Harman Dhadi

I'm interested in:

* Computer Science
* Software Development
* Artificial Intelligence
* Hardware & PC Building
* CAD & 3D Design
* IT
* Gaming & Technology

---

##  Future Plans

Potential future improvements include:

* Full Raspberry Pi deployment
* More Jarvis commands
* Additional MagicMirror modules
* Improved voice recognition
* More hardware integrations
* Custom physical enclosure
* Additional CAD designs
* More media controls
* Improved touchscreen UI

---


**HD-Tab — a personal smart display powered by AI.**
