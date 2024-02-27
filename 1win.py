import telebot 
from telebot import types


token = '6759716913:AAHBsNk5zPkW8PIlYmHuE2y7omeugzs_Sls'
bot = telebot.TeleBot(token)
admin_username='malsvx'
users=[]


@bot.message_handler(commands=['start'])
def countusers(message):
        if message.text=='/start':
                users.append(message.from_user.username)
                bot.register_next_step_handler(message,start)
def start(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Русский язык")
            btn2 = types.KeyboardButton("English Language")
            markup.add(btn1, btn2)
            bot.send_photo(message.from_user.id, open('1.png','rb'), caption='''🇷🇺Выберите ваш язык🇷🇺
                             
🇺🇸Select your language🇺🇸''',reply_markup=markup)
            if message.text=='Русский язык':
                    bot.register_next_step_handler(message, ru_language)
            else:
                    bot.register_next_step_handler(message, us_language)
def ru_language(message):
    if message.from_user.username==admin_username:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton("Сигнал Lucky Jet")
        btn4 = types.KeyboardButton("Сигнал Miner")
        btn5 = types.KeyboardButton("Admin Menu")
        markup.add(btn3, btn4, btn5)
        if message.text=='Admin Menu':
               bot.send_message(message.from_user.id,'Количество пользователей: {len(users)}')
               bot.send_message(message.from_user.id, "Список пользователей: \n {*users, sep='\n'}")
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn6 = types.KeyboardButton("Сигнал Lucky Jet")
        btn7 = types.KeyboardButton("Сигнал Miner")
        markup.add(btn6, btn7)
def us_language(message):
    if message.from_user.username==admin_username:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn8 = types.KeyboardButton("Signals Lucky Jet")
        btn9 = types.KeyboardButton("Signals Miner")
        btn10 = types.KeyboardButton("Admin Menu")
        markup.add(btn8, btn9, btn10)
        if message.text=='Admin Menu':
               bot.send_message(message.from_user.id,'Количество пользователей: {len(users)}')
               bot.send_message(message.from_user.id, "Список пользователей: \n {*users, sep='\n'}")
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn11 = types.KeyboardButton("Signals Lucky Jet")
        btn12 = types.KeyboardButton("Signals Miner")
        markup.add(btn11, btn12)
bot.polling()