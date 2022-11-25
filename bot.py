import telebot
from telebot import types
from config import TOKEN
from main import get_weather_data, generate_button, names_city, list_city


bot = telebot.TeleBot(TOKEN)

materics = ['Америка','Европа','Африка','Австралия','Азия']

@bot.message_handler(commands=['start'])
def start_handler(message: types.Message):
    markup = generate_button(*materics)
    text = 'Привет я бот погоды 🥶🥵🥴🤯. \n Отправь мне название любого города!'
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text_handler(message: types.Message):
    if message.chat.type == 'private':
        if message.text in materics:
            markup = generate_button(*names_city[message.text])
            bot.send_message(message.chat.id, 'Выбери город',reply_markup=markup)
        
        elif message.text == 'Меню':
            markup = generate_button(*materics)
            text = 'Отправь мне название любого города!'
            bot.send_message(message.chat.id, text, reply_markup=markup)
        elif message.text in list_city:
            response = get_weather_data(message.text)
            bot.send_message(message.chat.id, response)
    
        else:
            bot.send_message(message.chat.id, 
                f'Проверь правильность название города {message.text} 🧐')        

bot.polling(non_stop=True)

