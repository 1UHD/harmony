from cmds.utils.youtube_utils import check_if_already_downloaded
from cmds.utils.youtube_utils import check_video_name
from cmds.utils.youtube_utils import download_url
from cmds.utils.youtube_utils import get_youtube_thumbnail
from settings import bitrate
from settings import stream
import discord
from discord.ext import commands

@commands.hybrid_command(name="add", description="Adds music to the current playlist")
async def add(ctx, url):
    already_downloaded = check_if_already_downloaded(url)
    if already_downloaded[0]:
        video_name = already_downloaded[1]
        stream.append(video_name)

        embed = discord.Embed(
            title="Added song to playlist.",
            description=f"Name: {video_name}",
            color=discord.Color.magenta()
        )
        embed.set_thumbnail(url=get_youtube_thumbnail(url))
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title="Downloading song...",
            description=f"The song is being downloaded.\nBitrate: {bitrate}",
            color=discord.Color.gold()
        )
        await ctx.send(embed=embed)

        rep = download_url(url)
        if rep == "success":
            video_name = check_video_name(url)
            stream.append(video_name)

            embed = discord.Embed(
                title="Song has been downloaded.",
                description=f"The song has been downloaded and added to your playlist.\nName: {video_name}",
                color=discord.Color.magenta()
            )
            embed.set_thumbnail(url=get_youtube_thumbnail(url))
            await ctx.send(embed=embed)
        elif rep == "unavailable":
            embed = discord.Embed(
                title="Video unavailable.",
                description="This video is not available. Check the URL.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Unexpected error.",
                description="An unexpected error has occured.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

async def setup(bot):
    bot.add_command(add)