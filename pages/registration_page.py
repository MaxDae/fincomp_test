from page import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from element import Element
from selenium.webdriver.support import expected_conditions as EC


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


class RelationType(object):
    business = "Ihr Unternehmen"
    employer = "Ihren Arbeitgeber"
    customers = "Ihren Kunden"
    client = "Ihren Mandanten"


class BusinessRelation(InputField):

    _relation = RelationType
    relation_type_locator = "//li[@data-testid='{0}']"
    SELECT_OPTIONS = (By.XPATH, "//ul[@data-testid='register-form-select-options']")
    FIELD_ERROR_MESSAGE = "//label[@for='businessRelation']/following-sibling::p[@id='name-error-text']"

    @property
    def error_msg_locator(self):
        locator = (By.XPATH, self.FIELD_ERROR_MESSAGE)
        return locator

    def fill(self, text):
        pass

    def clear(self):
        pass

    def set_relation(self, relation):
        self.click(*self.locator)
        self.click(*(By.XPATH, self.relation_type_locator.format(relation)))
        self.wait.until(
            EC.staleness_of(self.find_element(*self.SELECT_OPTIONS))
        )
        self._relation = relation

    def get_relation(self):
        return self._relation


class RegistrationPage(Page):

    GENDER = "//input[@name='gender' and @value='{0}']"

    REGISTER = (By.XPATH, "//button[@data-testid='register-form-submit']")

    @property
    def L_NAME(self):
        return InputField(self, "lastName")

    @property
    def  F_NAME(self):
        return InputField(self, "firstName")

    @property
    def EMAIL(self):
        return InputField(self, "email")

    @property
    def PHONE(self):
        return InputField(self, "phone")

    @property
    def business_relation(self):
        return BusinessRelation(self, "select-businessRelation")

    @property
    def loaded(self):
        return self.is_element_displayed(self.REGISTER)

    def set_gender(self, gender="m"):
        self.click(*(By.XPATH, self.GENDER.format(gender)))

    def register(self):
        return self.click(*self.REGISTER)