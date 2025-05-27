from keep_alive import keep_alive
keep_alive()
import discord
import os
import sys
from dotenv import load_dotenv
intents = discord.Intents.default()
intents.message_content = True  # Needed to read message content
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print("PocketDiary is ready to be used")

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("-open"):
    await message.channel.send("PocketDiary is open!")
    

# =================================================DO_NOT_MESS=================================================    
if len(sys.argv) > 1 and sys.argv[1] == "test":
    load_dotenv(".gitignore\.env.test")
else:
    load_dotenv()

DISCORD_TOKEN = os.getenv("TOKEN")
client.run(DISCORD_TOKEN)
