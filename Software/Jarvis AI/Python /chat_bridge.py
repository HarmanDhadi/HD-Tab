import os
import json

FILE = "chat_messages.json"


def send_message(sender, message):

    data = {
        "sender": sender,
        "message": message
    }

    with open(FILE, "w") as f:
        json.dump(data, f)



def get_message():

    if os.path.exists(FILE):

        with open(FILE, "r") as f:
            data = json.load(f)

        os.remove(FILE)

        return data

    return None