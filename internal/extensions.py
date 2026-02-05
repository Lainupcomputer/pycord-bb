"""
extension_loader.py
-------------------

Author: Lainup
Date: 2026-01-12
Version: 1.0.0.0

Description:
    This module provides utility functions to load Discord bot extensions and modules.
    - `file_loader` loads all Python files in the `cogs` directory as extensions.
    - `module_loader` loads all modules from the `extensions` package.

Dependencies:
    - logging
    - os
    - pkgutil
    - Local package: extensions

Example:
    >>> file_loader(bot)
    >>> module_loader(bot)
"""

__author__ = "Lainup"
__date__ = "2026-01-12"
__version__ = "1.0.0.0"

import logging
import os
import pkgutil
import extensions

logger = logging.getLogger("Extension-Loader")


def file_loader(bot) -> None:
    """
    Loads all Python files in the `cogs` directory as bot extensions.

    Iterates through the 'cogs' folder, checks for files ending with '.py', 
    and loads each as a Discord extension using `bot.load_extension`.

    Args:
        bot (commands.Bot): The Discord bot instance.

    Returns:
        None

    Example:
        >>> file_loader(bot)
    """
    cogs: int = 0
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            bot.load_extension(f"cogs.{file[:-3]}")
            cogs += 1
    logger.info(f"Loaded {cogs} Extensions.")


def module_loader(bot) -> None:
    """
    Loads all modules in the `extensions` package as bot extensions.

    Iterates through all modules in the `extensions` package and loads 
    each module's `extension` submodule using `bot.load_extension`.

    Args:
        bot (commands.Bot): The Discord bot instance.

    Returns:
        None

    Example:
        >>> module_loader(bot)
    """
    loaded: int = 0
    for module in pkgutil.iter_modules(extensions.__path__):
        bot.load_extension(f"extensions.{module.name}.extension")
        loaded += 1
    logger.info(f"Loaded {loaded} Modules.")
