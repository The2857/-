from telebot.async_telebot import AsyncTeleBot
import asyncio
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import datetime
from shluedeweek import list_of_days
from tokenname import API_TOKEN


week = datetime.datetime.today()
today_week = int(week.strftime('%U'))


day = datetime.datetime.today()
today_day = day.today().weekday() + 1
print(today_day)

list_of_days = list_of_days

API_TOKEN = API_TOKEN


bot = AsyncTeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
async def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('Какое сегодня расписание'))
    markup.add(KeyboardButton('Какая сегодня неделя'))

    # display this markup:
    await bot.send_message(message.chat.id, text='\
    Здарова \
    ', reply_markup=markup)


@bot.message_handler(content_types=['text'])
async def schedule_func(message):
    if (message.text == 'Какое сегодня расписание') and (today_day in list_of_days):
        await bot.send_message(message.chat.id, text=f'{list_of_days[today_day]}')
    else:
        if (message.text == 'Какая сегодня неделя') and (today_week % 2 == 0):
            await bot.send_message(message.chat.id, text='Сегодня неделя - "Знаменатель"')
        elif (message.text == 'Какая сегодня неделя') and (today_week % 2 != 0):
            await bot.send_message(message.chat.id, text='Сегодня неделя - "Числитель"')


asyncio.run(bot.polling())