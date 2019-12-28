import discord
import asyncio
from discord.ext import commands
from itertools import cycle
import random
import os


import gspread

from oauth2client.service_account import ServiceAccountCredentials


scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
]
json_file_name = 'jungsanfile-e5ae2dbc8879.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1WzFr_aNi6T_ievrOaVJK3hT2tRQsjltfACC6WL2qXNI/edit#gid=716684045'
# 스프레스시트 문서 가져오기
doc = gc.open_by_url(spreadsheet_url)
# 시트 선택하기
worksheet = doc.worksheet('시트1')

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
        
        
        
         if message.content.startswith("!명령어"):
        channel = message.channel
        embed = discord.Embed(
            title = '명령어들이다 크크크큭',
            description = '각각의 명령어들 이다 잘 봐둬라 큭...',
            colour = discord.Colour.blue()
        )

        #embed.set_footer(text = '끗')
        dtime = datetime.datetime.now()
        #print(dtime[0:4]) # 년도
        #print(dtime[5:7]) #월
        #print(dtime[8:11])#일
        #print(dtime[11:13])#시
        #print(dtime[14:16])#분
        #print(dtime[17:19])#초
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.hour)+"시 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        #embed.set_footer(text=dtime[0:4]+"년 "+dtime[5:7]+"월 "+dtime[8:11]+"일 "+dtime[11:13]+"시 "+dtime[14:16]+"분 "+dtime[17:19]+"초")
        embed.add_field(name = '!안녕', value = '인사하고싶을때 ㄱㄱ',inline = False)
        embed.add_field(name='!오늘배그', value='오늘 배그각 알려줌', inline=False)
        embed.add_field(name='!홋치', value='!홋치 단어1 단어2 형식으로 적으면 학습함', inline=False)
        embed.add_field(name='!말해', value='!말해 단어1 형식으로 적으면 학습한내용 말함', inline=False)
        embed.add_field(name='!기억초기화', value='학습한 데이터 초기화함', inline=False)
        embed.add_field(name='!데이터목록', value='학습한 데이터목록 알려줌', inline=False)
        embed.add_field(name='!모두모여', value='모두를 언급함', inline=False)
        embed.add_field(name='!들어와', value='봇이 음성채널에 들어옴', inline=False)
        embed.add_field(name='!나가', value='봇이 음성채널에 나감', inline=False)
        embed.add_field(name='!재생', value='!재생 유튜브링크 형식으로 적으면 유튜브 틀어줌', inline=False)
        embed.add_field(name='!일시정지', value='재생중인 유튜브 일시정지함', inline=False)
        embed.add_field(name='!다시재생', value='정지중인 유튜브 다시 재생함', inline=False)
        embed.add_field(name='!멈춰', value='재생,정지중인 유튜브 없어짐(영상목록 초기화)', inline=False)
        embed.add_field(name='!날씨', value='!날씨 원하는지역 을 입력하면 그 지역의 날씨정보를 제공합니다.', inline=False)
        embed.add_field(name='!롤', value='!롤 닉네임 형식으로 적으면 그 닉네임에대한 정보를 알려줍니다..', inline=False)
        embed.add_field(name='!배그솔로', value='!배그솔로 닉네임 형식으로 적으면 그 닉네임에대한 정보를 알려줍니다..', inline=False)
        embed.add_field(name='!배그듀오', value='!배그듀오 닉네임 형식으로 적으면 그 닉네임에대한 정보를 알려줍니다..', inline=False)
        embed.add_field(name='!배그스쿼드', value='!배그스쿼드 닉네임 형식으로 적으면 그 닉네임에대한 정보를 알려줍니다..', inline=False)
        embed.add_field(name='!고양이', value='!고양이 라고 적으면 고양이 사진이 나옵니다..', inline=False)
        embed.add_field(name='!강아지', value='!강아지 라고 적으면 강아지 사진이 나옵니다.', inline=False)
        embed.add_field(name='!네코', value='!네코 라고 적으면 2D 고양이 이미지가 나옵니다', inline=False)
        embed.add_field(name='!실시간검색어, !실검', value='!실시간검색어, !실검 이라고 적으면 네이버의 실시간 검색어 순위가 나타납니다.', inline=False)
        embed.add_field(name='!번역 번역할문자', value='!번역 번역할문자 이라고 적으면 번역할 문자를 번역한 링크가 나타납니다. ("띄어쓰기를 하시면 안됩니다. _,-등으로 구분해주세요.")', inline=False)
        embed.add_field(name='!영화순위', value='영화를 1~20순위로 나눈 영화순위 정보를 제공합니다.', inline=False)
        embed.add_field(name='!급식', value='군포e비즈니스 고등학교의 급식정보를 제공합니다.', inline=False)
        embed.add_field(name='!복권', value='랜덤으로 선정한 복권번호를 메시지로 보내줍니다.', inline=False)
        embed.add_field(name='!검색', value='!검색 검색할키워드 형식으로 입력하시면 유튜브 검색결과를 메시지로 보내줍니다.', inline=False)

        await client.send_message(channel,embed=embed)

    if message.content.startswith("!모두모여"):
        await client.send_message(message.channel, "@everyone")
        
        
        
         if message.content.startswith("!들어와"):
        channel = message.author.voice.voice_channel
        server = message.server
        voice_client = client.voice_client_in(server)
        print("들어와")
        print(voice_client)
        print("들어와")
        if voice_client== None:
            await client.send_message(message.channel, '들어왔습니다') # 호오.... 나를 부르는건가? 네녀석.. 각오는 되있겠지?
            await client.join_voice_channel(channel)
        else:
            await client.send_message(message.channel, '봇이 이미 들어와있습니다.') # 응 이미 들어와있어 응쓰게싸




    if message.content.startswith("!나가"):
            server = message.server
            voice_client = client.voice_client_in(server)
            print("나가")
            print(voice_client)
            print("나가")
            if voice_client == None:
                await client.send_message(message.channel,'봇이 음성채널에 접속하지 않았습니다.') # 원래나가있었음 바보녀석 니녀석의 죄는 "어리석음" 이라는 .것.이.다.
                pass
            else:
                await client.send_message(message.channel, '나갑니다') # 나가드림
                await voice_client.disconnect()
            
            

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
