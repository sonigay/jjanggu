import discord
import asyncio
import random
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]
json_file_name = 'vast-ethos-251302-b8a92651b359.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1j83Zex9AdiHad-LkmnndHdvZdu25KupZCmMdtqwCjCY/edit#gid=0'
# 스프레스시트 문서 가져오기 
doc = gc.open_by_url(spreadsheet_url)
# 시트 선택하기
worksheet = doc.worksheet('시트1')


cell_data = worksheet.acell('B1').value
print(cell_data)
 
row_data = worksheet.row_values(1)
print(row_data)

column_data = worksheet.col_values(1)
print(column_data)


# 범위(셀 위치 리스트) 가져오기
range_list = worksheet.range('A1:D2')
print(range_list)
# 범위에서 각 셀 값 가져오기
for cell in range_list:
    print(cell.value)


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
