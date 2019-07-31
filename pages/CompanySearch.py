from .Page import Page
from .RegistrationPage import RegistrationPage
from selenium.webdriver.common.by import By


class CompanySearch(Page):
    URL_TEMPLATE = '/wizard/company/search'

    COMPANY_NAME_INPUT = (By.ID, "companyName")
    LOOKING_FOR_COMPANIES = (By.XPATH, "//button[@data-testid='company-search-submit']")
    COMPANY_SEARCH_CARD = (By.XPATH, "//div[@data-testid='company-search-card']")
    SEARCH_RESULT_CARD = "//div[contains(@class, 'funnel__step__company')]/descendant::font[contains(text(), '{0}')]"

    @property
    def loaded(self):
        return self.is_element_displayed(self.COMPANY_NAME_INPUT)

    def search_for_company(self, company_name):
        self.type_text(company_name, *self.COMPANY_NAME_INPUT)
        self.click(*self.LOOKING_FOR_COMPANIES)

    def select_search_result(self, company_name):
        self.click(*self.COMPANY_SEARCH_CARD)
        return RegistrationPage(self.driver_adapter)
