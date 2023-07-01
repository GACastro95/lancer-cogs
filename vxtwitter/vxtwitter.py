import discord
import re
from redbot.core import commands

class VxTwitter(commands.Cog):
    """Converts twitter links to Vxtwitter links"""

    @commands.hybrid_command()
    async def twitter(self, ctx, url):
        """Returns Vxtwitter Link."""
        subst = "https://vxtwitter.com"
        regex = r"((https?):\/\/)?(www.)?twitter\.com(\/@?(\w){1,15})\/status\/[0-9]{19}"
        matches = re.search(regex, url)
        if matches:
            regex_rm = r"((https?):\/\/)?(www.)?twitter\.com"
            result = re.sub(regex_rm, subst, url.split("?")[0], 1)
            await ctx.send(result)
        else:
            await ctx.send("This is not a tweet", ephemeral=True)