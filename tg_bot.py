import os

from dotenv import load_dotenv
from telegram import Bot


def send_message() -> None:
    load_dotenv()
    TOKEN = os.environ.get('TG_TOKEN')

    bot = Bot(token=TOKEN)

    while input('Send message? y/n >>> ') in ['y', 'Y']:
        bot.send_message(chat_id='@WowSpaceClose', text=input('input text >>> '))


if __name__ == '__main__':
    send_message()
