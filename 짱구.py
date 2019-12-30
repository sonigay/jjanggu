import os
import sys
import asyncio
import discord
import datetime
import random
import math
import logging
from discord.ext import commands
from gtts import gTTS
from github import Github
import base64
import re #정산
import gspread #정산
from oauth2client.service_account import ServiceAccountCredentials #정산
from io import StringIO
import urllib.request




@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("----------------")
    await client.change_presence(game=discord.Game(name='당첨자뽑기', type=1))



@client.event
async def on_message(message):

     if message.content.startswith('!주사위'):
        roll = message.content.split(" ")
        rolld = roll[1].split("d")
        dice = 0
        for i in range(1, int(rolld[0])+1):
            dice = dice + random.randint(1, int(rolld[1]))
        await client.send_message(message.channel, str(dice))

     if message.content.startswith('!한명뽑기'):
        await client.send_message(message.channel, "이번 당첨자 분은")   
                      
     if message.content.startswith('!한명뽑기'):
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
        
     if message.content.startswith('!여러명뽑기'):
        await client.send_message(message.channel, "이번 당첨자 분들은")  

     if message.content.startswith("!여러명뽑기"):
        team = message.content[7:]
        peopleteam = team.split("/")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        for i in range(0, len(person)):
            await client.send_message(message.channel, person[i] + "---->" + teamname[i])   
            
            ################ 복권 ################ 
            
     if message.content.startswith("!복권"):
        Text = ""
        number = [1, 2, 3, 4, 5, 6, 7] # 배열크기 선언해줌
        count = 0
        for i in range(0, 7):
            num = random.randrange(1, 46)
            number[i] = num
            if count >= 1:
                for i2 in range(0, i):
                    if number[i] == number[i2]:  # 만약 현재랜덤값이 이전숫자들과 값이 같다면
                        numberText = number[i]
                        print("작동 이전값 : " + str(numberText))
                        number[i] = random.randrange(1, 46)
                        numberText = number[i]
                        print("작동 현재값 : " + str(numberText))
                        if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                            numberText = number[i]
                            print("작동 이전값 : " + str(numberText))
                            number[i] = random.randrange(1, 46)
                            numberText = number[i]
                            print("작동 현재값 : " + str(numberText))
                            if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                                numberText = number[i]
                                print("작동 이전값 : " + str(numberText))
                                number[i] = random.randrange(1, 46)
                                numberText = number[i]
                                print("작동 현재값 : " + str(numberText))

            count = count + 1
            Text = Text + "  " + str(number[i])

        print(Text.strip())
        embed = discord.Embed(
            title="복권 번호!",
            description=Text.strip(),
            colour=discord.Color.red()
        )
        await client.send_message(message.channel, embed=embed)       
        
        
        ################ 음성파일 생성 후 재생 ################ 			
				
			if message.content.startswith('!ㅍ') or message.content.startswith('!V'):
				tmp_sayMessage = message.content
				sayMessage = tmp_sayMessage[len('!ㅍ')+1:]
				await MakeSound(message.author.display_name +'님이.' + sayMessage, './sound/say')
				await client.get_channel(channel).send("```< " + msg.author.display_name + " >님이 \"" + sayMessage + "\"```", tts=False)
				await PlaySound(voice_client1, './sound/say.wav')
   
        

            
                   
            

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
