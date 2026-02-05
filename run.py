"""
run.py
----------------

Author: Lainup
Date: 2026-01-12
Version: 1.0.0.0

Description:
    This is the main entry point for the Discord bot. It performs the following tasks:
        - Loads environment variables from a .env file.
        - Sets up logging with timestamped log files.
        - Builds the bot instance using `build_bot`.
        - Loads extensions and modules using either the new or old loader.
        - Starts the bot asynchronously and handles graceful shutdowns.

Dependencies:
    - discord.py
    - asyncio
    - logging
    - os, sys
    - dotenv
    - Local modules:
        - internal.bot (build_bot)
        - internal.logger (setup_logging)
        - internal.timing (get_time_sys)
        - internal.shutdown (shutdown)
        - internal.extensions (module_loader, file_loader)

Environment Variables:
    - BOT_TOKEN: Discord bot token required for authentication.

Example:
    >>> python bot_launcher.py
"""

import discord
from internal.bot import build_bot
from internal.logger import setup_logging
from internal.timing import get_time_sys
import os
import sys
import logging
from dotenv import load_dotenv
load_dotenv()
from internal.shutdown import shutdown


USE_NEW_LOADER = True
logger = logging.getLogger("BOT-LOADER")
import asyncio

from internal.extensions import module_loader, file_loader




async def main():
    """
    Main asynchronous entry point for running the bot.

    Starts the bot with the token from environment variables and ensures
    graceful shutdown in case of cancellation or interrupt.

    Returns:
        None
    """
    async with bot:
        try:
            await bot.start(os.getenv("BOT_TOKEN"))
        except asyncio.CancelledError:
            await shutdown(bot)


if __name__ == "__main__":
    setup_logging(f"{get_time_sys()}.log")
    # Pycord Logger
    logging.getLogger("discord").setLevel(logging.WARNING)

    bot = build_bot()
    logger.info("Loading Extensions...")
    if not USE_NEW_LOADER:
        file_loader(bot)
    else:
        module_loader(bot)
    try:
        asyncio.run(main())
    except discord.errors.LoginFailure:
        logger.error("Improper token has been passed. (token not valid), terminated")
        sys.exit()
    except TypeError:
        logger.error("Improper token has been passed. (check if token is set), terminated")
        sys.exit()
    except KeyboardInterrupt:
        logger.info("Shutdown requested by user")