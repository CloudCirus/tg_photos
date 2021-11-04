import os
import time
import random

from dotenv import load_dotenv
from telegram import Bot


def send_photo(delay: int) -> None:
    load_dotenv()
    token = os.environ.get('TG_TOKEN')
    id = os.environ.get('CHANNEL_ID')

    bot = Bot(token)
    while True:
        paths = get_file_paths()
        random.shuffle(paths)
        print(paths)
        for path in paths:
            bot.send_photo(chat_id=id, photo=open(f'{path}', 'rb'))
            time.sleep(delay)


def get_file_paths() -> list:
    images_dir = os.walk('images')
    paths = []
    for path, _, files in images_dir:
        for file in files:
            paths.append(os.path.join(path, file))
    return paths


def get_delay() -> int:
    load_dotenv()
    hours = int(os.environ.get('DELAY_HOURS'))
    minutes = int(os.environ.get('DELAY_MINUTES'))
    seconds = int(os.environ.get('DELAY_SECONDS'))
    delay_in_sec = sum((hours*3600, minutes*60, seconds))
    return delay_in_sec or 24 * 60 * 60


if __name__ == '__main__':
    delay_in_sec = get_delay()
    send_photo(delay_in_sec)
