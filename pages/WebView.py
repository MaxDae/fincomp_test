from warnings import warn
from ..interfaces.driver import IDriver
class WebView(object):
    def __init__(self, driver, timeout):
        self.driver = driver
        self.driver_adapter = IDriver(driver)
        self.timeout = timeout
        self.wait = self.driver_adapter.wait_factory(self.timeout)

    @property
    def selenium(self):
        warn("use driver instead", DeprecationWarning, stacklevel=2)
        return self.driver

    def find_element(self, strategy, locator):
        return self.driver_adapter.find_element(strategy, locator)

    def find_elements(self, strategy, locator):
        """Finds elements on the page.
        :param strategy: Location strategy to use. See :py:class:`~selenium.webdriver.common.by.By`
        :param locator: Location of target elements.
        :type strategy: str
        :type locator: str
        :return: List of :py:class:`~selenium.webdriver.remote.webelement.WebElement`
        :rtype: list
        """
        return self.driver_adapter.find_elements(strategy, locator)

    def is_element_present(self, strategy, locator):
        """Checks whether an element is present.
        :param strategy: Location strategy to use. See :py:class:`~selenium.webdriver.common.by.By`
        :param locator: Location of target element.
        :type strategy: str
        :type locator: str
        :return: ``True`` if element is present, else ``False``.
        :rtype: bool
        """
        return self.driver_adapter.is_element_present(strategy, locator)

    def is_element_displayed(self, strategy, locator):
        """Checks whether an element is displayed.
        :param strategy: Location strategy to use. See :py:class:`~selenium.webdriver.common.by.By`
        :param locator: Location of target element.
        :type strategy: str
        :type locator: str
        :return: ``True`` if element is displayed, else ``False``.
        :rtype: bool
        """
        return self.driver_adapter.is_element_displayed(strategy, locator)

    def click(self, *strategy_locator):
        """

        :param strategy_locator:
        :return:
        """
        return self.driver_adapter.click(*strategy_locator)

    def type_text(self, text, *strategy_locator):
        """

        :param text: str
        :param strategy_locator:
        :return: type text to webelement
        """
        return self.driver_adapter.type_text(text, *strategy_locator)

    def clear_text_field(self, *strategy_locator):
        """
        
        :param strategy_locator: 
        :return: clear input field
        """
        return self.driver_adapter.find_element(*strategy_locator).clear()
