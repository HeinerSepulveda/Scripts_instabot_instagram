import argparse
import os
import sys

BASE_DE_DATOS = "UsersPassDB_Devices.txt"

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('users', type=str, nargs='+', help='users')
args = parser.parse_args()


with open(BASE_DE_DATOS, "r") as f:
	lineas = [linea.strip().split(":", 2) for linea in f.readlines()]

acum=1
print "\033[0;32m"+"---------------------------------- Se ha Seguido a",args.users,"con la cuenta  #",acum,"-----------------------------------------------"+"\033[0;37m"

"""for x in range(0,len(lineas)):"""
for login, passw in lineas:
  acum=acum+1
  bot = Bot(filter_users=False)
  bot.login(username=login, password=passw)
  for username in args.users:
    bot.follow(username)
    msg = ("---------------------------------- Se ha Seguido a {} con la cuenta # {} -----------------------------------------------")
    msg = msg.format(args.users,acum)
    color = bot.console_print(msg, 'green')



