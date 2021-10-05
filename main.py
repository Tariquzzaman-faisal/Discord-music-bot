import discord
from discord.ext import commands
import music

cogs = [music]

Client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(Client)


Client.run("ODk0ODI4MDIxNTI0MTAzMTY4.YVvriQ.Rae6M5wEwP6-mLn3193T6YEnEpY")

