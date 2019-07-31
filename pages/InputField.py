from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .Element import Element

class InputField(Element):
    _filled = False
    strategy = By.ID
    value = ""
    FIELD_ERROR_MESSAGE = "//label[@for='{0}']/following-sibling::p[@id='name-error-text']"
    _text = ""


    @property
    def locator(self):
        locator = (self.strategy, self.value)
        return locator

    @property
    def error_msg_locator(self):
        locator = (By.XPATH, self.FIELD_ERROR_MESSAGE.format(self.value))
        return locator

    def get_error_msg(self):
        try:
            return self.find_element(*self.error_msg_locator).text
        except NoSuchElementException:
            return None

    def fill(self, text):
        if not self._filled:
            self.type_text(text, *self.locator)
            self._text = text
            self._filled = True
        else:

            self.clear()
            self.type_text(text, *self.locator)
            self._text = text

    def clear(self):
        self.clear_text_field(*self.locator)
        self._text = ""

