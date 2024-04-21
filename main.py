import sqlite3
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from logic import *
from config import *

bot = TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, f'Привет, @{message.from_user.username}!\nЗдесь ты можешь надёжно сохранять свои проекты! Надежное хранилище для твоего творчества!')


bot.infinity_polling()
