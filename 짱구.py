import discord
import asyncio
import random
from discord.ext import commands
import os
import datetime



client = discord.Client()

global command

command = []

command_inidata = repo.get_contents("command.ini")
	file_data4 = base64.b64decode(command_inidata.content)
	file_data4 = file_data4.decode('utf-8')
	command_inputData = file_data4.split('\n')

	
for i in range(command_inputData.count('\r')):
		command_inputData.remove('\r')
		
del(command_inputData[0])		
		
for i in range(len(command_inputData)):
		command.append(command_inputData[i][12:].rstrip('\r'))     #command[0] ~ [22] : 명령어	
	

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
        
        
        
     if message.content.startswith('!박스2'):
        embed = discord.Embed(title="명령어!", color=0x00ff00)
        embed.add_field(value= '```!박스```')
        embed.add_field(name="2", value= '```!박스2```')
        
        await client.send_message(message.channel, embed=embed, tts=False)  
        
        
        
    if message.content == command[0]:
				command_list = ''
				command_list += command[1] + '\n'     #!설정확인
				command_list += command[2] + '\n'     #!채널확인
				command_list += command[3] + ' [채널명]\n'     #!채널이동
				command_list += command[4] + '\n'     #!소환
				command_list += command[5] + '\n'     #!불러오기
				command_list += command[6] + '\n'     #!초기화
				command_list += command[7] + '\n'     #!명치
				command_list += command[8] + '\n'     #!재시작
				command_list += command[9] + '\n'     #!미예약
				command_list += command[10] + ' [인원] [금액]\n'     #!분배
				command_list += command[11] + ' [뽑을인원수] [아이디1] [아이디2]...\n'     #!사다리
				command_list += command[12] + ' [아이디]\n'     #!정산
				command_list += command[13] + ' 또는 ' + command[14] + ' 0000, 00:00\n'     #!보스일괄
				command_list += command[14] + '\n'     #!q
				command_list += command[15] + ' [할말]\n'     #!v
				command_list += command[16] + '\n'     #!리젠
				command_list += command[17] + '\n'     #!현재시간
				command_list += command[18] + '\n'     #!공지
				command_list += command[18] + ' [공지내용]\n'     #!공지
				command_list += command[18] + '삭제\n'     #!공지
				command_list += command[19] + ' [할말]\n\n'     #!상태
				command_list += command[20] + '\n'     #보스탐
				command_list += command[21] + '\n'     #!보스탐
				command_list += '[보스명]컷 또는 [보스명]컷 0000, 00:00\n'     
				command_list += '[보스명]멍 또는 [보스명]멍 0000, 00:00\n'     
				command_list += '[보스명]예상 또는 [보스명]예상 0000, 00:00\n' 
				command_list += '[보스명]삭제\n'     
				command_list += '[보스명]메모 [할말]\n'
				embed = discord.Embed(
						title = "----- 명령어 -----",
						description= '```' + command_list + '```',
						color=0xff00ff
						)
				embed.add_field(
						name="----- 추가기능 -----",
						value= '```[보스명]컷/멍/예상  [할말] : 보스시간 입력 후 빈칸 두번!! 메모 가능```'
						)
				await client.send_message(message.channel, embed=embed, tts=False)  

            
            

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
