import telebot

#token
bot = telebot.TeleBot('1436078395:AAEVeirrnvP32O25LhIamnC9wLVvRFpfGHY')
f = open('/home/aidar/PycharmProjects/pythonProject1/workbot/cities.txt', 'r')

#может быть несколько типов данных приема:
#@bot.message_handler(content_types=['text', 'document', 'audio']
name = ''
surname = ''
age = 0
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/city':
        bot.send_message(message.from_user.id, "Какой у тебя город?")
        bot.register_next_step_handler(message, get_city) #следующий шаг – функция get_city
    else:
        bot.send_message(message.from_user.id, 'Напиши /city')

def get_city(message):
    k = 0
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
        city = ''
    else:
        bot.send_message(message.chat.id, 'Хорошо, теперь я знаю твой город!')
    print(city)

bot.polling(none_stop=True, interval=0)
f.close()