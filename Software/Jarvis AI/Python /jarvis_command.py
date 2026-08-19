import os

FILE = "open_chat.txt"


def open_chat_signal():
    with open(FILE, "w") as f:
        f.write("open")


def check_signal():

    if os.path.exists(FILE):

        os.remove(FILE)

        return True

    return False