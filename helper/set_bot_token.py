from development import Storage
from colorama import Fore
import sys


def print_clr(content: str, color):
    print(color + content + Fore.RESET)


def set_bot_token(token: str):
    Storage(dir="../storage/", path="data.ezs").add("bot_token", token, overwrite=True)


if __name__ == "__main__":
    # This Helper Script will set the bot_token for pycord-bb instance
    print_clr("pycord-bb helper: bot_token", Fore.BLUE)
    print_clr("enter bot_token:", Fore.YELLOW)
    set_bot_token(input())
    print_clr("bot_token has been set", Fore.GREEN)
    print_clr("Exiting now ...", Fore.RED)
    sys.exit()
