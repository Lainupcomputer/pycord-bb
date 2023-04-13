"""
Ez_Storage Utils

A collection of utility functions for working with Ez_Storage.

Functions:
    check_create_dir(path: str) -> None:
        Checks if a folder exists at the given path, and creates it if it does not.

    get_time_sys(raw=False) -> (str, int):
        Returns the current system time as a formatted string.

    console_log(content: str, color, log_level: int) -> None:
        Prints a message in a given color, logs the message, and resets the color.
"""
import os
import logging
from datetime import datetime
from colorama import Fore


def check_create_dir(path: str) -> None:
    """
    Checks if a folder exists at the given path. If it does not exist, creates the folder.

    Args:
        path (str): The path to the folder to check/create.

    Example:
        >>> check_create_dir('/path/to/folder')
    """
    try:
        os.mkdir(path)
    except FileExistsError:
        pass


def get_time_sys(raw=False) -> (str, int):
    """
    Returns the current system time as a formatted string.

    Args:
        raw (bool, optional): Whether to return the time as a raw integer value. Defaults to False.

    Returns:
        str: The formatted time string if raw=False.
        int: The raw integer time value if raw=True.

    Example:
        >>> get_time_sys()
        '08-04-2023_16-35-45'

        >>> get_time_sys(raw=True)
        20230408163545
    """
    now = datetime.now()  # get current date and time
    if raw:
        return now.strftime("%Y%m%d%H%M%S")
    else:
        return now.strftime("%d-%m-%Y_%H-%M-%S")


def console_log(content: str, color, log_level: int) -> None:
    """
    Prints a message in a given color and logs the message to a file.

    Args:
        content (str): The message content.
        color: The color to use for the message (e.g. Fore.RED).
        log_level (int): The logging level to use for the message (e.g. logging.INFO).

    Example:
        >>> console_log("Hello, world!", Fore.GREEN, logging.INFO)
        Hello, world!
    """
    if log_level == logging.CRITICAL or log_level == logging.FATAL or log_level == logging.ERROR:
        color = Fore.RED
        content = "CRASHED: " + content
    for c in content.split("\n"):
        logging.log(log_level, c)
    print(color + content + Fore.RESET)
