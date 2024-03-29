from framework.base_element import BaseElement


class TextField(BaseElement):
    def get_placeholder(self) -> str:
        """Возвращает плейсхолдер"""
        return self.find_element_by_xpath().get_attribute("placeholder")

    def clear_text_field(self) -> None:
        """Очищает поле ввода"""
        entry_field = self.find_element_by_xpath()
        entry_field.clear()

    def send_text(self, text: str) -> None:
        """Вводит текст в поле"""
        self.find_element_by_xpath().send_keys(text)
