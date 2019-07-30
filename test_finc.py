# coding: utf-8
import pytest
import pages
from pages.page import BasePage


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(10)
    return selenium


@pytest.mark.capabilities
class Test():

    error_msg = "Dieses Feld ist ein Pflichtfeld"
    wrong_mail_err_msg = u"Gib eine gültige E-Mail Adresse an."
    wrong_phone_num_err_msg = u"Bitte geben Sie eine richtige Telefonnummer ein"

    @pytest.mark.parametrize(
        "company_name",  ["FinCompare GmbH"])
    def test_open_url(self, selenium, variables, company_name):

        credit_page = BasePage(selenium, variables.get("base_url"), variables.get("wait"))
        credit_page.open()
        productpage = credit_page.select_credit()
        productpage.type_amount(100)
        productpage.select_purpose(pages.Purpose.purchase_financing)
        productpage.select_term(24)
        company_search = productpage.submit()
        company_search.search_for_company(company_name)
        registration_page = company_search.select_search_result(company_name)
        registration_page.F_NAME.fill("Test")
        registration_page.register()
        # Check that error message displays for required fields
        assert (registration_page.L_NAME.get_error_msg() == self.error_msg)
        assert (registration_page.EMAIL.get_error_msg() == self.error_msg)
        assert (registration_page.F_NAME.get_error_msg() is None)
        assert (registration_page.business_relation.get_error_msg() == self.error_msg)
        # Check phone field error message
        assert (registration_page.PHONE.get_error_msg() == self.error_msg)
        registration_page.EMAIL.fill(company_name)
        registration_page.register()
        # Check if wrong mail error message displays
        assert (registration_page.EMAIL.get_error_msg() == self.wrong_mail_err_msg)
        registration_page.business_relation.set_relation(pages.RelationType.business)
        registration_page.PHONE.fill(company_name)
        registration_page.register()
        # Check that business relation field error msg no longer displays
        assert (registration_page.business_relation.get_error_msg() is None)
        assert (registration_page.PHONE.get_error_msg() == self.wrong_phone_num_err_msg)
