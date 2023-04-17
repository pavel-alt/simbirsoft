from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class BrowserFactory:
    @staticmethod
    def get_driver() -> webdriver.Chrome:
        """Возвращает драйвер браузера Chrome"""
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.implicitly_wait(10)
        return driver
