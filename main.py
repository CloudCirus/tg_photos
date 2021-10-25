import os
import sys

import requests


def download_picture(url: str, filename: str) -> None:
    filepath = 'images'
    if not os.path.exists(filepath):
        try:
            os.makedirs(filepath)
        except FileExistsError as ex:
            print(ex)
    resp = requests.get(url)
    resp.raise_for_status()
    with open(f'{filepath}/{filename}', 'wb') as f:
        f.write(resp.content)


if __name__ == '__main__':
    hubble_url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    download_picture(hubble_url, 'hubble.jpeg')
