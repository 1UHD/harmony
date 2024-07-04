import requests
from bs4 import BeautifulSoup
import re
import threading

def get_playlist_by_link(url: str):
    rep = requests.get(url)

    if rep.status_code != 200:
        return "unavailable"

    soup = BeautifulSoup(rep.text, "html.parser")

    title = str(soup.title.contents[0].split("-")[0])
    metas = soup.find_all("meta")
    links = []

    for meta in metas:
        match = re.findall(r'content="https://open.spotify.com/track/(.*?)"', str(meta))
        links.extend(match)

    return {"title": title, "songs": links}

def get_name_of_song(url: str):
    rep = requests.get(url)

    soup = BeautifulSoup(rep.text, "html.parser")
    titleheader = soup.title.contents[0]
    title = titleheader.split("-")[0]
    author = titleheader.split("song and lyrics by")[1].split("|")[0]

    return f"{author}- {title}"

def fetch_song_name(song_id, songs):
    song_name = get_name_of_song(f"https://open.spotify.com/track/{song_id}")
    songs.append(song_name)

def get_playlist_songs(playlist_url: str):
    playlist = get_playlist_by_link(playlist_url)
    playlist_title = playlist["title"]
    songs = []
    threads = []

    for song_id in playlist["songs"]:
        thread = threading.Thread(target=fetch_song_name, args=(song_id, songs), daemon=True)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return [playlist_title, songs]

playlist = get_playlist_songs("https://open.spotify.com/playlist/2ke9zwWFlmBpcfcRSAdcxv")
print(playlist[0])
print("\n".join(i for i in playlist[1]))