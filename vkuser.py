from pprint import pprint

import requests
from tqdm import tqdm


def max_size(sizes):
    return max(sizes, key=lambda item: item['height'] * item['width'])


class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, id, version='5.130', token='958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'):
        self.token = token
        self.version = version
        self.id = id
        self.params = {'access_token': self.token, 'v': version}

    def get_profile_photos(self):
        result = []
        additional_params = {'owner_id': self.id, 'album_id': 'profile', 'extended': 1, 'photo_sizes': 1}
        response = requests.get(self.url + 'photos.get', params={**self.params, **additional_params})
        photos = response.json()['response']['items']
        for photo in tqdm(photos):
            need_size = max_size(photo['sizes'])
            result.append({'likes': str(photo['likes']['count']), 'url': need_size['url'], 'date': str(photo['date']), 'type': need_size['type']})
        return result