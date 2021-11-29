import requests
import os
from pprint import pprint

TOKEN = 'AQAAAAAF6-4uAADLW96CeC1e-UNysejZC995nJ4'
path_local = os.path.join(os.getcwd(), 'Test_file.txt')


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()


if __name__ == '__main__':

    ya = YandexDisk(token=TOKEN)
    ya.upload_file_to_disk("Netology/'Test_file.txt'", path_local)
