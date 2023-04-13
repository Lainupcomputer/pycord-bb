import os
import sys
import logging
import discord
from discord import default_permissions
from discord.ext import commands
from colorama import Fore
from internal import get_time_sys, check_create_dir, console_log, check_version


VERSION = "1.1.0.1"
# ez storage development
# this will change in future
#from ez_storage.ez_storage import Ez_Storage
from development import Storage


def build_bot(s) -> discord.Bot:
    """
    Builds a basic pycord-bb bot
    :param s: storage file: EzStorage
    :return: discord.Bot
    """
    intents = discord.Intents.all()
    bbot = commands.Bot(intents=intents, command_prefix=s.get("bot_prefix", within="bot"))

    @bbot.event
    async def on_ready():
        console_log("Bot Online!", Fore.GREEN, logging.INFO)
        if bot.auto_sync_commands:
            await bot.sync_commands()
            console_log("Commands synced!", Fore.GREEN, logging.INFO)

    @bbot.event
    async def on_connect():
        console_log("Bot connected", Fore.YELLOW, logging.INFO)

    @bbot.slash_command(description="Check if Bot is alive")
    @default_permissions(administrator=True)
    async def alive_check(ctx: discord.commands.context.ApplicationContext):
        await ctx.send_response("Alive!", ephemeral=True)
        console_log(f"{ctx.user.mention} performed 'alive_check'", Fore.YELLOW, logging.INFO)

    return bbot


if __name__ == "__main__":
    """
    Create needed directory's, skip if found 
    /logs
    /storage
    -
    Setup logger configuration
    -
    Check for Updates
    -
    Load Extensions 
    -
    Try to start the bot
    """
    check_create_dir("./logs")
    logging.basicConfig(filename=f"logs/{get_time_sys()}.log", level=logging.INFO,
                        format="%(asctime)s %(message)s")
    #_s = Ez_Storage("./storage/data.ezs")
    #_s.enable_debug = True
    #_s.storage_prefix = "bot"
    _s = Storage(dir="./storage/", path="data.ezs")
    bot = build_bot(_s)
    console_log(check_version("cot", VERSION), Fore.YELLOW, logging.INFO)
    for file in os.listdir("extensions"):
        if file.endswith(".py"):
            bot.load_extension(f"extensions.{file[:-3]}")
    try:

        bot.run(_s.get("bot_token", within="bot"))
    except discord.errors.LoginFailure:
        console_log("Improper token has been passed. (Login Failure)", Fore.RED, logging.ERROR)
        sys.exit()
    except TypeError:
        console_log("Improper token has been passed. (check if token is set)", Fore.RED, logging.ERROR)
        sys.exit()
