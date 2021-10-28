import argparse
import os
from datetime import datetime, timedelta
from urllib.parse import urlsplit

import requests
from dotenv import load_dotenv


def download_pictures(links: list, whose_pic_name: str) -> None:
    path = f'images/{whose_pic_name}'
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except FileExistsError as ex:
            print(ex)

    for index, link in enumerate(links, start=1):
        resp = requests.get(link)
        resp.raise_for_status()
        ext = _get_file_extension(link)
        with open(f'{path}/{index}_{whose_pic_name}{ext}', 'wb') as f:
            f.write(resp.content)


def _get_file_extension(url: str) -> str:
    path = urlsplit(url).path
    return os.path.splitext(path)[1]


def get_all_spx_launches_id() -> list:
    url = f'https://api.spacexdata.com/v5/launches/'
    resp = requests.get(url)
    resp.raise_for_status()
    return [lounch['id'] for lounch in resp.json()]


def get_spx_last_launch_img_links(launches_id: list) -> list:
    url_launches = f'https://api.spacexdata.com/v5/launches/'
    last_launch_with_imgs = {}
    counter = 1
    for id in reversed(launches_id):
        url = f'{url_launches}{id}'
        resp = requests.get(url).json()
        launch_imgs = resp['links']['flickr'].get('original')
        if launch_imgs:
            last_launch_with_imgs = {
                'flight_number': resp.get('flight_number'),
                'id': id,
                'links': launch_imgs
            }
            break
        counter += 1
    return last_launch_with_imgs.get('links')


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
    url_info = 'https://api.nasa.gov/EPIC/api/natural/all'
    options = {
        'api_key': os.environ.get('NASA_API_KEY')
    }
    resp = requests.get(url_info, params=options)
    resp.raise_for_status()

    key = options.get('api_key')
    links = []
    for day in resp.json()[:days]:
        date = day.get('date').replace('-', '/').split()[0]
        image = day.get('image')
        url_img = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png?api_key={key}'
        links.append(url_img)
    return links


def fetch_spacex_last_launch() -> None:
    launches_id = get_all_spx_launches_id()
    last_launch = get_spx_last_launch_img_links(launches_id)
    download_pictures(last_launch, 'spacex')


def fetch_nasa_apods(days) -> None:
    links = get_nasa_apod_img_links(days)
    download_pictures(links, 'nasa')


def fetch_nasa_epic_imgs(days):
    links = get_nasa_epic_img_links(days)
    download_pictures(links, 'nasa_epic')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--spx', type=bool,
        help='download spacex lastlaunch pics')
    parser.add_argument(
        '--apods', type=int, help='number of day to dwload nasa apods pics', default=1)
    parser.add_argument(
        '--epic', type=int, help='number of day to dwload nasa epic pics', default=1)
    args = parser.parse_args()
    print('Wait for downloading...')
    if args.spx:
        fetch_spacex_last_launch()
    fetch_nasa_apods(args.apods)
    fetch_nasa_epic_imgs(args.epic)


if __name__ == '__main__':
    main()
