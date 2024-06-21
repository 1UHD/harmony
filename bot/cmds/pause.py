import discord
import settings
from discord.ext import commands


@commands.hybrid_command(name="pause", description="Pauses the currently playing song.")
async def pause(ctx):   
    vc = ctx.voice_client

    if vc and vc.is_playing() and not settings.is_paused:
        vc.pause()
        settings.is_paused = True
        embed = discord.Embed(
            title="Song has been paused.",
            color=discord.Color.magenta()
        )
        await ctx.send(embed=embed)
    elif settings.is_paused:
        vc.resume()
        settings.is_paused = False
        embed = discord.Embed(
            title="The song has been resumed.",
            color=discord.Color.magenta()
        )
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title="No music is playing.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

async def setup(bot):
    bot.add_command(pause)