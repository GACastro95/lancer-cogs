import discord
from discord.ui import Button, View
import re
from redbot.core import commands
from typing import Optional

class CustomView(discord.ui.view):
    def __init__(self):
        super().__init__()
        self.message = None

@discord.ui.button(label="Click")
async def click(self, interaction, button):
    await interaction.response.send_message("Clicked!")
    if self.message is not None:
        await self.message.edit(view=None)  

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
            view = CustomView()
            await ctx.send(result, view=view)
        else:
            await ctx.send("This is not a tweet", ephemeral=True)
