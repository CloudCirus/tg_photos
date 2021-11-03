import requests

from storage import download_pictures


def get_all_spx_launches_id() -> list:
    url = f'https://api.spacexdata.com/v5/launches/'
    resp = requests.get(url)
    resp.raise_for_status()
    return [launch['id'] for launch in resp.json()]


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


def fetch_spacex_last_launch() -> None:
    launches_id = get_all_spx_launches_id()
    last_launch = get_spx_last_launch_img_links(launches_id)
    download_pictures(last_launch, 'spacex')


if __name__ == '__main__':
    print('Wait for downloading...')
    fetch_spacex_last_launch()
