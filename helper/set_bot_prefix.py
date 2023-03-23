from ez_storage.ez_storage import Ez_Storage
from colorama import Fore
import sys


def print_clr(content: str, color):
    print(color + content + Fore.RESET)


def set_bot_prefix(prefix: str):
    Ez_Storage("../storage/data.ezs").add_storage(mode="o", obj="bot", data="bot_prefix",
                                                  value=prefix, override=True)


if __name__ == "__main__":
    # This Helper Script will set the bot_token for pycord-bb instance
    print_clr("pycord-bb helper: bot_prefix", Fore.BLUE)
    print_clr("enter bot_prefix:", Fore.YELLOW)
    set_bot_prefix(input())
    print_clr("bot_prefix has been set", Fore.GREEN)
    print_clr("Exiting now ...", Fore.RED)
    sys.exit()





