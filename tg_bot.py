import os

import random
from dotenv import load_dotenv
from telegram import Bot


def send_message() -> None:
    TOKEN = os.environ.get('TG_TOKEN')

    bot = Bot(token=TOKEN)

    while input('Send message? y/n >>> ') in ['y', 'Y']:
        bot.send_message(chat_id='@WowSpaceClose',
                         text=input('input text >>> '))


def send_photo() -> None:
    TOKEN = os.environ.get('TG_TOKEN')

    bot = Bot(token=TOKEN)

    while input('Send photo? y/n >>> ') in ['y', 'Y']:
        index = random.randint(1, 10)
        bot.send_photo(chat_id='@WowSpaceClose',
                       photo=open(f'images/nasa/{index}_nasa.jpg', 'rb'))


if __name__ == '__main__':
    load_dotenv()
    send_photo()
