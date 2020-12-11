import telebot
import datetime
from pyowm import OWM
#from telebot import types
'''markup = types.ReplyKeyboardMarkup()
markup.row('a', 'v')
markup.row('c', 'd', 'e')
markup.row('s', 'q', 'i')'''
f = open('/home/aidar/PycharmProjects/pythonProject1/workbot/cities.txt', 'r')
bot = telebot.TeleBot('1436078395:AAEVeirrnvP32O25LhIamnC9wLVvRFpfGHY')
owm = OWM('e23d57aaefa08cc8b89abfbdb73d678e')

@bot.message_handler(commands=['start'])#бот будет реагировать на команду /start
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start, если хочешь узнать погоду в своём городе для начала пиши /city')

@bot.message_handler(commands=['city'])
def user_city(message: str):
    bot.send_message(message.from_user.id, 'Какой у тебя город?')
    bot.register_next_step_handler(message, get_city)
def get_city(message):
    city = message.text.lower()
    a = []
    for i in f:
        i = i.replace('\n', '')
        a.append(i)
    k = 0
    for i in a:
        if city == i.lower():
            k += 1
    if k != 1:
        bot.send_message(message.chat.id, 'Ты ошибся при написании города, пиши заново /city')
    else:
        bot.send_message(message.chat.id, 'Хорошо, теперь я знаю твой город!')
    print(city)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        t = str(datetime.datetime.now().time())
        t = t[0] + t[1]
        t = int(t)
        if t >= 0 and t <= 6:
            bot.send_message(message.chat.id, 'Вижу вам не спится, здравствуйте!')
        if t >= 6 and t <= 10:
            bot.send_message(message.chat.id, 'Доброе утро!')
        if t >= 10 and t <= 18:
            bot.send_message(message.chat.id, 'Добрый день!')
        if t >= 18 and t <= 23:
            bot.send_message(message.chat.id, 'Добрый вечер!')

    if message.text.lower() == 'пока':
        t = str(datetime.datetime.now().time())
        t = t[0] + t[1]
        t = int(t)
        if t > 0 and t < 6:
            bot.send_message(message.chat.id, 'Спокойной ночи!')
        if t > 6 and t < 10:
            bot.send_message(message.chat.id, 'Хорошего утра!')
        if t > 10 and t < 18:
            bot.send_message(message.chat.id, 'Доброго дня!')
        if t > 18 and t < 23:
            bot.send_message(message.chat.id, 'Хорошего вечера!')

    if message.text.lower() == 'йоу':
        bot.send_message(message.chat.id, 'Йоу, создатель')
    if message.text.lower() == 'салам':
        bot.send_message(message.chat.id, 'Салам алейкум, создатель')


bot.polling(none_stop=True, interval=0)
bot.polling()
f.close()
