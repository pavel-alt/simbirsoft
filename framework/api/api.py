from abc import ABC

import requests
from requests import Response


class API(ABC):
    """ Базовый класс для API соединения """

    def __init__(self, base_url: str):
        self.url = base_url
        self.headers = None

    def get(self, uri: str, **kwargs) -> Response:
        url = self.url + uri
        return requests.get(url, headers=self.headers, **kwargs)

    def post(self, uri: str, **kwargs) -> Response:
        url = self.url + uri
        return requests.post(url, headers=self.headers, **kwargs)

    def delete(self, uri: str, **kwargs) -> Response:
        url = self.url + uri
        return requests.delete(url, headers=self.headers, **kwargs)

    def put(self, uri: str = None, full_url: str = None, **kwargs) -> Response:
        url = self.url + uri if uri else full_url
        return requests.put(url, headers=self.headers, **kwargs)
