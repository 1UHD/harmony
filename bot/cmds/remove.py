import discord
from discord.ext import commands
import settings
from cmds.utils.control_utils import send_error_embed, send_success_embed

@commands.hybrid_command(name="remove", description="Removes a song from the current queue.")
async def remove(ctx, index: int):
    if index > len(settings.stream):
        await send_error_embed("That song does not exist.")
        return

    del settings.stream[index - 1]
    await send_success_embed(f"Song {index} has been removed.")

async def setup(bot):
    bot.add_command(remove)