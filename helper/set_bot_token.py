from ez_storage.ez_storage import Ez_Storage
from colorama import Fore
import sys


def print_clr(content: str, color):
    print(color + content + Fore.RESET)


def set_bot_token(token: str):
    Ez_Storage("../storage/data.ezs").add_storage(mode="o", obj="bot", data="bot_token",
                                                  value=token, override=True)


if __name__ == "__main__":
    # This Helper Script will set the bot_token for pycord-bb instance
    print_clr("pycord-bb helper: bot_token", Fore.BLUE)
    print_clr("enter bot_token:", Fore.YELLOW)
    set_bot_token(input())
    print_clr("bot_token has been set", Fore.GREEN)
    print_clr("Exiting now ...", Fore.RED)
    sys.exit()
