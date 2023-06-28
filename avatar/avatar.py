# Simple avatar URL fetch

# Discord
import discord

# Red
from redbot.core import commands


class Avatar(commands.Cog):
    """Get user's avatar URL."""

    @commands.group()
    async def avatar(self, ctx: commands.Context) -> None:
        """Returns user avatar URL."""
        pass

    @avatar.command(name="server")
    async def _server_avatar(self, ctx, *, user: discord.Member=None):
        """Returns server user avatar.

        User argument can be user mention, nickname, username, user ID.
        Default to yourself when no argument is supplied.
        """
        await self.get_avatar(ctx, "server", user)

    @avatar.command(name="global")
    async def _global_avatar(self, ctx, *, user: discord.Member=None):
        """Returns the global user avatar.

        User argument can be user mention, nickname, username, user ID.
        Default to yourself when no argument is supplied.
        """
        await self.get_avatar(ctx, "global", user)

    async def get_avatar(self, ctx, type, user: discord.Member):
        """Gets the correct avatar type for the user
        """
        author = ctx.author

        if not user:
            user = author

        if (type == "global"):
            avatar = user.avatar
        elif (type == "server"):
            avatar = user.display_avatar

        if (avatar.is_animated()):
            url = avatar.with_static_format("gif")
        else:
            url = avatar.with_static_format("png")
        
        await ctx.send(f"{user}'s Avatar URL : {url}")