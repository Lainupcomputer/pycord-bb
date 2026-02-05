from extensions import Extension
import discord
from discord.ext import commands
from discord import default_permissions
from discord.commands import slash_command


class System(Extension):
    __version__ = "1.0.1"
    __name__ = "System"

    def __init__(self, bot: commands.Bot) -> None:
        super().__init__(bot)

    def cog_unload(self):
        self.logger.info(f"{self.__name__} unloaded.")

    @slash_command(description="Check if Bot is alive",
                   default_member_permissions=discord.Permissions(manage_guild=True))
    @default_permissions(administrator=True)
    async def alive_check(self, ctx: discord.commands.context.ApplicationContext) -> None:
        await ctx.send_response("Alive!", ephemeral=True)

    @commands.command(description="delete amount of messages.")
    @commands.has_permissions(manage_messages=True)
    async def del_msg(self, ctx: discord.ApplicationContext, amount: int = 5) -> None:
        if amount < 1:
            await ctx.send_response("Bitte gib eine gültige Anzahl an Nachrichten an (mindestens 1).", ephemeral=True)
            return
        deleted = await ctx.channel.purge(limit=amount + 1)
        await ctx.send_response(f"🧹 {len(deleted) - 1} Nachrichten gelöscht!", ephemeral=True)

    @del_msg.error
    async def clear_error(self, ctx: discord.ApplicationContext, error) -> None:
        if isinstance(error, commands.MissingPermissions):
            await ctx.send_response("❌ Du hast keine Berechtigung, Nachrichten zu löschen.", ephemeral=True)
        elif isinstance(error, commands.BadArgument):
            await ctx.send_response("❌ Bitte gib eine gültige Zahl an.", ephemeral=True)
        else:
            await ctx.send_response("❌ Ein Fehler ist aufgetreten.", ephemeral=True)


def setup(bot):
    bot.add_cog(System(bot))
