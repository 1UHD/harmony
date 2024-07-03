<div align="center">
    <img src="https://imgur.com/7Ohek0j.png" alt="harmony logo" width=150/>
    <h1>HARMONY
    <h3>free & open source Discord Music bot using yt-dlp
</div>

## Install
Make sure to have Python installed. After installing Python, you can clone this repository.
```sh
git clone https://github.com/1UHD/harmony.git
```
###
This bot is locally hosted, which means that you need to create the bot on your own. To do this, open the [Discord Developer Portal](https://discord.com/developers/applications) and create a new Application. Go to the Bot Tab and change the username, picture and banner to your liking. Our logo and banner can be found in the /bot/assets directory.
To add your bot to the server, navigate to the OAuth2 tab and tick "bot" in the OAuth2 URL Generator. Once you have done that, you can pick bot permissions. The Bot **needs** the following permissions:
<ul>
    <li>Read Messages/View Channels</li>
    <li>Send Messages</li>
    <li>Embed Links</li>
    <li>Connect</li>
    <li>Speak</li>
    <li>Priority Speaker (If you want the bot to have priority in voice calls)</li>
    <li>Use External Sounds</li>
</ul>

_If you're lazy just tick Adminstrator_ ;)
At the bottom, you can find a link. Copy it and paste it into your browser to add your bot to your server. Once you've done that, go back to the Bot tab and click on Reset Token. Copy your token and set up your bot.

###
To set up the bot, you can run the setup script. It will ask you to install [FFmpeg](https://ffmpeg.org/download.html) and [OPUS](https://opus-codec.org/). It will also ask you to paste your bot token that you've saved earlier.
```sh
python setup.py
```
(If you run into any problems, dm kurtiscool on Discord)

## Run the Discord bot
After your setup is done, run the main file and the bot will go online.
```sh
python bot/main.py
```