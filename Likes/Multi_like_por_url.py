import argparse
import os
import sys
import requests

BASE_DE_DATOS = "UsersPassDB.txt"

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot


parser = argparse.ArgumentParser(description='Likes por url Instagram', add_help=True)
parser.add_argument('link', type=str, help='Url de foto Instagram')
args = parser.parse_args()

with open(BASE_DE_DATOS, "r") as f:
	lineas = [linea.strip().split(":", 2) for linea in f.readlines()]

solicitud = requests.get(args.link)

if 'https://www.instagram.com/p/'  not in args.link:
	print "[!] Verifique la URL \n[!] Ejemplo: https://www.instagram.com/p/BjBQQiXAA45"
	sys.exit(0)

if solicitud.status_code == 200:
 for login, passw in lineas:
  bot = Bot()
  bot.login(username=login, password=passw)
  foto=bot.get_media_id_from_link(args.link)
  bot.like(foto)
  msg = ("---------------------------------- Se dio 1 like al link {} con id # {} -----------------------------------------------")
  msg = msg.format(args.link,foto)
  color = bot.console_print(msg, 'green')
elif solicitud.status_code == 404:
 print "Error",solicitud.status_code,"Foto no encontrada, revisa la Url"
