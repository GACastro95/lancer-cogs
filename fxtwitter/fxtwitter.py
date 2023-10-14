import discord
from discord.ui import Button, View
import re
from redbot.core import commands
from typing import Optional

class ButtonMenu(View):
    def __init__(self):
        super().__init__()

        # Create buttons
        self.button1 = Button(style=discord.ButtonStyle.primary, label="Button 1")
        self.button2 = Button(style=discord.ButtonStyle.primary, label="Button 2")

        # Add buttons to the view
        self.add_item(self.button1)
        self.add_item(self.button2)

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
            menu = ButtonMenu()
            await ctx.send(result, view=menu)
        else:
            await ctx.send("This is not a tweet", ephemeral=True)
