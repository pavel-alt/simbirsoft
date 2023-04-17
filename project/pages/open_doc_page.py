from framework.base_page import BasePage


class OpenDocPage(BasePage):

    def close_file(self):
        """Закрывает вкладку с документом"""
        self.switch_to_page(self.driver.window_handles[1])
        self.driver.close()
        self.switch_to_page(self.driver.window_handles[0])

