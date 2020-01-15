import discord
import asyncio
import random
import os
import datetime



client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("----------------")
    await client.change_presence(game=discord.Game(name='업무지식 안내', type=1))




@client.event
async def on_message(message):

    if message.channel.is_private and message.author.id != "538289410018639893":
        await client.send_message(discord.utils.get(client.get_all_members(), id="315237238940106754"), message.author.name + "(" + message.author.id + ") : " + message.content)
            
    if message.channel.is_private and message.author.id != "538289410018639893":
        await client.send_message(client.get_channel("661768769131249667"), message.author.name + "(" + message.author.id + ") : " + message.content)
        
    if message.content.startswith("DM"):
        member = discord.utils.get(client.get_all_mambers(), id=message.content[4:22])
        await client.send_message(member,"봇 홍팀장답변 : " + message.content[23:])

                        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
