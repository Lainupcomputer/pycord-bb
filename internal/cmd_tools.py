from colorama import Fore
import logging


def print_clr(content: str, color):
    print(color + content + Fore.RESET)


def print_log(content: str, color, log_level: int):
    if log_level == logging.CRITICAL or log_level == logging.FATAL or log_level == logging.ERROR:
        color = Fore.RED
        content = "CRASHED: " + content
    for c in content.split("\n"):
        logging.log(log_level, c)
        print(color + c + Fore.RESET)


