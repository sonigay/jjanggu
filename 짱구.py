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
            
            ################ 복권 ################ 
            
@client.event
async def on_message(message):

     if message.content.startswith('!정보'):
         date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
         embed = discord.Embed(color=0x00ff00)
         embed.add_field(name="이름", value=message.author.name, inline=True)
         embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
         embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
         embed.add_field(name="아이디", value=message.author.id, inline=True)
         embed.set_thumbnail(url=message.author.avatar_url)
         await client.send_message(message.channel, embed=embed)
            
     ################ embed ################        
            
     if message.content.startswith('!박스'):
        embed = discord.Embed(title="박스타이틀!", color=0x00ff00)
        embed.add_field(name="박스1", value= '```내용1```')
        embed.add_field(name="박스2", value= '```내용2```')
        embed.add_field(name="박스3", value= '```내용3```')
        embed.add_field(name="박스4", value= '```내용4```')
        embed.add_field(name="박스5", value= '```내용5```')
        embed.add_field(name="박스5", value= '```내용5```')
        embed.add_field(name="박스5", value= '```내용5```')
        await client.send_message(message.channel, embed=embed, tts=False) 
        
        
        
     if message.content.startswith('!명령'):
        embed = discord.Embed(title="명령어!", color=0x00ff00)
        embed.add_field(name="1", value= '```!박스```')
        embed.add_field(name="2", value= '```!박스2```')
        
        await client.send_message(message.channel, embed=embed, tts=False)  
        
        
     if message.content.startswith('!안녕하세요'):
        embed = discord.Embed(title="명령어!", description= '```안녕하세```', color=0x00ff00)
        embed.add_field(name="1", value= '```!박스```')
               
        await client.send_message(message.channel, embed=embed, tts=False)   

                                  
@client.event
async def on_message(message):
    if message.channel.is_private and message.author != "538289410018639893":
        await client.send_message(discord.utils.get(client.get_all_memvers(), id="315237238940106754", message.author.name + "(" +message.author.id + ") : " + message.content)
            


                                  
                                  
                                  
                                  
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
