from bs4 import BeautifulSoup
from mutagen.mp3 import MP3
import settings
import requests
import yt_dlp
import os

def download_url(youtube_link: str) -> str:
    ylp_settings = {
            "format" : "bestaudio/best",
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': f'{settings.bitrate}',
            }],
            'outtmpl': __file__.replace("\\", "/").replace("bot/cmds/utils/youtube_utils.py", "downloaded") + "/%(title)s.%(ext)s",
        }
    try:
        with yt_dlp.YoutubeDL(ylp_settings) as ydl:
            ydl.download([youtube_link])
        return "success"
    except yt_dlp.utils.DownloadError:
        return "unavailable"
    except Exception as e:
        return str(e)

def check_video_name(youtube_link: str) -> str:
    try:
        vid = requests.get(youtube_link)
    except Exception as e:
        return str(e)
    soup = BeautifulSoup(vid.text, features="html.parser")

    link = soup.find_all(name="title")[0]
    title = link.text
    title = title.replace(" - YouTube", "")

    if title == "":
        return "unavailable"

    return title

def check_if_already_downloaded(youtube_link: str) -> bool:
    title = check_video_name(youtube_link=youtube_link)
    if title == "unavailable":
        return [False, "unavailable"]

    if os.path.exists(__file__.replace("\\", "/").replace("bot/cmds/utils/youtube_utils.py", "downloaded") + "/" + title + ".mp3"):
        return [True, title]
    else:
        return [False, "unavailable"]

def get_youtube_thumbnail(youtube_link: str) -> str:
    video_id = youtube_link.replace("https://www.youtube.com/watch?v=", "")
    return f"http://img.youtube.com/vi/{video_id}/hqdefault.jpg"

def get_video_length(name: str) -> int:
    audio = MP3( __file__.replace("\\", "/").replace("bot/cmds/utils/youtube_utils.py", "downloaded/") + name + ".mp3")
    return audio.info.length