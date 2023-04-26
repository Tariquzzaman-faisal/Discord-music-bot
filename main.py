import discord
from discord.ext import commands
import music

cogs = [music]

Client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(Client)


Client.run("") # put bot token here

