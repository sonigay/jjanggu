import discord
import asyncio
import random
import os
import datetime



client = discord.Client()


@client.event
async def on_ready():
     if message.channel.is_private and message.author.id != "538289410018639893":
        await client.send_message(discord.utils.get(client.get_all_memvers(), id="315237238940106754", message.author.name + "(" +message.author.id + ") : " + message.content)
                                  
                                  
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
