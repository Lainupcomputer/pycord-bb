import logging
from discord.ext import commands


def check_compatibility(versions):
    root = versions[0]
    for v in versions:
        if not  v == root:
            return False

    return True


class Extension(commands.Cog):
    __version__ = "1.0.0"
    __name__ = "Base-Extension"

    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot: commands.Bot = bot
        self.database = bot.db

        self.logger: logging.Logger = logging.getLogger(self.__name__)
        self.logger.info(
            f"Loading {self.__name__} (Version: {self.__version__})"
        )

    def cog_unload(self):
        self.logger.warning("EXTENSION UNLOAD UNDEFINED")