import speech_recognition as sr
import subprocess
import sounddevice as sd
import soundfile as sf
import threading
import time
import datetime
import requests
import json

from zoneinfo import ZoneInfo
from gemini import ask_gemini

from youtube_player import (
    play_youtube,
    pause_youtube,
    resume_youtube,
    stop_youtube,
    lower_music_volume,
    restore_music_volume
)


recognizer = sr.Recognizer()

recognizer.energy_threshold = 300
recognizer.pause_threshold = 1.2
recognizer.dynamic_energy_threshold = True


speaking = False


OPEN_FILE = "open_chat.txt"
MESSAGE_FILE = "chat_messages.json"



def send_chat(sender, text):

    with open(MESSAGE_FILE, "w") as f:

        json.dump(
            {
                "sender": sender,
                "text": text
            },
            f
        )



def open_chat():

    with open(OPEN_FILE, "w") as f:

        f.write("open")



def get_time():

    now = datetime.datetime.now(
        ZoneInfo("America/Toronto")
    )

    return now.strftime(
        "It is %I:%M %p on %A, %B %d, %Y"
    )



def get_weather():

    try:

        url = (
            "https://api.open-meteo.com/v1/forecast"
            "?latitude=43.7315"
            "&longitude=-79.7624"
            "&current=temperature_2m,weather_code"
            "&temperature_unit=celsius"
        )


        data = requests.get(url).json()


        temp = data["current"]["temperature_2m"]

        code = data["current"]["weather_code"]


        conditions = {

            0:"clear skies",
            1:"mostly clear",
            2:"partly cloudy",
            3:"cloudy",
            61:"rain",
            63:"heavy rain",
            71:"snow",
            80:"showers"

        }


        weather = conditions.get(
            code,
            "unknown conditions"
        )


        return (
            f"It is currently {temp} "
            f"degrees Celsius in Brampton "
            f"with {weather}."
        )


    except:

        return "I cannot get the weather right now."



def listen_for_stop():

    global speaking


    while speaking:

        try:

            with sr.Microphone() as source:

                audio = recognizer.listen(
                    source,
                    timeout=1,
                    phrase_time_limit=2
                )


            command = recognizer.recognize_google(
                audio
            ).lower()


            if "stop" in command:

                sd.stop()

                speaking = False

                break


        except:

            pass



def speak(text):

    global speaking


    print(
        "Jarvis:",
        text
    )


    send_chat(
        "ai",
        "Jarvis: " + text
    )


    try:

        lower_music_volume()

    except:

        pass



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


    audio, samplerate = sf.read(
        "jarvis.wav"
    )


    speaking = True


    threading.Thread(
        target=listen_for_stop,
        daemon=True
    ).start()



    sd.play(
        audio,
        samplerate
    )


    sd.wait()


    speaking = False



    try:

        restore_music_volume()

    except:

        pass




def listen():

    with sr.Microphone() as source:

        print("Listening...")


        audio = recognizer.listen(
            source,
            phrase_time_limit=12
        )


    try:

        text = recognizer.recognize_google(
            audio
        )


        print(
            "You:",
            text
        )


        return text.lower()


    except:

        return ""




def think(question):


    if "time" in question or "date" in question:

        return get_time()



    if "weather" in question or "temperature" in question:

        return get_weather()



    if "pause" in question:

        return pause_youtube()



    if "resume" in question:

        return resume_youtube()



    if "stop music" in question:

        return stop_youtube()



    if "play" in question or "youtube" in question:


        song = question.replace(
            "youtube",
            ""
        ).replace(
            "play",
            ""
        ).strip()



        if song:

            return play_youtube(song)



        return "What would you like me to play?"



    return ask_gemini(question)





def main():

    while True:


        command = listen()


        if command and "jarvis" in command:


            open_chat()


            question = command.replace(
                "hey jarvis",
                ""
            ).replace(
                "jarvis",
                ""
            ).strip()



            if question:


                send_chat(
                    "user",
                    "You: " + question
                )


                answer = think(
                    question
                )


                speak(
                    answer
                )


            else:

                speak(
                    "Yes?"
                )



        time.sleep(0.2)





if __name__ == "__main__":

    main()