import discord
import re
from redbot.core import commands


class FxTwitter(commands.Cog):
    """Converts twitter links to Fxtwitter links"""

    @commands.hybrid_command()
    async def twitter(self, ctx, url, download: bool = False):
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
            await ctx.send(result, ephemeral=True)
        else:
            await ctx.send("This is not a tweet", ephemeral=True)
