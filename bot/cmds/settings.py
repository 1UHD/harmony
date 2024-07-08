import discord
from discord import app_commands
from discord.ext import commands
import settings
from cmds.utils.control_utils import *

@commands.hybrid_group(name="settings", description="Changes the settings for the bot.")
async def settingscmd(ctx):
    await ctx.send(embed=discord.Embed(
        title="Wrong usage.",
        description="Usage:\n/settings bitrate <bitrate>\n/settings streaming <enable/disable>\n/settings bad_connection_mode <enable/disable>",
        color=discord.Color.red()
    ))

@settingscmd.command(name="bitrate", description="Changes the bitrate of downloaded and streamed music.")
async def bitrate(ctx, bitrate = None):
    if not bitrate or bitrate == settings.bitrate:
        await send_success_embed(ctx, f"Current bitrate: {settings.bitrate}.")
    else:
        settings.bitrate = bitrate
        await send_success_embed(ctx, f"Bitrate has been changed to {settings.bitrate}.")

@settingscmd.command(name="streaming", description="Toggles streaming mode.")
@app_commands.choices(streaming = [
    app_commands.Choice(name="enable", value=1),
    app_commands.Choice(name="disable", value=0)
])
async def streaming(ctx, streaming: int):
    if streaming == 1:
        streaming = True
    else:
        streaming = False

    if streaming == settings.streaming:
        await send_success_embed(ctx, f"Streaming is currently {'enabled' if settings.streaming else 'disabled'}.")
    else:
        settings.streaming = streaming
        await send_success_embed(ctx, f"Streaming has been {'enabled' if settings.streaming else 'disabled'}.")

@settingscmd.command(name="bad_connection_mode", description="Bad connection mode makes sure that no bugs occur while streaming with bad internet connection.")
@app_commands.choices(bad_connection_mode = [
    app_commands.Choice(name="enable", value=1),
    app_commands.Choice(name="disable", value=0)
])
async def bad_connection_mode(ctx, bad_connection_mode: int):
    if bad_connection_mode == 1:
        bad_connection_mode = True
    else:
        bad_connection_mode = False

    if bad_connection_mode == settings.bad_connection_mode:
        await send_success_embed(ctx, f"Bad connection mode is currently {'enabled' if settings.bad_connection_mode else 'disabled'}.")
    else:
        settings.bad_connection_mode = bad_connection_mode
        await send_success_embed(ctx, f"Bad connection mode has been {'enabled' if settings.bad_connection_mode else 'disabled'}.")

async def setup(bot):
    bot.add_command(settingscmd)