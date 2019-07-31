from .Page import Page
from .CreditPage import CreditPage as C
from selenium.webdriver.common.by import By

class BasePage(Page):
    URL_TEMPLATE = '/wizard'

    CREDIT_PRODUCT_IMG = (By.XPATH, "//h2[contains(text(), 'Kredit')]")

    @property
    def loaded(self):
        return self.is_element_displayed(By.CSS_SELECTOR, "div.funnel__products")

    def select_credit(self):
        self.click(*self.CREDIT_PRODUCT_IMG)
        return C(self.driver_adapter)

