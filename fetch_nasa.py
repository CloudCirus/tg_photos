import argparse
import os
from datetime import datetime, timedelta
from pprint import pprint

import requests
from dotenv import load_dotenv

from storage import download_pictures


def get_nasa_apod_img_links(days: int) -> None:
    load_dotenv()
    url = 'https://api.nasa.gov/planetary/apod'
    options = {
        'api_key': os.environ.get('NASA_API_KEY'),
        'start_date': (datetime.now() - timedelta(days)).strftime('%Y-%m-%d'),
        'end_date': datetime.now().strftime('%Y-%m-%d'),
    }
    resp = requests.get(url, params=options)
    resp.raise_for_status()
    links = []
    for day in resp.json():
        if day.get('media_type') == 'image':
            url = day.get('url')
            if url:
                links.append(url)
    return links


def get_nasa_epic_img_links(days: int) -> list:
    load_dotenv()
    url_all = 'https://api.nasa.gov/EPIC/api/natural/all'
    options = {
        'api_key': os.environ.get('NASA_API_KEY')
    }
    resp = requests.get(url_all, params=options)
    resp.raise_for_status()

    links = []
    for day in resp.json()[:days]:
        date = day.get('date')
        url_date = 'https://api.nasa.gov/EPIC/api/natural/date/' + date
        resp_day = requests.get(url_date, params=options).json()[0]

        image = resp_day.get('image')
        date = date.replace('-', '/')
        url_img = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png \
                    ?api_key={options.get("api_key")}'
        links.append(url_img)
    return links


def fetch_nasa_apods(days) -> None:
    links = get_nasa_apod_img_links(days)
    download_pictures(links, 'nasa')


def fetch_nasa_epic_imgs(days):
    links = get_nasa_epic_img_links(days)
    download_pictures(links, 'nasa_epic')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--apods', type=int, help='number of day to dwload nasa apods pics', default=10)
    parser.add_argument(
        '--epic', type=int, help='number of day to dwload nasa epic pics', default=10)
    args = parser.parse_args()

    fetch_nasa_apods(args.apods)
    fetch_nasa_epic_imgs(args.epic)


if __name__ == '__main__':
    main()
