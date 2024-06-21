import discord
import settings
from discord.ext import commands

@commands.hybrid_command(name="bitrate", description="Changes the bitrate of song downloads.")
async def bitrate(ctx, bitrate: int = settings.bitrate):
    if bitrate == settings.bitrate:
        embed = discord.Embed(
            title=f"Current bitrate: {settings.bitrate}",
            color=discord.Color.magenta()
        )
        await ctx.send(embed=embed)
    else:
        settings.bitrate = bitrate
        embed = discord.Embed(
            title=f"Bitrate has been changed to {settings.bitrate}",
            color=discord.Color.magenta()
        )
        await ctx.send(embed=embed)

async def setup(bot):
    bot.add_command(bitrate)