import requests
from config import API_KEY
from pprint import pprint
from datetime import datetime
from telebot import types

code_to_smile = {
        'Clear': "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }



def get_weather(city, API_KEY):
    try: 
        url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_KEY + "&units=metric"
    except Exception as e:
        print(e)
        return None
    r = requests.get(url)
    return r.json()

def get_weather_data(city):
    weather_data = get_weather(city, API_KEY)
    if weather_data is None:
        return None
    print(weather_data['cod'])
    if weather_data['cod'] == '404':
        return None
    city = weather_data['name']
    cur_weather = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    pressure = weather_data['main']['pressure']
    wind_speed = weather_data['wind']['speed']
    sunrise = datetime.fromtimestamp(weather_data['sys']['sunrise'])
    sunset = datetime.fromtimestamp(weather_data['sys']['sunset'])
    long_of_day = sunset - sunrise
    weather_desc = weather_data['weather'][0]['main']

    if weather_desc in code_to_smile:
        wd = code_to_smile[weather_desc]
    else:
        wd = "Посмотри в окно, не пойму что за погода там!"

    return f"""
Сегодня: {datetime.now().strftime('%m/%d/%Y %H:%M:%S')}
Город: {city}
Температура: {cur_weather} °C {wd}
Влажность: {humidity}
Давление: {pressure} мм.рт.ст
Скорость ветра: {wind_speed}
Восход: {sunrise}
День: {long_of_day}
Закат: {sunset}
""" 






names_city = {
    'Америка': ['Нью-Йорк', 'Washigton' ],
    'Европа': ['London', 'Paris', 'Atyrau', 'Astana'],
    'Африка': ['Тунис', 'Алжир', 'Египет', 'Сомали'],
    'Австралия': ['Сидней', 'Кейптаун'],
    'Азия': ['Кабул', 'Пекин', 'Куала-Лумпур', 'Гонконг'],
}

list_city = []
for i in names_city.values():
    for j in i:
        list_city.append(j)



def generate_button(*args):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.max_row_keys = 3
    markup.row(*args, 'Меню')
    return markup




