import discord
from discord.ext import commands

@commands.hybrid_command(name="help", description="Gives a list of commands.")
async def help(ctx):
    embed = discord.Embed(
        title="HARMONY",
        color=discord.Color.orange()
    )

    await ctx.send(embed=embed)

async def setup(bot):
    bot.add_command(help)