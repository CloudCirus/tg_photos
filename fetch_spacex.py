import os

import requests
from dotenv import load_dotenv

from storage import download_pictures, create_dir


def get_spx_last_launch_img_links() -> list:
    url = f'https://api.spacexdata.com/v5/launches/'
    all_launches_resp = requests.get(url)
    all_launches_resp.raise_for_status()

    for launch in reversed(all_launches_resp.json()):
        launch_imgs = launch['links']['flickr'].get('original')
        if launch_imgs:
            return launch_imgs


def fetch_spacex_last_launch(storage_name: str, whose_pic_name: str) -> None:
    last_launch = get_spx_last_launch_img_links()
    path = create_dir(storage_name, whose_pic_name)
    download_pictures(last_launch, path, whose_pic_name)


if __name__ == '__main__':
    load_dotenv()
    storage_name = os.environ.get('STORAGE_NAME', default='images')
    fetch_spacex_last_launch(storage_name, 'spacex')
