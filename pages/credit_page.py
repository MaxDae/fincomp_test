from page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from company_search_page import CompanySearch


class Credit(BasePage):
    URL_TEMPLATE = "/products/credit"

    AMOUNT_INPUT = (By.ID, "amount")
    PURPOSE_DROPDOWN = (By.ID, "select-purpose")
    TERM_DROPDOWN = (By.ID, "select-term")
    SUBMIT = (By.XPATH, "//button[@type='submit']")
    ROOT = (By.TAG_NAME, "body")
    MENU_PURPOSE = (By.XPATH, "//div[@id='menu-purpose']")
    MENU_TERM = (By.XPATH, "//div[@id='menu-term']")

    AWAILABLE_MONTH_TERM = [3, 6, 12, 24, 48, 60, 72, 84, 96, 108, 120]

    @property
    def loaded(self):
        return self.is_element_displayed(By.ID, "amount")

    def select_purpose(self, purpose):
        self.click(*self.PURPOSE_DROPDOWN)
        self.click(*(By.XPATH, "//li[@data-testid='{0}']".format(purpose)))
        self.wait.until(EC.invisibility_of_element_located(self.MENU_PURPOSE))

    def select_term(self, term):
        if term in self.AWAILABLE_MONTH_TERM:
            self.wait.until(EC.invisibility_of_element_located(self.MENU_TERM))
            self.click(*self.TERM_DROPDOWN)
            self.click(*(By.XPATH, "//li[@data-value='{0}']".format(str(term))))
        else:
            raise Exception("Not allowed term! Please choose term from {0}".format(str(self.AWAILABLE_MONTH_TERM)))

    def type_amount(self, amount):

        self.type_text(str(amount), *self.AMOUNT_INPUT)

    def submit(self):
        self.wait.until(EC.invisibility_of_element_located(self.MENU_TERM) and
                        EC.invisibility_of_element_located(self.MENU_PURPOSE))
        self.click(*self.SUBMIT)
        return CompanySearch(self.driver_adapter)


class Purpose(object):
    facilities_equipment = 'Betriebsmittel'
    resource = 'Anlagen / Ausstattung'
    purchase_financing = "Einkaufsfinanzierung"
    software = "Software / IT / DEV"

