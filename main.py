import os
from pprint import pprint

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


def get_all_launches_id(url: str):
    resp_all_launches = requests.get(url).json()
    return [lounch['id'] for lounch in resp_all_launches]


def get_last_launch_with_img(launches_id: list, url: str) -> dict:
    url_launches = f'https://api.spacexdata.com/v5/launches/'
    last_launch_with_imgs = {}
    counter = 1
    print(counter)
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
        print(counter)
    return last_launch_with_imgs


if __name__ == '__main__':
    url_launches = 'https://api.spacexdata.com/v5/launches/'
    launches_id = get_all_launches_id(url_launches)
    pprint(get_last_launch_with_img(launches_id, url_launches))
