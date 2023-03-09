import discord
from discord.ext import commands
import os
import sys
from ez_storage.ez_storage import Ez_Storage
from colorama import Fore


intents = discord.Intents.all()

bot = commands.Bot(intents=intents, command_prefix=".")
storage = Ez_Storage("./storage/data.ezs")


@bot.event
async def on_ready():
    if bot.auto_sync_commands:
        await bot.sync_commands()
    print(Fore.GREEN + "Bot Online!" + Fore.RESET)


@bot.event
async def on_connect():
    print(Fore.YELLOW + "Bot connected" + Fore.RESET)


if __name__ == "__main__":
    if "-token" in sys.argv:
        storage.add_storage(mode="o", obj="bot", data="token",
                            value=sys.argv[2], override=True)
    # additional commands Start:
    # Place additional commands between start - end
    # additional commands END
    print(Fore.YELLOW + "Starting Discord Bot ...\nLoading Cogs ..." + Fore.RESET)
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            bot.load_extension(f"cogs.{file[:-3]}")
    bot.run(storage.get_storage(mode="o", obj="bot", data="token"))