from .Page import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .Element import Element
from selenium.webdriver.support import expected_conditions as EC
from .RelationType import RelationType
from .InputField import InputField



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