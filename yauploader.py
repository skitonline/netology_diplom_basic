import json
from pprint import pprint

import requests
from tqdm import tqdm


class YaUploader:
    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': self.token}

    def _create_folder(self, name):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': name}
        requests.put(url=url, params=params, headers=self.headers)

    def _upload(self, url_file, path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'url': url_file, 'path': path}
        response = requests.post(url=url, params=params, headers=self.headers)

    def upload_photo_from_vk(self, vk_user):
        folder_name = 'vk_photo'
        self._create_folder(folder_name)
        photos = vk_user.get_profile_photos()
        names = []
        fields_photo = []
        for photo in tqdm(photos):
            if photo['likes'] not in names:
                name = photo['likes']
            else:
                name = photo['likes'] + '_' + photo['date']
            names.append(name)
            path = folder_name + '/' + name
            self._upload(photo['url'], path)
            fields_photo.append({'file_name': name, 'size': photo['type']})
        with open('fields_photo', 'w') as f:
            json.dump(fields_photo, f, ensure_ascii=False, indent=2)