import discord
from settings import CMDS_DIR, COGS_DIR, TOKEN, LOGO
import colorama as col
from discord.ext import commands
import atexit

async def exit_handler() -> None:
    for voice_client in bot.voice_clients:
        await voice_client.disconnect()

    print("[DEBUG] Disconnected all voice clients before exiting to prevent errors.")

def run() -> None:
    intents = discord.Intents.all()
    activity = discord.Game("/help")

    global bot
    bot = commands.Bot(command_prefix=".", activity=activity, intents=intents, help_command=None, case_insensitive=False)

    @bot.event
    async def on_ready():
        print(col.Fore.MAGENTA + LOGO)
        print(f"{col.Fore.CYAN}Bot{col.Style.RESET_ALL}: {bot.user} ({bot.user.id})")
        
        for cmd_file in CMDS_DIR.glob("*.py"):
            if cmd_file.name != "__init__.py":
                await bot.load_extension(f"cmds.{cmd_file.name[:-3]}")
                print(f"[DEBUG] Loaded CMD: {cmd_file.name[:-3]}")

        for cog_file in COGS_DIR.glob("*.py"):
            if cog_file.name != "__init__.py":
                await bot.load_extension(f"cogs.{cog_file.name[:-3]}")
                print(f"[DEBUG] Loaded COG: {cog_file.name[:-3]}")

        await bot.tree.sync()
        print("[DEBUG] bot tree synched")

    bot.run(TOKEN)

if __name__ == "__main__":
    run()
