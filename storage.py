import os
from urllib.parse import urlparse, unquote

import requests


def download_pictures(links: list, path: str, whose_pic_name: str, params=None) -> None:
    for index, link in enumerate(links, start=1):
        resp = requests.get(link, params=params)
        resp.raise_for_status()
        ext = get_file_extension(link)
        file_name = f'{index}_{whose_pic_name}{ext}'
        with open(f'{path}/{file_name}', 'wb') as f:
            f.write(resp.content)


def create_dir(storage_name: str, whose_pic_name: str) -> str:
    path = f'{storage_name}/{whose_pic_name}'
    os.makedirs(path, exist_ok=True)
    return path


def get_file_extension(url: str) -> str:
    components = urlparse(unquote(url, encoding='utf-8'))
    return os.path.splitext(components.path)[-1]
