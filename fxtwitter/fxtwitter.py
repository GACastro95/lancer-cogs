import discord
from discord.ui import View
import re
import discord.ext
from redbot.core import commands
from typing import Optional

class ButtonMenu(View):
    def __init__(self, timeout, member):
        super().__init__(timeout=timeout)
        self.member = member
        self.value = None

    @discord.ui.button(style=discord.ButtonStyle.red, emoji="🗑")
    async def delete(self, interaction, button):
        if interaction.user.id != self.member.id:
            await interaction.response.send_message(
                ("You are not the author of this command."), ephemeral=True
            )
        await interaction.response.defer()
        await interaction.delete_original_response()


         
class FxTwitter(commands.Cog):
    """Converts twitter links to Fxtwitter links"""
    @commands.hybrid_command()
    async def twitter(self, ctx, url, download: Optional[bool] = False):
        """Returns Fxtwitter Link."""
        if download:
                subst = "https://dl.fxtwitter.com"
        else:
            subst = "https://fxtwitter.com"
        regex = r"((https?):\/\/)?(www.)?(x|twitter?)\.com(\/@?(\w){1,15})\/status\/[0-9]{19}"
        matches = re.search(regex, url)
        if matches:
            regex_rm = r"((https?):\/\/)?(www.)?(x|twitter?)\.com"
            result = re.sub(regex_rm, subst, url.split("?")[0], 1)
            menu = ButtonMenu(timeout=None, member=ctx.author)
            await ctx.send(result, view=menu)
        else:
            await ctx.send("This is not a tweet", ephemeral=True)
