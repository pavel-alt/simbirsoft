from framework.base_page import BasePage
from framework.button import Button
from framework.text_field import TextField
from project.constants import URL_AUTH


class AuthorizationPage(BasePage):
    check_element_xpath = "//span[contains(@class, 'passp-add-account-page-title')]"
    name = "AuthorizationPage"
    text_field_mail_xpath = '//input[contains(@data-t, "field:input-login")]'
    text_field_password_xpath = '//input[contains(@data-t, "field:input-passwd")]'
    creds_accept_button_xpath = '//button[@id="passp:sign-in"]'
    change_mail_way_button_xpath = "//span[text()='Почта']"
    url = URL_AUTH

    def __init__(self, driver):
        super().__init__(driver)
        self.text_field_mail = TextField(driver, self.text_field_mail_xpath)
        self.text_field_password = TextField(driver, self.text_field_password_xpath)
        self.creds_accept_button = Button(driver, self.creds_accept_button_xpath)
        self.change_mail_way_button = Button(driver, self.change_mail_way_button_xpath)

    def change_mail_way(self) -> None:
        """Выбор способа авторизации по почте"""
        self.change_mail_way_button.click_on_element()

    def logining(self, mail, password) -> None:
        """Ввод логина (почты) и пароля"""
        self.__send_mail(mail)
        self.__send_password(password)

    def __send_mail(self, mail) -> None:
        self.text_field_mail.send_text(mail)
        self.creds_accept_button.click_on_element()

    def __send_password(self, password) -> None:
        self.text_field_password.send_text(password)
        self.creds_accept_button.click_on_element()
