import pathlib
import config

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

bitrate = 128
#bitrate modes: high=192; medium=128; low=64
stream = []
currently_playing = "Nothing"

playback = True
is_paused = False
is_looped = False

starting_time = 0
time_elapsed = 0