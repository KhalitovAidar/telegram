import telebot
import datetime
from pyowm import OWM
from telebot import types

markup = types.ReplyKeyboardMarkup()
markup.row('a', 'v')
markup.row('c', 'd', 'e')
markup.row('s', 'q', 'i')

bot = telebot.TeleBot('1436078395:AAEVeirrnvP32O25LhIamnC9wLVvRFpfGHY')
owm = OWM('e23d57aaefa08cc8b89abfbdb73d678e')


@bot.message_handler(commands=['start'])  # Напишем декоратор#бот будет реагировать на команду /start
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start, если хочешь узнать погоду в своём городе для начала пиши /city')


@bot.message_handler(commands=['city'])
def nowcity(message):
    global city
    bot.send_message(message.chat.id,
                     'Теперь напиши свой город')
    last_call = message.text.lower()
    new_call = message.text.lower()


# ответ не только на команды, но и на сообщения
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        t = str(datetime.datetime.now().time())
        t = t[0] + t[1]
        t = int(t)
        if t > 0 and t < 6:
            bot.send_message(message.chat.id, 'Вижу вам не спится, здравствуйте!')
        if t > 6 and t < 10:
            bot.send_message(message.chat.id, 'Доброе утро!')
        if t > 10 and t < 18:
            bot.send_message(message.chat.id, 'Добрый день!')
        if t > 18 and t < 23:
            bot.send_message(message.chat.id, 'Добрый вечер!')

    if message.text.lower() == 'пока':
        if t > 0 and t < 6:
            bot.send_message(message.chat.id, 'Спокойной ночи!')
        if t > 6 and t < 10:
            bot.send_message(message.chat.id, 'Хорошего утра!')
        if t > 10 and t < 18:
            bot.send_message(message.chat.id, 'Доброго дня!')
        if t > 18 and t < 23:
            bot.send_message(message.chat.id, 'Хорошего вечера!')
    elif message.text.lower() == 'йоу':
        bot.send_message(message.chat.id, 'Йоу, создатель')
    elif message.text.lower() == 'салам':
        bot.send_message(message.chat.id, 'Салам алейкум, создатель')


# @bot.message_handler(content_types=['text'])
# def weather(message):

bot.polling()