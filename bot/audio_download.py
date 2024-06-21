from bs4 import BeautifulSoup
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
            'outtmpl': f'{__file__.replace("\\", "/").replace("audio/audio_download.py", "downloaded").replace("bot/audio_download.py", "downloaded")}/%(title)s.%(ext)s',
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

    if os.path.exists(__file__.replace("\\", "/").replace("audio/audio_download.py", "downloaded").replace("bot/audio_download.py", "downloaded") + "/" + title + ".mp3"):
        return [True, title]
    else:
        return [False, "unavailable"]