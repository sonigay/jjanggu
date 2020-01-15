import discord
import asyncio
import random
import os
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('jungsanfile-e5ae2dbc8879.json', scope)
client = gspread.authorize(creds)
doc = client.open_by_url('https://docs.google.com/spreadsheets/d/15p6G4jXmHw7Z_iRCYeFwRzkzLxqf-3Pj0c6FeVuFYBM/edit#gid=0')

sheet1 = doc.worksheet('재고주문')

client = discord.Client()

@client.event
async def on_message(message):
    if messsage.content.startswith('!주문'):
        client.sheet1.insert_row(['내용2', '내용5'])

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
        
    if message.content.startswith("!DM"):
            member = discord.utils.get(client.get_all_members(), id=message.content[4:22])
            await client.send_message(member, "봇 홍팀장답변 : " + message.content[23:])

                        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
