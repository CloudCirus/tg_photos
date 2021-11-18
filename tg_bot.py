import os
import time
import random

from dotenv import load_dotenv
from telegram import Bot


def send_photos(delay: int, token: str, id: str, path: str) -> None:
    bot = Bot(token)
    while True:
        paths = get_file_paths(path)
        random.shuffle(paths)
        for path in paths:
            with open(f'{path}', 'rb') as photo:
                bot.send_photo(chat_id=id, photo=photo)
            time.sleep(delay)


def get_file_paths(path: str) -> list:
    image_dirs = os.walk(path)
    paths = []
    for path, _, files in image_dirs:
        for file in files:
            paths.append(os.path.join(path, file))
    return paths


def count_delay(hours: int, min: int, sec: int) -> int:
    delay_in_sec = sum((hours * 3600, min * 60, sec))
    return delay_in_sec or 24 * 60 * 60


def main() -> None:
    load_dotenv()
    tg_token = os.environ.get('TG_TOKEN')
    channel_id = os.environ.get('CHANNEL_ID')
    hours = int(os.environ.get('DELAY_HOURS', default=0))
    minutes = int(os.environ.get('DELAY_MINUTES', default=0))
    seconds = int(os.environ.get('DELAY_SECONDS', default=0))
    path = os.environ.get('STORAGE_PATH', default='images')

    delay_in_sec = count_delay(hours, minutes, seconds)
    send_photos(delay_in_sec, tg_token, channel_id, path)


if __name__ == '__main__':
    main()
