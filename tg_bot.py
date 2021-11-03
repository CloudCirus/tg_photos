import os
import time
import random

from dotenv import load_dotenv
from telegram import Bot


def send_photo(delay: int, repeat_after: int) -> None:
    load_dotenv()
    token = os.environ.get('TG_TOKEN')
    id = os.environ.get('CHANNEL_ID')

    bot = Bot(token)
    __antirepeat = []
    while True:
        file = random.choice(get_file_paths())
        if file in __antirepeat:
            continue
        bot.send_photo(chat_id=id,
                       photo=open(f'{file}', 'rb'))
        __antirepeat.append(file)
        if len(__antirepeat) == repeat_after:
            del __antirepeat[0]
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
    delay = []
    hours = os.environ.get('DELAY_HOURS')
    if hours:
        delay.append(int(hours)*3600)
    minutes = os.environ.get('DELAY_MINUTES')
    if minutes:
        delay.append(int(minutes)*60)
    seconds = os.environ.get('DELAY_SECONDS')
    if seconds:
        delay.append(int(seconds))
    delay = sum(delay)
    if not delay:
        day = 24*3600
        return day
    return delay


if __name__ == '__main__':
    delay_in_sec = get_delay()
    send_photo(delay_in_sec, repeat_after=10)
