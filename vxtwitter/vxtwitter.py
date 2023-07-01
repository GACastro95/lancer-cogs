import discord
import re
from redbot.core import commands

class VxTwitter(commands.Cog):
    """Get user's avatar URL."""

    @commands.hybrid_command()
    async def twitter(self, ctx, url):
        """Returns user avatar URL."""
        await self.validate_url(ctx, url)



    async def validate_url(self, ctx, url):
        subst = "https://vxtwitter.com"
        regex = r"((https?):\/\/)?(www.)?twitter\.com(\/@?(\w){1,15})\/status\/[0-9]{19}\?"
        matches = re.search(regex, url)
        if matches:
            result = re.sub(regex, subst, url, 1)
            await ctx.send(result)
        else:
            await ctx.send("This is not a tweet")
        
        # if not tweet:
        #     await ctx.send("Tweet not found.")
        # else:
        #     print(tweet[0])
        #     vx = tweet[0].split("https://")
        #     await ctx.send(f"{vx[0]}vx{vx[1]}")
