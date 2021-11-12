import os
from urllib.parse import urlparse, unquote

import requests


def download_pictures(links: list, path: str, whose_pic_name: str, options=None) -> None:
    path = create_dir(path, whose_pic_name)

    for index, link in enumerate(links, start=1):
        resp = requests.get(link, params=options)
        resp.raise_for_status()
        ext = get_file_extension(link)
        with open(f'{path}/{index}_{whose_pic_name}{ext}', 'wb') as f:
            f.write(resp.content)


def create_dir(path: str, whose_pic_name: str) -> str:
    path = f'{path}/{whose_pic_name}'
    os.makedirs(path, exist_ok=True)
    return path


def get_file_extension(url: str) -> str:
    components = urlparse(unquote(url, encoding='utf-8'))
    return os.path.splitext(components.path)[-1]
