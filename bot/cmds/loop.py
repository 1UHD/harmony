import discord
from discord.ext import commands
import settings
from cmds.utils.control_utils import send_error_embed, send_success_embed

@commands.hybrid_command(name="loop", description="Loops the song that is currently playing.")
async def loop(ctx):
    if not ctx.voice_client:
        await send_error_embed(ctx, "Bot is not in a voice channel.")
        return

    if not ctx.voice_client.is_playing():
        await send_error_embed(ctx, "Can't loop because there's no song playing.")
        return
    
    if settings.is_looped:
        settings.is_looped = False
        await send_success_embed(ctx, f"Unlooped {settings.currently_playing.split('<|||>')[0]}")
    else:
        settings.is_looped = True
        await send_success_embed(ctx, f"Looped {settings.currently_playing.split('<|||>')[0]}")
    
async def setup(bot):
    bot.add_command(loop)
