# Simple avatar URL fetch

# Discord
import discord

# Red
from redbot.core import commands


class Avatar(commands.Cog):
    """Get user's avatar URL."""

    @commands.command()
    async def avatar(self, ctx, server=None, user: discord.Member=None):
        """Returns user avatar URL.

        User argument can be user mention, nickname, username, user ID.
        Default to yourself when no argument is supplied.
        """
        author = ctx.author

        if not user:
            user = author

        if not server or server == "global":
            avatar = user.avatar
        elif server == "server":
            avatar = user.display_avatar
            
        if (avatar.is_animated()):
            url = avatar.with_static_format("gif")
        else:
            url = avatar.with_static_format("png")

        await ctx.send(f"{user}'s Avatar URL : {url}")