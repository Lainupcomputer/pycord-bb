"""
helpüer.py
-----------------

Author: Lainup
Date: 2026-01-12
Version: 1.0.0.1

Description:
    This module provides a utility function to send a direct message to a Discord user.
    The function handles permission errors gracefully and returns a boolean status.

Dependencies:
    - discord.py (discord)

Example:
    >>> success = await send_user_message(user, "Hello!")
    >>> if success:
    >>>     print("Message sent successfully")
    >>> else:
    >>>     print("Failed to send message")
"""

__author__ = "Lainup"
__date__ = "2026-01-12"
__version__ = "1.0.0.1"
__all__ = ["send_user_message"]

import discord


async def send_user_message(send_user: discord.User, message: str) -> bool:
    """
    Sends a direct message to a specified Discord user.

    Attempts to send a message to the given user. If the bot lacks permission
    to send DMs (discord.Forbidden), the function returns False.

    Args:
        send_user (discord.User): The Discord user to send the message to.
        message (str): The message content to send.

    Returns:
        bool: True if the message was sent successfully, False otherwise.

    Example:
        >>> success = await send_user_message(user, "Hello!")
        >>> if success:
        >>>     print("Message sent successfully")
        >>> else:
        >>>     print("Failed to send message")
    """
    try:
        await send_user.send(message)
        return True
    except discord.Forbidden:
        return False
