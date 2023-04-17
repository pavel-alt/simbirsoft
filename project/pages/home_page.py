from framework.base_page import BasePage
from framework.button import Button
from framework.link import Link
from project.constants import URL_HOME


class HomePage(BasePage):
    check_element_xpath = "//span[contains(@aria-label, 'Логотип Дзен')]"
    name = 'HomePage'
    url = URL_HOME
    enter_button_xpath = "//button[contains(@aria-label, 'Войти')]"  # класс Button
    enter_yandex_id_link_xpath = "//a[contains(@aria-label, 'Войти через Яндекс ID')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.enter_button = Button(driver, self.enter_button_xpath)
        self.enter_yandex_id_link = Link(driver, self.enter_yandex_id_link_xpath)

    def click_enter_button(self) -> None:
        """Нажимает кнопку Войти"""
        self.enter_button.click_on_element()

    def click_enter_yandex_id_link(self) -> None:
        """Нажимает кнопку Войти через Яндекс ID"""
        self.enter_yandex_id_link.click_on_element()
