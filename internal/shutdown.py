"""
shutdown.py
---------------

Author: Lainup
Date: 2026-01-12
Version: 1.0.0.0

Description:
    This module provides a utility function to gracefully shut down a Discord bot.
    The shutdown process includes unloading all cogs/extensions, closing the database 
    connection, and properly closing the bot client.

Dependencies:
    - logging
    - Local module: db.session (shutdown_db)
    - discord.py (for bot object)

Example:
    >>> await shutdown(bot)
"""

__author__ = "Lainup"
__date__ = "2026-01-12"
__version__ = "1.0.0.1"
__all__ = ["shutdown"]

import logging
from db.session import shutdown_db

logger = logging.getLogger("Bot-Shutdown")


async def shutdown(bot) -> None:
    """
    Gracefully shuts down a Discord bot instance.

    Steps performed:
        1. Logs shutdown initiation.
        2. Unloads all cogs/extensions by calling `cog_unload` if available.
        3. Closes the database engine if the bot has a `db` attribute.
        4. Closes the bot client.
        5. Logs completion of shutdown.

    Args:
        bot (discord.ext.commands.Bot): The bot instance to shut down.

    Returns:
        None

    Example:
        >>> await shutdown(bot)
    """
    logger.info("Shutdown initiated...")

    for cog in list(bot.cogs.values()):
        if hasattr(cog, "cog_unload"):
            cog.cog_unload()
    logger.info("Extensions Unloaded")

    # Close DB Engine
    if hasattr(bot, "db"):
        logger.info("Closing Database Engine...")
        await shutdown_db()

    # Close bot
    await bot.close()
    logger.info("Shutdown Completed!")
