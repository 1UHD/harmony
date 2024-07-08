import discord
from discord.ext import commands
import settings
from cmds.utils.control_utils import send_error_embed
from cmds.utils.youtube_utils import get_video_length
import time
import math

def seconds_to_time_format(seconds):
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes}:{seconds:02}"

def get_elapsed_time_string():
    elapsed_time = 0

    if not settings.streaming:
        song_length = math.ceil(get_video_length(settings.currently_playing))
    else:
        song_length = math.ceil(settings.video_length)

    if settings.is_paused:
        elapsed_time = settings.time_elapsed
    else:
        elapsed_time = round(time.time() - settings.starting_time) + settings.time_elapsed

    try:
        progress = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        progress_index = math.ceil(elapsed_time / (song_length / 15)) - 1
        progress[progress_index] = "o"

        return f"{seconds_to_time_format(elapsed_time)} {''.join(i for i in progress)} {seconds_to_time_format(song_length)}"
    except Exception as e:
        return f"ERROR: elapsed: {elapsed_time} | length: {song_length}"


@commands.hybrid_command(name="playing", description="Gives information on the song that is currently playing.")
async def playing(ctx):
    if not ctx.voice_client:
        await send_error_embed(ctx, "Bot is not in a voice channel.")
        return

    if not ctx.voice_client.is_playing() and not settings.is_paused:
        await send_error_embed(ctx, "No song is playing.")
        return

    embed = discord.Embed(
        title="Currently playing:",
        description=f"**{settings.currently_playing.split('|')[0]}**\n{get_elapsed_time_string()}\n_Loop:_ {'yes' if settings.is_looped else 'no'} | _Paused:_ {'yes' if settings.is_paused else 'no'}",
        color=discord.Color.magenta()
    )

    await ctx.send(embed=embed)

async def setup(bot):
    bot.add_command(playing)