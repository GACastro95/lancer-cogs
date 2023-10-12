from .fxtwitter import FxTwitter


async def setup(bot):
    await bot.add_cog(FxTwitter())