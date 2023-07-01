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
        url_extract_pattern = "((https?):\/\/)?(www.)?twitter\.com(\/@?(\w){1,15})\/status\/[0-9]{19}"
        tweet = re.findall(url_extract_pattern, url)
        print(tweet)
        # if not tweet:
        #     await ctx.send("Tweet not found.")
        # else:
        #     print(tweet[0])
        #     vx = tweet[0].split("https://")
        #     await ctx.send(f"{vx[0]}vx{vx[1]}")
