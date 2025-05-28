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
bot = bridge.Bot(intents=discord.Intents.all(), command_prefix="-")

# An event for when bot goes online
@bot.event
async def on_ready():
  print(f"{bot.user} is ready to be used")
  await bot.sync_commands()

# "help" command placeholder
@bot.bridge_command(description="List of commands that bot has")
async def list(ctx):
    embed = discord.Embed(title="Command List",
                          description="- `/info` : Provides information about the bot",
                          color=discord.Colour.blurple()
                          )
    await ctx.respond(embed=embed)   

# Info about the bot - "info" command - both / and -
@bot.bridge_command(description="Gives information about the bot")
async def info(ctx: discord.ApplicationContext):
    embed = discord.Embed(title=f"Hi! I am Pocket Diary",
                          description="A bot **currently in development** by <@1363200418552873024>.",
                          color=discord.Colour.blurple()
    )
    embed.add_field(name="Coded in", value="Python", inline=True)
    embed.add_field(name="Library", value="Pycord", inline=True)
    embed.add_field(name="Created on", value="<t:1748347560:D>", inline=True)
    embed.set_footer(text="Learning and Improving everyday")
    embed.set_author(name="61sts")
    embed.set_thumbnail(url="https://img.freepik.com/premium-vector/pixel-art-open-book-icon-game-asset-design_466450-2192.jpg")
    embed.set_image(url="https://i.pinimg.com/originals/4f/d3/0e/4fd30efd8301e3551a3a63da0d9c4d88.gif")
    await ctx.respond(embed=embed)
















#*             =================================================DO_NOT_MESS=================================================    
if len(sys.argv) > 1 and sys.argv[1] == "test":
    bot.run(os.getenv("TEST_TOKEN"))
else:
    bot.run(os.getenv("TOKEN"))

# python Pocket_diary_alpha.py test
