import os
import time
import random

from dotenv import load_dotenv
from telegram import Bot


def send_photo(delay: int, token: str, id: str) -> None:
    bot = Bot(token)
    while True:
        paths = get_file_paths()
        random.shuffle(paths)
        print(paths)
        for path in paths:
            with open(f'{path}', 'rb') as photo:
                bot.send_photo(chat_id=id, photo=photo)
            time.sleep(delay)


def get_file_paths() -> list:
    images_dir = os.walk('images')
    paths = []
    for path, _, files in images_dir:
        for file in files:
            paths.append(os.path.join(path, file))
    return paths


def count_delay(hours: int, min: int, sec: int) -> int:
    delay_in_sec = sum((hours*3600, min*60, sec))
    return delay_in_sec or 24 * 60 * 60


def main() -> None:
    load_dotenv()
    tg_token = os.environ.get('TG_TOKEN')
    channel_id = os.environ.get('CHANNEL_ID')
    hours = int(os.environ.get('DELAY_HOURS', default=0))
    minutes = int(os.environ.get('DELAY_MINUTES', default=0))
    seconds = int(os.environ.get('DELAY_SECONDS', default=0))

    delay_in_sec = count_delay(hours, minutes, seconds)
    send_photo(delay_in_sec, tg_token, channel_id)


if __name__ == '__main__':
    main()
