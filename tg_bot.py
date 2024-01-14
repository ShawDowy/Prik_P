import requests
import datetime
import telebot
bot = telebot.TeleBot('6765450140:AAF-C7RCcPNxZNxXQShVd4aOr63sawwsKGA')
open_weather_token = "15e1abea6ac4b5f63f3a5ad569c55d60"

def get_weather(city, token):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric"
        )
        data = r.json()
        city = data["name"]
        temp = data["main"]["temp"]
        weather = data["weather"][0]["main"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        return (f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода в городе: {city}\nТемпература: {temp} C\nВлажность: {humidity} %\nДавление: {pressure} мм.рт.ст.\n"
              f"Скорость ветра: {wind_speed} m/c\nПродолжительность дня: {length_of_the_day}\nПогода: {weather}\n"
              f"Да-да и никакой не вздор!")
    except Exception as ex:
        return "Введите правильное название"

@bot.message_handler(commands=['weather'])
def weather_command(message):
    try:
        city = message.text.split()[-1]
        weather_info = get_weather(city, open_weather_token)
        bot.reply_to(message, weather_info)
    except IndexError:
        bot.reply_to(message, "Введите название города после команды /weather")

bot.polling()
