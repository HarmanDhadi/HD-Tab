import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav


sample_rate = 44100
seconds = 5

print("Recording...")

audio = sd.rec(
    int(seconds * sample_rate),
    samplerate=sample_rate,
    channels=1
)

sd.wait()

print("Finished!")

wav.write(
    "test.wav",
    sample_rate,
    audio
)

print("Saved as test.wav")