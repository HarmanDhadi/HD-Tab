import subprocess
from playsound3 import playsound

text = "Hello! I am Jarvis, how may i help you today? Feel Free to ask whatever!"

subprocess.run(
    [
        "piper",
        "--model",
        "en_US-joe-medium",
        "--output_file",
        "jarvis.wav"
    ],
    input=text.encode()
)

playsound("jarvis.wav")