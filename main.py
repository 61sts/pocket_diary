from keep_alive import keep_alive
keep_alive()
import discord
from discord.ext import bridge
from discord.ext import commands
import os
import sys
from dotenv import load_dotenv
#* ====================================================================================================================================

# Making bot object from Bridge class (Subclass of Client)
bot = bridge.Bot(intents=discord.Intents.all(), command_prefix="-", help_command=None)

# An event for when bot goes online
@bot.event
async def on_ready():
  print(f"{bot.user} is ready to be used")
  await bot.sync_commands()

#Loading Cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
        print(f"Loaded {filename} cog")


#*             =================================================DO_NOT_MESS=================================================    
if __name__ == "__main__":

    if len(sys.argv) > 1 and sys.argv[1] == "test":
        bot.run(os.getenv("TEST_TOKEN"))
    else:
        bot.run(os.getenv("TOKEN"))

# python main.py test
