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
        """Returns fxTwitter Link."""
        if download:
                subst = "dl.fxtwitter"
        else:
            subst = "fxtwitter"
        regex = r"((https?):\/\/)?(www.)?(x|twitter)\.com(\/@?(\w){1,15})\/status\/[0-9]{19}"
        matches = re.search(regex, url)
        if matches:
            regex_rm = r"(x|twitter)"
            result = re.sub(regex_rm, subst, url.split("?")[0], 1)
            menu = ButtonMenu(timeout=None, member=ctx.author)
            await ctx.send(result, view=menu)
        else:
            await ctx.send("This is not a valid tweet", ephemeral=True)

    
    @commands.hybrid_command()
    async def tiktok(self, ctx, url):
        """Returns fxTikTok Link."""
        regex = r"((https?):\/\/)?((vm|www?).)?(tiktok)\.com\/(@?.*?)\/(video)?(\/[0-9]{19})?"
        matches = re.search(regex, url)
        if matches:
            regex_rm = r"tiktok"
            result = re.sub(regex_rm, "vxtiktok", url.split("?")[0], 1)
            menu = ButtonMenu(timeout=None, member=ctx.author)
            await ctx.send(result, view=menu)
        else:
            await ctx.send("This is not a valid tiktok", ephemeral=True)

    @commands.hybrid_command()
    async def instagram(self, ctx, url):
        """Returns ddInstagram Link."""
        regex = r"((https?):\/\/)?((www?).)?(instagram)\.com\/(p|reel)\/(.*)\/.*?"
        matches = re.search(regex, url)
        if matches:
            regex_rm = r"instagram"
            result = re.sub(regex_rm, "ddinstagram", url.split("?")[0], 1)
            menu = ButtonMenu(timeout=None, member=ctx.author)
            await ctx.send(result, view=menu)
        else:
            await ctx.send("This is not a valid instagram post", ephemeral=True)
