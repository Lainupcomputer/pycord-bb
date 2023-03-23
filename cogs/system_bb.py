import logging
import discord
from colorama import Fore
from discord.ext import commands
from discord import default_permissions
from discord.commands import slash_command
from ez_storage.ez_storage import Ez_Storage
from internal.cmd_tools import print_log

VERSION = "1.0.0.1"


class system_bb(commands.Cog):
    def __init__(self, bot):
        print_log(f"Loading system_bb (COG:{VERSION})", Fore.BLUE, logging.INFO)
        self.bot = bot

    @slash_command(description="Check if Bot is alive")
    @default_permissions(administrator=True)
    async def alive_check(self, ctx: discord.commands.context.ApplicationContext):
        await ctx.send_response("Alive!", ephemeral=True)


def setup(bot):
    bot.add_cog(system_bb(bot))
