import discord
import settings
from discord.ext import commands

@commands.hybrid_command(name="stream", description="Provides a list of queued songs.")
async def stream(ctx):
    if settings.stream:
        embed = discord.Embed(
            title="Current playlist:",
            description=f"**{settings.currently_playing}**" + "".join('_(Looped)_\n' if settings.is_looped else '\n') + "\n".join(f"- {i}" for i in settings.stream),
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
    bot.add_command(stream)