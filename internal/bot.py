"""
bot.py
------------

Author: Lainup
Date: 2026-01-12
Version: 1.0.0.0

This module provides functionality to create and configure a Discord bot using discord.py.
It sets up a database connection, registers core bot events, and optionally synchronizes
slash commands. Designed for bots that require full intents and database interaction.

Dependencies:
    - discord.py (discord, discord.ext.commands)
    - asyncio
    - logging
    - Local module: db.session (init_db, SessionLocal, shutdown_db)

Example:
    >>> bot = build_bot()
    >>> bot.run("YOUR_BOT_TOKEN")
"""

__author__ = "Lainup"
__date__ = "2026-01-12"
__version__ = "1.1.0.0"
__all__ = ["build_bot"]

import logging
import discord
from discord.ext import commands
from db.session import init_db, SessionLocal
logger = logging.getLogger("BOT")


def build_bot() -> discord.ext.commands.bot.Bot:
    """
    Creates and configures a Discord bot instance.

    This function initializes a `commands.Bot` with all intents enabled and the
    default command prefix "?". It also sets up a database session and registers
    core bot events including `on_ready` and `on_connect`.

    Returns:
        discord.ext.commands.bot.Bot: The configured bot instance.

    Example:
        >>> bot = build_bot()
        >>> bot.run("YOUR_BOT_TOKEN")
    """
    bot = commands.Bot(intents=discord.Intents.all(), command_prefix="?")
    logger.info(f"Setting up Bot Runtime (Version:{__version__})")
    bot.db = SessionLocal

    @bot.event
    async def on_ready() -> None:
        """
        Event handler triggered when the bot is ready.

        Performs setup tasks:
            - Initializes and synchronizes the database.
            - Synchronizes slash commands (if enabled).
            - Logs the bot's ready status.
        """
        logger.info("Setup tasks...")
        await init_db()
        logger.info("Database synced!")
        if bot.auto_sync_commands:
            await bot.sync_commands()
            logger.info("Commands synced!")
        logger.info("Bot is Ready!")

    @bot.event
    async def on_connect() -> None:
        """
        Event handler triggered when the bot connects to Discord.
        """
        logger.info("Bot connected!")

    return bot



