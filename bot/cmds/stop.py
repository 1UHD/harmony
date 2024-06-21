import discord
import settings
from discord.ext import commands

@commands.hybrid_command(name="stop", description="Stops the music.", aliases=["stfu"])
async def stop(ctx):
    if ctx.voice_client:
        ctx.voice_client.stop()
        await ctx.voice_client.disconnect()
        settings.is_paused = False
        settings.playback = False
        embed = discord.Embed(
            title="Stopped music.",
            color=discord.Color.magenta()
        )
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title="The bot is not playing.",
            color=discord.Color.magenta()
        )
        await ctx.send(embed=embed)

async def setup(bot):
    bot.add_command(stop)