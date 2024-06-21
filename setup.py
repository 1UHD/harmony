import os
import sys
import platform

def install(package):
    os.system(f"{sys.executable} -m pip install {package}")

try:
    import discord
    print("[SETUP] discord.py is installed.")
except ModuleNotFoundError:
    install("discord")
    print("[SETUP] Installed discord.py.")

try:
    import yt_dlp
    print("[SETUP] yt-dlp is installed.")
except ModuleNotFoundError:
    try:
        install("yt-dlp")
        print("[SETUP] Installed yt-dlp.")
    except:
        print("[SETUP] ffmpeg is missing. Install ffmpeg and re-run this script. (MacOS: brew install ffmpeg; Windows: install at https://ffmpeg.org/download.html)")
        sys.exit()

try:
    if platform.system() == "Darwin":
        discord.opus.load_opus("/opt/homebrew/Cellar/opus/1.5.2/lib/libopus.dylib")
    else:
        discord.opus.load_opus()
except:
    print("[SETUP] opus is missing. Install opus and re-run this script. (MacOS: brew install opus; Windows: install at https://opus-codec.org/)")
    sys.exit()

print(f"[SETUP] You're good to go. Start the bot using {sys.executable} bot/main.py. If you experience any issues, dm me on Discord: kurtiscool")