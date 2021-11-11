import os

import requests
from dotenv import load_dotenv

from storage import download_pictures


def get_spx_last_launch_img_links() -> list:
    url = f'https://api.spacexdata.com/v5/launches/'
    all_launches_resp = requests.get(url)
    all_launches_resp.raise_for_status()

    for launch in reversed(all_launches_resp.json()):
        launch_imgs = launch['links']['flickr'].get('original')
        if launch_imgs:
            last_launch_with_imgs = {
                'flight_number': launch.get('flight_number'),
                'links': launch_imgs,
            }
            break
    return last_launch_with_imgs.get('links')


def fetch_spacex_last_launch(path: str, whose_pic_name: str) -> None:
    last_launch = get_spx_last_launch_img_links()
    download_pictures(last_launch, path, whose_pic_name)


if __name__ == '__main__':
    load_dotenv()
    path = os.environ.get('STORAGE_PATH', default='images')
    fetch_spacex_last_launch(path, 'spacex')
