from colorama import Fore


def print_clr(content: str, color):
    print(color + content + Fore.RESET)
