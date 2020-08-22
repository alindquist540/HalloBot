import discord
from discord.ext import commands

client = commands.Bot(command_prefix='h!')


@client.event
async def on_ready():
    print('Bot is ready.')

client.run('NzQ2NDU0NzE1MTg4OTAzOTY2.X0AkIA.NEehz3sMWfwYwgXfHE_id4oOIRM')
