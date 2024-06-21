import discord
from discord.ext import commands

@commands.hybrid_command(name="skip", description="Skips the currently playing song.")
async def skip(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.stop()
        embed = discord.Embed(
            title="Skipped song.",
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
    bot.add_command(skip)