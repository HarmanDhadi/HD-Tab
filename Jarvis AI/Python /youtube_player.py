import yt_dlp
import vlc


player = None
old_volume = 100



def play_youtube(query):

    global player


    # Stop previous song
    if player:

        player.stop()

        try:
            player.release()
        except:
            pass

        player = None



    url = "ytsearch1:" + query


    ydl_opts = {

        "format": "bestaudio/best",

        "quiet": True,

        "noplaylist": True,

        "js_runtimes": {
            "deno": {}
        },

        "extractor_args": {

            "youtube": {

                "player_client": [
                    "default"
                ]

            }

        }

    }



    try:

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:

            info = ydl.extract_info(
                url,
                download=False
            )


        if not info or "entries" not in info:

            return "I couldn't find that song."


        if len(info["entries"]) == 0:

            return "I couldn't find that song."


        video = info["entries"][0]


        audio_url = video["url"]



    except Exception as e:

        print("YouTube error:", e)

        return "I had trouble finding that song."



    player = vlc.MediaPlayer(
        audio_url,
        "--no-video"
    )


    player.audio_set_volume(
        100
    )


    player.play()


    return f"Playing {video['title']}"





def pause_youtube():

    if player:

        player.pause()

        return "Paused the music."


    return "Nothing is playing."





def resume_youtube():

    if player:

        player.play()

        return "Resuming music."


    return "Nothing is paused."





def stop_youtube():

    global player


    if player:

        player.stop()

        try:
            player.release()
        except:
            pass


        player = None

        return "Stopped the music."


    return "Nothing is playing."





def lower_music_volume():

    global old_volume


    if player:

        old_volume = player.audio_get_volume()

        player.audio_set_volume(20)





def restore_music_volume():

    if player:

        player.audio_set_volume(
            old_volume
        )