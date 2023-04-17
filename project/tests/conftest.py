import pytest
from selenium import webdriver

from framework.browser_factory import BrowserFactory
from project.api_yandex_disk.api_yandex_disk import ApiYandexDisc
from project.constants import URL_JA_DISK
from project.pages.ya_disk_page import YaDiskPage


@pytest.fixture(scope='session')
def driver() -> webdriver.Chrome:
    instance_driver = BrowserFactory.get_driver()
    yield instance_driver
    YaDiskPage(instance_driver).logout()


@pytest.fixture(scope='session')
def api_yandex() -> ApiYandexDisc:
    api = ApiYandexDisc(URL_JA_DISK)
    api.set_headers()
    yield api


