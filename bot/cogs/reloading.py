import discord
from settings import CMDS_DIR, COGS_DIR
from discord.ext import commands
import sys
from cmds.utils.control_utils import send_success_embed

class reloading_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="reload", description="Reloads all commands.")
    async def reload(self, ctx):

        for cmd_file in CMDS_DIR.glob("*.py"):
            if cmd_file.name != "__init__.py":
                await self.bot.unload_extension(f"cmds.{cmd_file.name[:-3]}")
                print(f"[DEBUG] Unloading command: {cmd_file.name[:-3]}")

        for cog_file in COGS_DIR.glob("*.py"):
            if cog_file.name != "__init__.py":
                await self.bot.unload_extension(f"cogs.{cog_file.name[:-3]}")
                print(f"[DEBUG] Unloading category: {cog_file.name[:-3]}")

        for cmd_file in CMDS_DIR.glob("*.py"):
            if cmd_file.name != "__init__.py":
                await self.bot.load_extension(f"cmds.{cmd_file.name[:-3]}")
                print(f"[DEBUG] Reloading command: {cmd_file.name[:-3]}")

        for cog_file in COGS_DIR.glob("*.py"):
            if cog_file.name != "__init__.py":
                await self.bot.load_extension(f"cogs.{cog_file.name[:-3]}")
                print(f"[DEBUG] Reloading category: {cog_file.name[:-3]}")
        
        embed = discord.Embed(
            title="Reloaded.",
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)

    @commands.hybrid_command(name="reloadbottree", description="Reloads the bot tree.")
    async def reloadbottree(self, ctx):
        embed = discord.Embed(
            title="Reloaded bot tree.",
            color=discord.Color.green()
        )
        await self.bot.tree.sync()
        print("[SYSTEM] Bot tree reloaded")
        await ctx.send(embed=embed)

    @commands.hybrid_command(name="shutdown", description="Shuts down the bot.")
    async def shutdown(self, ctx):
        for voice_client in self.bot.voice_clients:
            await voice_client.disconnect()

        await send_success_embed(ctx, "Shutting down.")
        sys.exit()

async def setup(bot):
    await bot.add_cog(reloading_commands(bot))