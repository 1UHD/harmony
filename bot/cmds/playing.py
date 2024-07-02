import discord
from discord.ext import commands
import settings
from cmds.utils.control_utils import send_error_embed

#TODO: make this work (I am lacking WiFi to look up any tutorial. I also don't even know if it works or not, but my guts tell me it doesn't.)
class Buttons(discord.ui.View):
    def __init__(self, embed):
        self.embed = embed

    @discord.ui.button(label=":pause_button:", style=discord.ButtonStyle.green)
    async def pause(self, button: discord.ui.Button, interaction: discord.Interaction):
        if not settings.is_paused:
            interaction.voice_client.pause()
            button.label = ":arrow_forward:"
            settings.is_paused = True
        else:
            interaction.voice_client.resume()
            button.label = ":pause_button:"
            settings.is_paused = False

        await interaction.message.edit(embed=self.embed, view=self)


@commands.hybrid_command(name="playing", description="Gives information on the song that is currently playing.")
async def playing(ctx):
    if not ctx.voice_client:
        await send_error_embed(ctx, "Bot is not in a voice channel.")
        return

    if not ctx.voice_client.is_playing():
        await send_error_embed(ctx, "No song is playing.")
        return

    embed = discord.Embed(
        title="Currently playing:",
        description=f"**{settings.currently_playing}**\n_Loop:_ {'yes' if settings.is_looped else 'no'} | _Paused:_ {'yes' if settings.is_paused else 'no'}",
        color=discord.Color.magenta()
    )

    #view = Buttons(embed)

    await ctx.send(embed=embed)

async def setup(bot):
    bot.add_command(playing)