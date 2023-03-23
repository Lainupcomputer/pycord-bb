import discord
from discord.ext import commands
from discord.commands import slash_command
from discord import default_permissions
import os
import logging
from ez_storage.ez_storage import Ez_Storage
from colorama import Fore
from internal.cmd_tools import print_log
from internal.timing import get_time_sys
from internal.file_system import check_create_dir


BOT_STORAGE = "./storage/data.ezs"


intents = discord.Intents.all()
bot = commands.Bot(intents=intents,
                   command_prefix=Ez_Storage(BOT_STORAGE).get_storage(mode="o", obj="bot", data="bot_prefix"))


@bot.event
async def on_ready():
    print_log("Bot Online!", Fore.GREEN, logging.INFO)
    if bot.auto_sync_commands:
        await bot.sync_commands()
        print_log("Commands synced!", Fore.GREEN, logging.INFO)


@bot.event
async def on_connect():
    print_log("Bot connected", Fore.YELLOW, logging.INFO)


if __name__ == "__main__":
    check_create_dir("./Logs")
    logging.basicConfig(filename=f"Logs/{get_time_sys()}.log", level=logging.DEBUG,
                        format="%(asctime)s %(message)s")
    print_log("Starting Discord Bot ...\nLoading Cogs ...", Fore.YELLOW, logging.INFO)
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            bot.load_extension(f"cogs.{file[:-3]}")
    bot.run(Ez_Storage(BOT_STORAGE).get_storage(mode="o", obj="bot", data="bot_token"))
