import argparse
import os
import sys

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('users', type=str, nargs='+', help='users')
args = parser.parse_args()


bot = Bot()
bot.login(username="tejada.patri", password="JuanMono")
for username in args.users:
    bot.like_user(username, amount=20, filtration=False)

bot = Bot()
bot.login(username="fitnes9292", password="fitnes123456")
for username in args.users:
    bot.like_user(username, amount=20, filtration=False)

bot = Bot()
bot.login(username="calipotenciafitness", password="anto1824")
for username in args.users:
    bot.like_user(username, amount=20, filtration=False)

bot = Bot()
bot.login(username="3022240329", password="juanmanuel123456789")
for username in args.users:
    bot.like_user(username, amount=20, filtration=False)

bot = Bot()
bot.login(username="edwin.wine", password="JuanMono")
for username in args.users:
    bot.like_user(username, amount=20, filtration=False)



bot = Bot()
bot.login(username="camilomunoz32", password="camilo123456789")
for username in args.users:
    bot.like_user(username, amount=20, filtration=False)


bot = Bot()
bot.login(username="1011ca", password="5566re")
for username in args.users:
    bot.like_user(username, amount=20, filtration=False)


bot = Bot()
bot.login(username="luisperez757", password="hhhjj7")
for username in args.users:
    bot.like_user(username, amount=20, filtration=False)


bot = Bot()
bot.login(username="luisa7041", password="1234567luisa")
for username in args.users:
    bot.like_user(username, amount=20, filtration=False)


bot = Bot()
bot.login(username="77juan6", password="Dv123456")
for username in args.users:
    bot.like_user(username, amount=20, filtration=False)







