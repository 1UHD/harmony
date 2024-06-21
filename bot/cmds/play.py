import discord
import settings
from discord.ext import commands
from settings import stream
import os

if not discord.opus.is_loaded():
    #discord.opus.load_opus('libopus.so' if os.name != 'nt' else 'opus.dll')
    discord.opus.load_opus("/opt/homebrew/Cellar/opus/1.5.2/lib/libopus.dylib")

@commands.hybrid_command(name="play", description="Joins your voice channel and starts playing your playlist.")
async def play(ctx):

    if ctx.author.voice:
        try:
            vc = await ctx.author.voice.channel.connect()
        except discord.errors.ClientException:
            vc = ctx.voice_client
            print("[DEBUG] already in vc, playing music now.")

        if not vc.is_playing() and stream:
            settings.playback = True
            await play_next_song(ctx, vc)
        elif not stream and not vc.is_playing():
            embed = discord.Embed(
                title="Your playlist is empty.",
                description="Use /play again once you added some songs.",
                color=discord.Color.gold()
            )
            await ctx.send(embed=embed)
        elif vc.is_playing():
            embed = discord.Embed(
                title="Bot already playing.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        
    else:
        embed = discord.Embed(
            title="You're not in a voice call.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        
async def play_next_song(ctx, vc):
    if not settings.playback:
        return

    try:
        audio = discord.FFmpegPCMAudio(source=__file__.replace("bot/cmds/play.py", "downloaded/") + stream[0] + ".mp3")
    except Exception as e:
        embed = discord.Embed(
            title="No songs are in queue.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

    if not vc.is_playing():
        try:
            vc.play(audio, after=lambda e: ctx.bot.loop.create_task(play_next_song(ctx, vc)))
        except Exception as e:
            print(f"[DEBUG] playlist empty")

        embed = discord.Embed(
            title="Song playing:",
            description=f"{stream[0]}",
            color=discord.Color.magenta()
        )

        del stream[0]
        await ctx.send(embed=embed)


        

async def setup(bot):
    bot.add_command(play)