import discord

from redbot.core import commands


# Classname should be CamelCase and the same spelling as the folder
class Avatar(commands.Cog):
    """Description of the cog visible with [p]help MyFirstCog"""

    @commands.command()
    async def avatar(self, ctx, *, user: discord.Member = None):
        """Returns user avatar URL.

        User argument can be user mention, nickname, username, user ID.
        Default to yourself when no argument is supplied.
        """
        author = ctx.author

        if not user:
            user = author

        url = user.avatar.with_static_format("png")

        await ctx.send(f"{user}'s Avatar URL : {url}")
