import disnake
from disnake.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(
        name="help",
        description="a small tutorial on how to roll the dice!",
    )

    async def help(self, inter: disnake.ApplicationCommandInteraction):
        file_path = './tutorial.png'
        tutorial_image = disnake.File(file_path)
        await inter.response.send_message("To use the Dice Roller, do /roll and input your dice identifier! You can see below what each part of the dice identifier means.", file=tutorial_image)

         

def setup(bot: commands.Bot):
    bot.add_cog(HelpCommand(bot))