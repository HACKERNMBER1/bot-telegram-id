import telebot
import flask
from flask import FLASK
from telebot import types 

Z = '\033[1;31m' #احمر

X = '\033[1;33m' #اصفر

Z1 = '\033[2;31m' #احمر ثاني

F = '\033[2;32m' #اخضر

A = '\033[2;34m'#ازرق

C = '\033[2;35m' #وردي

B = '\033[2;36m'#سمائي

Y = '\033[1;34m' #ازرق فاتح

server = Flask(__name__)
token = "5134782801:AAFSEsM-00Ink4Jsz0Q2g4tOZ9cOZ8Ea3Hg"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])

def start(message):

  bot.send_message(message.chat.id,"*Welcome to the bot to know your account ID Telegram to know your account ID send* /id\n\n*BY :* @HarithTools",parse_mode='markdown')

@bot.message_handler(commands=['id'])

def id(message):

  bot.send_message(message.chat.id,f"*ID :* `{message.chat.id}`",parse_mode='markdown')

@bot.message_handler(commands=['info'])

def info(message):

  bot.send_message(message.chat.id,f"*With this bot, you can get the ID of your Telegram account By sending* /id\n\n*BY :* @HarithTools",parse_mode='markdown')

@bot.message_handler(content_types=['text'])

def start1(message):

  bot.send_message(message.chat.id,"*To Get id send* /id\n\n*BY : @HarithTools*",parse_mode='markdown')
@server.route(f"/{token}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200
if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://telebot-id.herokuapp.com/"+str(token))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
bot.infinity_polling()
