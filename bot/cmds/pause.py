import discord
from discord.ext import commands
import settings
import time
from cmds.utils.control_utils import *

@commands.hybrid_command(name="pause", description="Pauses the currently playing song.")
async def pause(ctx):
    if not ctx.voice_client:
        await send_error_embed(ctx, "Bot is not in a voice channel.")
        return

    if not ctx.voice_client.is_playing() and not settings.is_paused:
        await send_error_embed(ctx, "No song is playing.")
        return

    if not settings.is_paused:        
        ctx.voice_client.pause()
        settings.is_paused = True

        now = time.time()
        settings.time_elapsed = round(now - settings.starting_time)
        settings.starting_time = now

        await send_success_embed(ctx, "Song has been paused.")
    else:
        ctx.voice_client.resume()
        settings.is_paused = False

        settings.starting_time = time.time()

        await send_success_embed(ctx, "Song has been resumed.")

async def setup(bot):
    bot.add_command(pause)