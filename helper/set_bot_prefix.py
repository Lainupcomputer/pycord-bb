from development import Storage
from colorama import Fore
import sys


def print_clr(content: str, color):
    print(color + content + Fore.RESET)


def set_bot_prefix(prefix: str):
    Storage(dir="../storage/", path="data.ezs").add("bot_prefix", prefix, overwrite=True)


if __name__ == "__main__":
    # This Helper Script will set the bot_prefix for pycord-bb instance
    print_clr("pycord-bb helper: bot_prefix", Fore.BLUE)
    if len(sys.argv) > 1:
        set_bot_prefix(sys.argv[1])
    else:
        print_clr("enter bot_prefix:", Fore.YELLOW)
        set_bot_prefix(input())
    print_clr(f"bot_prefix has been set", Fore.GREEN)
    print_clr("Exiting now ...", Fore.RED)
    sys.exit()
