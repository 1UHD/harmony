from cmds.utils.youtube_utils import *
from cmds.utils.control_utils import send_error_embed, send_progress_embed, send_success_embed
from settings import bitrate, stream
import discord
from discord.ext import commands

@commands.hybrid_group(name="add2")
async def add(ctx):
    await ctx.send(embed=discord.Embed(
        title="Wrong usage.",
        description="Usage:\n/add youtube_url <url>\n/add search <title>",
        color=discord.Color.red()
    ))

@add.command(name="youtube_url", description="Adds an audio via a YouTube url.")
async def youtube_url(ctx, url):
    already_downloaded = check_if_already_downloaded(url)

    if already_downloaded[0]:
        video_name = already_downloaded[1]
        stream.append(video_name)

        await send_success_embed(ctx, f"Added {video_name} to stream.")

    else:
        await send_progress_embed(ctx, f"Downloading song. Bitrate: {bitrate}")

        rep = download_url(url)

        if rep == "success":
            video_name = check_video_name(url)
            stream.append(video_name)

            embed = discord.Embed(
                title="Song added to stream.",
                description=f"{video_name}",
                color=discord.Color.magenta()
            )
            embed.set_thumbnail(url=get_youtube_thumbnail(url))
            await ctx.send(embed=embed)

        elif rep == "unavailable":
            await send_error_embed(ctx, "Video couldn't be found.")
            return

        else:
            await send_error_embed(ctx, "An unknown error occured.")
            return

@add.command(name="search", description="Searches your title on YouTube and adds the first result.")
async def search(ctx: commands.Context, title):
    await send_progress_embed(ctx, f"Searching for {title}")
    result = search_youtube(title)
    already_downloaded = check_if_already_downloaded(result)

    if already_downloaded[0]:
        video_name = already_downloaded[1]
        stream.append(video_name)

        await send_success_embed(ctx, f"Added {video_name} to stream.")

    else:
        await send_progress_embed(ctx, f"Downloading song. Bitrate: {bitrate}")

        rep = download_url(result)

        if rep == "success":
            video_name = check_video_name(result)
            stream.append(video_name)

            embed = discord.Embed(
                title="Song added to stream.",
                description=f"{video_name}",
                color=discord.Color.magenta()
            )
            embed.set_thumbnail(url=get_youtube_thumbnail(result))
            await ctx.send(embed=embed)

        elif rep == "unavailable":
            await send_error_embed(ctx, "Video couldn't be found.")
            return

        else:
            await send_error_embed(ctx, "An unknown error occured.")
            return

async def setup(bot):
    bot.add_command(add)