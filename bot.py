import discord
from discord.ext import commands
import os
from ez_storage.ez_storage import Ez_Storage
from colorama import Fore
from internal.cmd_tools import print_clr


intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix=".")


@bot.event
async def on_ready():
    if bot.auto_sync_commands:
        await bot.sync_commands()
    print_clr("Bot Online!", Fore.GREEN)


@bot.event
async def on_connect():
    print_clr("Bot connected", Fore.YELLOW)


if __name__ == "__main__":
    print_clr("Starting Discord Bot ...\nLoading Cogs ...", Fore.YELLOW)
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            bot.load_extension(f"cogs.{file[:-3]}")
    bot.run(Ez_Storage("./storage/data.ezs").get_storage(mode="o", obj="bot", data="token"))
