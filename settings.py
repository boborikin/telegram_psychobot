import json
import os
from pathlib import Path

from aiogram import Bot
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR.joinpath('env'))
API_TOKEN = "1625412049:AAGuj82zDP8iaknJwoPhaLE54iCCX7wPuYY"

DATABASE = {
    "NAME": "test",
    "USER": "test",
    "PASSWORD": "1234qweasdzxcq",
    "HOST": "localhost",
}

# База данных/тип postgresql, mysql
DATABASE_TYPE = "postgresql"

DATABASE_STR = ""

if DATABASE_TYPE == "postgresql":
    DATABASE_STR = f"postgresql://{DATABASE['USER']}:{DATABASE['PASSWORD']}@{DATABASE['HOST']}/{DATABASE['NAME']}"

def get_words(file_name):
    data = {}
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

WORDS = get_words(r'dictionary.json')

# Канал с отзывами
# REVIEWS_CHANNEL = '@psyxologyreviews'
REVIEWS_CHANNEL = '@Mindlybot_reviews'
# диалог с разработчиком
DEVELOPER_DIALOG = '@mindlybot_service'
# DEVELOPER_DIALOG = '@alexandrvs1'
#NOT_WORD_DIALOG = 911357472
NOT_WORD_DIALOG = 916718512
SITE = 'mindfulness_bot.com'

bot = Bot(token=API_TOKEN, parse_mode='HTML')
