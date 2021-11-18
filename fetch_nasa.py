import argparse
import os
from datetime import datetime, timedelta

import requests
from dotenv import load_dotenv

from storage import download_pictures, create_dir


def fetch_nasa_apods(days: int, api_key: str, storage_name: str, whose_pic_name: str) -> None:
    url = 'https://api.nasa.gov/planetary/apod'
    options = {
        'api_key': api_key,
        'start_date': (datetime.now() - timedelta(days)).strftime('%Y-%m-%d'),
        'end_date': datetime.now().strftime('%Y-%m-%d'),
    }
    resp = requests.get(url, params=options)
    resp.raise_for_status()
    links = []
    for day in resp.json():
        if day.get('media_type') == 'image':
            url = day.get('url')
            links.append(url)
    path = create_dir(storage_name, whose_pic_name)
    download_pictures(links, path, whose_pic_name, options)


def fetch_nasa_epic_imgs(days: int, api_key: str, storage_name: str, whose_pic_name: str) -> None:
    url_all = 'https://api.nasa.gov/EPIC/api/natural/all'
    options = {
        'api_key': api_key
    }
    resp = requests.get(url_all, params=options)
    resp.raise_for_status()

    links = []
    for day in resp.json()[:days]:
        date = day.get('date')
        url_date = f'https://api.nasa.gov/EPIC/api/natural/date/{date}'
        resp_day = requests.get(url_date, params=options)
        resp_day.raise_for_status()
        resp_day = resp_day.json()[0]
        image = resp_day.get('image')
        date = date.replace('-', '/')
        url_img = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png'
        links.append(url_img)
    path = create_dir(storage_name, whose_pic_name)
    download_pictures(links, path, whose_pic_name, options)


def main() -> None:
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--apods', type=int, help='number of day to download nasa apods pics', default=10)
    parser.add_argument(
        '--epic', type=int, help='number of day to download nasa epic pics', default=10)
    args = parser.parse_args()

    days_apods = args.apods
    days_epic = args.epic
    api_key = os.environ.get('NASA_API_KEY')
    storage_name = os.environ.get('STORAGE_NAME', default='images')

    fetch_nasa_apods(days_apods, api_key, storage_name, 'nasa')
    # fetch_nasa_epic_imgs(days_epic, api_key, storage_name, 'nasa_epic')


if __name__ == '__main__':
    main()
