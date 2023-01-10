import argparse
import os
import sys
import time

BASE_DE_DATOS = "UsersPassDB_Devices.txt"

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('users', type=str, nargs='+', help='users')
args = parser.parse_args()


with open(BASE_DE_DATOS, "r") as f:
	lineas = [linea.strip().split("||", 3) for linea in f.readlines()]

acum_followed=0
acum=1
print "\033[0;32m"+"---------------------------------- Se seguiran los seguidores de ",args.users,"con la cuenta  #",acum,"-----------------------------------------------"+"\033[0;37m"

"""for x in range(0,len(lineas)):"""
for login, passw, dispositivo in lineas:
  acum=acum+1
  bot = Bot(filter_business_accounts=False, filter_previously_followed=True, device=dispositivo)
  print "\033[0;32m"+"Usando el dispositivo:", dispositivo +"\033[0;37m"
  bot.login(username=login, password=passw)
  for username in args.users:
    acum_followed=acum_followed+20
    follows = bot.get_user_followers(user_id=username, nfollows=acum_followed)
    bot.follow_users(user_ids=follows)
    msg = ("---------------------------------- Se seguiran los seguidores de {} con la cuenta # {} -----------------------------------------------")
    msg = msg.format(args.users,acum)
    color = bot.console_print(msg, 'green')
    time.sleep(5)



