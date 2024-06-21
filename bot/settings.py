import pathlib
import config

TOKEN = config.TOKEN
bitrate = 128
#bitrate modes: high=192; medium=128; low=64
stream = []
is_paused = False
playback = True

BASE_DIR = pathlib.Path(__file__).parent
CMDS_DIR = BASE_DIR / "cmds"
COGS_DIR = BASE_DIR / "cogs"

LOGO = """
 _   _                                        
| | | | __ _ _ __ _ __ ___   ___  _ __  _   _ 
| |_| |/ _` | '__| '_ ` _ \\ / _ \\| '_ \\| | | |
|  _  | (_| | |  | | | | | | (_) | | | | |_| |
|_| |_|\\__,_|_|  |_| |_| |_|\\___/|_| |_|\\__, |
                                        |___/
"""
