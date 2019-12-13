import telebot
import random
import string


bot = telebot.TeleBot('750269199:AAEtjTL-mj6qQJhr9B8u_LOYT87qSH4_EqI')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Числа и буквы', 'Числа, буквы и спецсимволы')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Бот создаёт пароль от 9 до 44 символов. \\n Пароль может состоять из чисел и букв или из чисел, букв и спецсимволов',
    reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def passwordgeneration(message):
    if message.text.lower() == 'числа и буквы':
        symbols = string.ascii_letters + string.digits
    elif message.text.lower() == 'числа, буквы и спецсимволы':
        symbols = string.ascii_letters + string.digits + string.punctuation
    length = random.randint(9,44)
    password = ''.join(random.sample(symbols, length))
    bot.send_message(message.chat.id, password)

bot.polling()