from .RelationType import RelationType
from .InputField import InputField
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Element import Element
from selenium.webdriver.support import expected_conditions as EC


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


