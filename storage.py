import os
from urllib.parse import urlsplit

import requests


def download_pictures(links: list, whose_pic_name: str) -> None:
    path = create_dir(whose_pic_name)

    for index, link in enumerate(links, start=1):
        resp = requests.get(link)
        resp.raise_for_status()
        ext = get_file_extension(link)
        with open(f'{path}/{index}_{whose_pic_name}{ext}', 'wb') as f:
            f.write(resp.content)


def create_dir(whose_pic_name: str) -> str:
    path = f'images/{whose_pic_name}'
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def get_file_extension(url: str) -> str:
    path = urlsplit(url).path
    return os.path.splitext(path)[1]
