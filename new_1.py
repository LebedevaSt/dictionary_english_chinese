import time

import telebot
import asyncio
from telebot import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, executor, types
import googletrans
from googletrans import Translator

translator_main = Translator(service_urls=['translate.googleapis.com'])
# bot = telebot.TeleBot('5460597839:AAGXpt7WiY6fiBrX250sAxt6f4Zo3GNNmqA')

bot = Bot(token='5460597839:AAGXpt7WiY6fiBrX250sAxt6f4Zo3GNNmqA')
dp = Dispatcher(bot=bot)

# ADDIING BUTTONS TO CHOOSE TO GET SYNONYMS OR DEFINITION OF A GIVEN WORD

english = InlineKeyboardButton(text="Английский", callback_data="english")
chinese = InlineKeyboardButton(text="Китайский", callback_data="chinese")
russian = InlineKeyboardButton(text="Русский", callback_data="russian")
row = InlineKeyboardMarkup(row_width=3)
EngChRu = InlineKeyboardMarkup().add(english,chinese,russian)







@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer(f'Привет, {message.chat.first_name} {message.chat.last_name}. Напиши слово для перевода )')



# MANAGING REGULAR MESSAGES
@dp.message_handler()
async def regular_messages(message: types.Message):
    global theword
    theword = message.text
    await message.answer("На какой язык переведим слово/фразу??", reply_markup=EngChRu)

# MANAGING KEYBOARD OPTIONS FOR english OR chinese
@dp.callback_query_handler(text=["english", "chinese","russian"])
async def engChRu(call: types.CallbackQuery):
    if call.data == "english":
        translation = translator_main.translate(text=theword, dest='en')
        await call.message.answer(translation.text)
        await asyncio.sleep(2)
        await call.message.answer('Введите слово/фразу для перевода')
    elif call.data == "chinese":
        translation = translator_main.translate(text=theword, dest='chinese (simplified)')
        await call.message.answer(translation.text)
        await asyncio.sleep(2)
        await call.message.answer('Введите слово/фразу для перевода')
    elif call.data == "russian":
        translation = translator_main.translate(text=theword, dest='russian')
        await call.message.answer(translation.text)
        await asyncio.sleep(2)
        await call.message.answer('Введите слово/фразу для перевода')
    else:
        await call.message.delete()
        await call.message.answer("This command doesn't work right now...")

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)

bot.polling(none_stop=True)
