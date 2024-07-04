import discord
from discord.ext import commands


async def send_error_embed(ctx, title: str) -> None:
    embed = discord.Embed(
        title=title,
        color=discord.Color.red()
    )
    await ctx.send(embed=embed)

async def send_success_embed(ctx, title: str) -> None:
    embed = discord.Embed(
        title=title,
        color=discord.Color.magenta()
    )
    await ctx.send(embed=embed)

async def send_progress_embed(ctx, title: str) -> None:
    embed = discord.Embed(
        title=title,
        color=discord.Color.gold()
    )
    await ctx.send(embed=embed)

async def check_for_voice(ctx) -> bool:
    if not ctx.author.voice:
        embed = discord.Embed(
            title="You're not in a voice channel.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

        return False
    else:
        return True

async def check_playing(ctx) -> bool:
    if not ctx.voice_client.is_playing():
        return False
    else:
        return True

async def join_vc(ctx) -> bool:
    if check_for_voice(ctx=ctx) and not ctx.voice_client:
        ctx.author.voice.channel.connect()
        return True
    else:
        return False