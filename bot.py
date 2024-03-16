import disnake
from disnake.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.InteractionBot()


@bot.event
async def on_ready():
    print("The bot is ready!")

bot.load_extensions('cogs')

bot.run(TOKEN)