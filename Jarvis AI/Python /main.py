import subprocess
import sys
import time
import os


folder = os.path.dirname(os.path.abspath(__file__))


interface = subprocess.Popen(
    [
        sys.executable,
        os.path.join(folder, "interface.py")
    ]
)


time.sleep(2)


voice = subprocess.Popen(
    [
        sys.executable,
        os.path.join(folder, "voice.py")
    ]
)


try:

    interface.wait()
    voice.wait()


except KeyboardInterrupt:

    print("Closing Jarvis...")

    interface.terminate()
    voice.terminate()