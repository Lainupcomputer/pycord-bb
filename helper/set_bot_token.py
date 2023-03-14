from ez_storage.ez_storage import Ez_Storage
from colorama import Fore
import sys
from internal.cmd_tools import print_clr


# This Helper Script will set the bot_token for pycord-bb instance
print_clr("pycord-bb helper: bot_token", Fore.BLUE)
print_clr("enter bot_token:", Fore.YELLOW)
user_input = input()
Ez_Storage("../storage/data.ezs").add_storage(mode="o", obj="bot", data="bot_token", value=user_input, override=True)
print_clr("bot_token has been set", Fore.GREEN)
print_clr("Exiting now ...", Fore.RED)
sys.exit()
