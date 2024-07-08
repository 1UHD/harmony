import pathlib
import config
import json


def get_json_value(value: str) -> any:
    with open(__file__.replace("\\", "/").replace("settings.py", "conf.json"), "r") as settingsfile:
        data = json.load(settingsfile)

        return data[value]

def set_json_values() -> None:
    with open(__file__.replace("\\", "/").replace("settings.py", "conf.json"), "w") as settingsfile:
        json.dump(settingsfile, {
            "streaming": streaming,
            "bitrate": bitrate,
            "bad_connection_mode": bad_connection_mode
        })

#token
TOKEN = config.TOKEN

#directories
BASE_DIR = pathlib.Path(__file__).parent
CMDS_DIR = BASE_DIR / "cmds"
COGS_DIR = BASE_DIR / "cogs"

#logo
LOGO = """
 _   _                                        
| | | | __ _ _ __ _ __ ___   ___  _ __  _   _ 
| |_| |/ _` | '__| '_ ` _ \\ / _ \\| '_ \\| | | |
|  _  | (_| | |  | | | | | | (_) | | | | |_| |
|_| |_|\\__,_|_|  |_| |_| |_|\\___/|_| |_|\\__, |
                                        |___/
"""

bitrate = get_json_value("bitrate")
#bitrate modes: high=192; medium=128; low=64
stream = []
currently_playing = "Nothing"

#bad connection mode instantly sends an embed when using /play and having streaming enabled to prevent the interaction from timing out while loading a song
bad_connection_mode = False

streaming = get_json_value("streaming")
playback = True
is_paused = False
is_looped = False

video_length = 0
starting_time = 0
time_elapsed = 0