import discord
import settings
from discord.ext import commands

@commands.hybrid_command(name="playlist", description="Provides a list of queued songs.", aliases=["stream"])
async def playlist(ctx):
    if settings.stream:
        embed = discord.Embed(
            title="Current playlist:",
            description="\n".join(f"- {i}" for i in settings.stream),
            color=discord.Color.magenta()
        )
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title="Your playlist is empty.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

async def setup(bot):
    bot.add_command(playlist)