import disnake
from disnake.ext import commands
import random
import re

class RollCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(
    name="roll",
    description="Roll the Dice!",
)
    async def roll_dice(self,
                        inter: disnake.ApplicationCommandInteraction,
                        roll: str = commands.Param(description="The dice you want to roll! See /help for more info.")):
        roll_input = roll # For code Readability, we'll be using the roll_input variable instead of the roll variable
        dice_pattern = re.compile(r"^(?P<count>\d*)d(?P<type>\d+)(?P<bonus>[+-]?\d+)?$")
        match = dice_pattern.match(roll_input.lower())
    
        if not match:
            # If the pattern does not match, send an error message
            await inter.response.send_message("Please enter a valid dice format, e.g., '5d20', 'd6', or '2d10+3'.")
            return
        # Split the input on 'd' to separate the number of dice and dice type
        parts = roll_input.lower().split('d')
        num_dice = int(parts[0]) if parts[0] else 1  # Default to 1 dice if not specified

        # Handle additional modifiers (e.g., "+2" in "1d6+2")
        bonus = 0
        if '+' in parts[1]:
            dice_type_str, bonus_str = parts[1].split('+')
            bonus = int(bonus_str)  # Convert bonus to int
        elif '-' in parts[1]:
            dice_type_str, bonus_str = parts[1].split('-')
            bonus = int(bonus_str)*-1
        else:
            dice_type_str = parts[1]

        dice_type = int(dice_type_str)

        # Debug output to verify input processing
        debug_roll_input = f'{num_dice}d{dice_type}' + (f'+{bonus}' if bonus else '')
        print(f"DEBUG: Roll Input is {debug_roll_input}")

        total_roll = 0
        individual_rolls = []
        for _ in range(num_dice):
            roll_result = random.randint(1, dice_type)
            print(f"DEBUG: Roll is {roll_result}")
            total_roll += roll_result
            individual_rolls.append(roll_result)
        
        total_roll += bonus

        print(f"DEBUG: Total roll is {total_roll}")
        result_string = ""
        for index, roll in enumerate(individual_rolls, start=1):
            result_string += f"**Roll {index}:** {roll} *(d{dice_type})*\n"
        result_string += f"**Total:** {total_roll}"
        await inter.response.send_message(result_string)



def setup(bot: commands.Bot):
    bot.add_cog(RollCommand(bot))