import discord
from discord.ext import commands
import settings
import sys
import time
import platform
from cmds.utils.control_utils import *
from cmds.utils.youtube_utils import stream_audio

def load_opus():
    try:
        if platform.system() == "Darwin":
            discord.opus.load_opus("/opt/homebrew/Cellar/opus/1.5.2/lib/libopus.dylib")
        elif platform.system() == "Windows":
            discord.opus.load_opus("C:\\Windows\\System32\\opus.dll")
        else:
            print("[DEBUG] you're on linux, figure it out how to load opus yourself (replace this (in /bot/cmds/play.py) with discord.opus.load_opus('path to opus') and remove the sys.exit()), exiting...")
            sys.exit()
    except Exception as e:
        print("[DEBUG] OPUS could not be loaded, exiting...")
        sys.exit()

load_opus()

async def stream_next_song(ctx, vc):
    if not settings.playback:
        return

    if not settings.stream:
        await send_error_embed(ctx, "Stopping. No songs in queue.")
        return

    if settings.bad_connection_mode:
        message = await ctx.send(embed=discord.Embed(
            title="Song is loading.",
            description="This might take a while. Bad connection mode is enabled.\n",
            color=discord.Color.gold()
        ))

    if not settings.is_looped:
        print("this got executed (1)")
        d = stream_audio(f"https://www.youtube.com/watch?v={settings.stream[0].split('|')[1]}")
        print("this god executed too (heyyy)")
        audio = d[0]
        settings.video_length = d[1]

        settings.currently_playing = settings.stream[0]
        del settings.stream[0]
        await  ctx.send("if u see this and the song u want isnt playing then sum ting is wong")
    else:
        d = stream_audio(f"https://www.youtube.com/watch?v={settings.currently_playing.split('|')[1]}")
        audio = d[0]
        settings.video_length = d[1]

    if not vc.is_playing():
        settings.starting_time = time.time()
        settings.time_elapsed = 0
        vc.play(audio, after=lambda e: ctx.bot.loop.create_task(stream_next_song(ctx, vc)))

    embed = discord.Embed(
        title="Song playing:",
        description=f"{settings.currently_playing.split('|')[0]}",
        color=discord.Color.magenta()
    )

    if not settings.bad_connection_mode:
        await ctx.send(embed=embed)
    else:
        await message.edit(embed=embed)

async def play_next_song(ctx, vc):
    if not settings.playback:
        return

    if not settings.stream:
        await send_error_embed(ctx, "Stopping. No songs in queue.")
        return

    if not settings.is_looped:
        audio = discord.FFmpegPCMAudio(source=__file__.replace("\\", "/").replace("bot/cmds/play2.py", "downloaded/") + settings.stream[0] + ".mp3")
        settings.currently_playing = settings.stream[0]
        del settings.stream[0]
    else:
        audio = discord.FFmpegPCMAudio(source=__file__.replace("\\", "/").replace("bot/cmds/play2.py", "downloaded/") + settings.currently_playing + ".mp3")

    if not vc.is_playing():
        settings.starting_time = time.time()
        settings.time_elapsed = 0
        vc.play(audio, after=lambda e: ctx.bot.loop.create_task(play_next_song(ctx, vc)))

        embed = discord.Embed(
            title="Song playing:",
            description=f"{settings.currently_playing.split('|')[0]}",
            color=discord.Color.magenta()
        )

        await ctx.send(embed=embed)

@commands.hybrid_command(name="play", description="Joins your voice channel and starts playing your playlist.")
async def play(ctx):
    if not ctx.author.voice:
        await send_error_embed(ctx, "You're not in a voice channel.")
        return

    if not ctx.voice_client:
        await ctx.author.voice.channel.connect()


    if ctx.voice_client.channel is not ctx.author.voice.channel:
        await ctx.voice_client.disconnect()
        await ctx.author.voice.channel.connect()


    if not ctx.voice_client.is_playing() and settings.stream:
        settings.playback = True

        if not settings.streaming:
            await play_next_song(ctx, ctx.voice_client)
        
        else:
            await stream_next_song(ctx, ctx.voice_client)


    elif not ctx.voice_client.is_playing() and not settings.stream:
        await send_progress_embed(ctx, "Playlist is empty.")
        return

    else:
        await send_error_embed(ctx, "Bot is already playing.")
        return

async def setup(bot):
    bot.add_command(play)