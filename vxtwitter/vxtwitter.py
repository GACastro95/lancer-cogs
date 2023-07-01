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
        url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"     
        await ctx.send(re.match(url_pattern, url))

        url_extract_pattern = "https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)"
        await ctx.send(re.findall(url_extract_pattern, url))