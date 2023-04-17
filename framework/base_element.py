from abc import ABC
from typing import List, Union
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BaseElement(ABC):
    name = ""

    def __init__(self, driver: Union[webdriver.Chrome], xpath):
        self.driver = driver
        self.xpath = xpath

    def find_element_by_xpath(self) -> WebElement:
        """Поиск елемента по Хпасу"""
        return self.driver.find_element(by=By.XPATH, value=self.xpath)

    def find_elements_by_xpath(self) -> List[WebElement]:
        """Поиск списка элементов по Хпасу"""
        return self.driver.find_elements(by=By.XPATH, value=self.xpath)

    def check_visibility(self) -> bool:
        """Проверить видимость элемента"""
        return self.find_element_by_xpath().is_displayed()

    def double_click_on_element(self) -> None:
        """Двойной клик по элементу"""
        clickable = self.find_element_by_xpath()
        ActionChains(self.driver).double_click(clickable).perform()

    def click_on_element(self) -> None:
        """Клик по элементу"""
        try:
            self.find_element_by_xpath().click()
        except:
            pass

