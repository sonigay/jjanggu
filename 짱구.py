import discord
import asyncio
import random
import os


client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("----------------")
    await client.change_presence(game=discord.Game(name='당첨자뽑기', type=1))



@client.event
async def on_message(message):
    if message.content.startswith('!안녕'):
        await client.send_message(message.channel, "안녕하세요")

    if message.content.startswith('!주사위'):
        roll = message.content.split(" ")
        rolld = roll[1].split("d")
        dice = 0
        for i in range(1, int(rolld[0])+1):
            dice = dice + random.randint(1, int(rolld[1]))
        await client.send_message(message.channel, str(dice))

    if message.content.startswith('!뽑기'):
        choice = message.content.split(" ")
        choicenumber = random.randint(1, len(choice)-1)
        choiceresult = choice[choicenumber]
        await client.send_message(message.channel, choiceresult)

    if message.content.startswith('!뭐먹지'):
        food = "짜장면 짬뽕 라면 밥 굶기"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber-1]
        await client.send_message(message.channel, foodresult)
        
    if message.content.startswith("!사다리"):
        team = message.content[6:]
        peopleteam = team.split("/")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        for i in range(0, len(person)):
            await client.send_message(message.channel, person[i] + "---->" + teamname[i])   




access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
