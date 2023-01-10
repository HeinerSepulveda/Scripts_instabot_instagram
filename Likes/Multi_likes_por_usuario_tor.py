import argparse
import os
import sys

BASE_DE_DATOS = "UsersPassDB.txt"

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('--likes', type=int, help="amount")
parser.add_argument('users', type=str, nargs='+', help='users')
args = parser.parse_args()


with open(BASE_DE_DATOS, "r") as f:
	lineas = [linea.strip().split(":", 2) for linea in f.readlines()]

acum=1
print "\033[0;32m"+"---------------------------------- Enviando likes con la cuenta  #",acum,"-----------------------------------------------"+"\033[0;37m"

"""for x in range(0,len(lineas)):"""
for login, passw in lineas:
  acum=acum+1
  bot = Bot()
  bot.login(username=login, password=passw)
  for username in args.users:
    bot.like_user(username, amount=args.likes, filtration=False)
    msg = ("---------------------------------- Enviando likes con la cuenta # {} -----------------------------------------------")
    msg = msg.format(acum)
    color = bot.console_print(msg, 'green')



