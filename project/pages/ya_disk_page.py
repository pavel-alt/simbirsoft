from typing import Union, List

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from framework.base_page import BasePage
from framework.button import Button
from framework.link import Link
from framework.text_field import TextField
from project.constants import URL_DISK, NAME_TEST_FOLDER_UI, NAME_TEST_DOC_UI, mail, password
from project.pages.authorization_page import AuthorizationPage
from project.pages.open_doc_page import OpenDocPage


class YaDiskPage(BasePage):
    check_element_xpath = '//span[contains(@class, "create")]/button'
    name = "DiskYandex"
    url = URL_DISK
    create_button_xpath = '//span[contains(@class, "create")]/button'
    create_dir_button_xpath = '//button[contains(@aria-label, "Папку")]'
    new_dir_name_textfield_xpath = '//input[contains(@text, "Новая папка")]'
    save_file_name_button_xpath = '//button[contains(@class, "confirmation-dialog__button_submit")]'
    custom_dir_link_xpath = f'//div[contains(@aria-label, "{NAME_TEST_FOLDER_UI}")]/parent::div/parent::div'  # f'//div[contains(@aria-label, {name_folder})]/span'
    create_doc_button_xpath = '//span[contains(@class, "doc")]/parent::button'
    new_doc_name_textfield_xpath = '//input[contains(@text, "Новый документ")]'
    all_file_xpath = '//div[contains(@class, "items")]//div[contains(@class, "item")]/span[contains(@title, "")]'
    test_file_xpath = f'//span[contains(@title, "{NAME_TEST_DOC_UI}")]/parent::div/parent::div'
    user_account_xpath = '//a[contains(@class, "user-account")]'
    logout_button_xpath = '//a[contains(@aria-label, "Выйти из аккаунта")]'
    second_enter_button_xpath = '//div[contains(@class, "ActionButtons_1")]/a[contains(@href, "https://passport.yandex.ru")]'
    lite_auth_link_xpath = '//a[contains(@href, "https://sso")]'

    def __init__(self, driver: Union[webdriver.Chrome]):
        super().__init__(driver)
        self.create_button = Button(driver, self.create_button_xpath)
        self.create_dir_button = Button(driver, self.create_dir_button_xpath)
        self.new_dir_name_textfield = TextField(driver, self.new_dir_name_textfield_xpath)
        self.save_file_name_button = Button(driver, self.save_file_name_button_xpath)
        self.custom_dir_link = Link(driver, self.custom_dir_link_xpath)
        self.create_doc = Button(driver, self.create_doc_button_xpath)
        self.new_doc_name_textfield = TextField(driver, self.new_doc_name_textfield_xpath)
        self.all_file = TextField(driver, self.all_file_xpath)
        self.test_file = Link(driver, self.test_file_xpath)
        self.user_account = Link(driver, self.user_account_xpath)
        self.logout_button = Link(driver, self.logout_button_xpath)
        self.second_enter_button = Link(driver, self.second_enter_button_xpath)
        self.lite_auth_link = Link(driver, self.lite_auth_link_xpath)

    def open_page(self) -> None:
        """Открывает страницу ЯндексДиск, при появлении 'обложки' повторно проходит авторизацию"""
        super().open_page()
        if self.second_enter_button.find_elements_by_xpath():
            self.second_enter_button.click_on_element()
            if self.lite_auth_link.find_elements_by_xpath():
                self.lite_auth_link.click_on_element()
            else:
                AuthorizationPage(self.driver).logining(mail, password)

    def create_dir(self, name_folder: str) -> None:
        """Создает папку"""
        self.create_button.click_on_element()
        self.create_dir_button.click_on_element()
        self.__name_the_dir(name_folder)

    def __name_the_dir(self, name_folder: str) -> None:
        self.new_dir_name_textfield.click_on_element()
        self.new_dir_name_textfield.send_text(name_folder)
        self.save_file_name_button.click_on_element()

    def open_dir(self) -> None:
        """Открывает папку"""
        self.custom_dir_link.double_click_on_element()

    def create_file(self, name_doc: str) -> OpenDocPage:
        """Создает документ"""
        self.create_button.click_on_element()
        self.create_doc.click_on_element()
        self.__name_the_doc(name_doc)
        return OpenDocPage(self.driver)

    def __name_the_doc(self, name_doc: str) -> None:
        self.new_doc_name_textfield.click_on_element()
        # sleep(5)
        self.new_doc_name_textfield.send_text(name_doc)
        # self.new_dir_name_textfield.clear_text_field()
        # sleep(5)
        self.save_file_name_button.click_on_element()

    def get_all_file(self) -> List[WebElement]:
        """Возвращает список файлов"""
        return self.all_file.find_elements_by_xpath()

    def logout(self) -> None:
        """Выход из аккаунта"""
        self.user_account.click_on_element()
        self.logout_button.click_on_element()
