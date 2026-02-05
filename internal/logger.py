"""
logging.py
----------------

Author: Lainup
Date: 2026-01-12
Version: 1.0.0.0

Description:
    This module provides a utility function to set up logging for a project.
    It creates a 'logs' directory if it does not exist, and configures both
    console and file handlers with a standardized logging format.

Dependencies:
    - logging
    - os

Example:
    >>> logger = setup_logging("bot.log")
    >>> logger.info("Logger is ready!")
"""

__author__ = "Your Name"
__date__ = "2026-01-12"
__version__ = "1.0.0.0"
__all__ = ["setup_logging"]

import os
import logging


def setup_logging(log_filename: str = "default.log") -> logging.Logger:
    """
    Sets up logging for the application with console and file handlers.

    Creates a 'logs' directory if it doesn't exist. Configures a console handler
    and a file handler that logs INFO level messages and higher. The log format
    includes timestamp, logger name, log level, and message.

    Args:
        log_filename (str): The name of the log file. Defaults to "default.log".

    Returns:
        logging.Logger: Configured logger instance.

    Example:
        >>> logger = setup_logging("bot.log")
        >>> logger.info("Logger is ready!")
    """
    logs_folder = "logs"
    if not os.path.exists(logs_folder):
        os.makedirs(logs_folder)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        file_handler = logging.FileHandler(
            os.path.join(logs_folder, log_filename), mode='a', encoding='utf-8'
        )
        file_handler.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
