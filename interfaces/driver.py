from zope.interface import Interface

class IDriver(Interface):
    """ Driver interface """

    def wait_factory(timeout):
        """Returns a WebDriverWait like property for a given timeout.
        :param timeout: Timeout used by WebDriverWait like calls
        :type timeout: int
        """

    def open(url):
        """Open the page.
        Navigates to :py:attr:`url`
        """

    def find_element(strategy, locator, root=None):
        """Finds an element on the page.
        :param strategy: Location strategy to use (type depends on the driver implementation)
        :param locator: Location of target element.
        :param root: (optional) root node.
        :type strategy: str
        :type locator: str
        :type root: web element object or None.
        :return: web element object
        :rtype: it depends on the driver implementation
        """

    def find_elements(strategy, locator, root=None):
        """Finds elements on the page.
        :param strategy: Location strategy to use (type depends on the driver implementation)
        :param locator: Location of target elements.
        :param root: (optional) root node.
        :type strategy: str
        :type locator: str
        :type root: web element object or None.
        :return: iterable of web element objects
        :rtype: iterable (if depends on the driver implementation)
        """

    def is_element_present(strategy, locator, root=None):
        """Checks whether an element is present.
        :param strategy: Location strategy to use (type depends on the driver implementation)
        :param locator: Location of target element.
        :param root: (optional) root node.
        :type strategy: str
        :type locator: str
        :type root: web element object or None.
        :return: ``True`` if element is present, else ``False``.
        :rtype: bool
        """

    def is_element_displayed(strategy, locator, root=None):
        """Checks whether an element is displayed.
        :param strategy: Location strategy to use (type depends on the driver implementation)
        :param locator: Location of target element.
        :param root: (optional) root node.
        :type strategy: str
        :type locator: str
        :type root: web element object or None.
        :return: ``True`` if element is displayed, else ``False``.
        :rtype: bool
        """
    def click(*strategy_locator_tuple):
        """Click to element.
        :param strategy: Location strategy to use (type depends on the driver implementation)
        :param locator: Location of target element.
        :type strategy: str
        :type locator: str
        :return: ``True`` if element is displayed, else ``False``.
        :rtype: depends on driver implementations
        """

    def type_text(text, *strategy_locator_tuple):
        """

        :param strategy_locator_tuple: (By._, locator)
        :return: typed text
        """
    def clear_text_field(*strategy_locator_tuple):
        """

        :param strategy_locator_tuple:  (By._, locator)
        :return: cleared field from text
        """

