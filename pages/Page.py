import collections
import sys
from selenium.webdriver.common.by import By
from .WebView import WebView

if sys.version_info >= (3,):
    import urllib.parse as urlparse
    from urllib.parse import urlencode
else:
    import urlparse
    from urllib import urlencode


def iterable(arg):
    if isinstance(arg, collections.Iterable) and not isinstance(arg, str):
        return arg
    return [arg]


class Page(WebView):
    """A page object.
    Used as a base class for your project's page objects.
    :param driver: A driver.
    :param base_url: (optional) Base URL.
    :param timeout: (optional) Timeout used for explicit waits. Defaults to ``10``.
    :param url_kwargs: (optional) Keyword arguments used when generating the :py:attr:`seed_url`.
    :type driver: :py:class:`~selenium.webdriver.remote.webdriver.WebDriver`
    :type base_url: str
    :type timeout: int
    Usage (Selenium)::
      from page import Page
      from selenium.webdriver import Firefox
      class PageNew(Page):
          URL_TEMPLATE = 'https://www.google.com/{locale}'
      driver = Firefox()
      page = Page(driver)
      page.open()
    """

    URL_TEMPLATE = None
    """Template string representing a URL that can be used to open the page.
    Examples::
        URL_TEMPLATE = 'https://www.google.com/'  # absolute URL
        URL_TEMPLATE = '/search'  # relative to base URL
        URL_TEMPLATE = '/search?q={term}'  # keyword argument expansion
    """

    def __init__(self, driver, base_url=None, timeout=10, **url_kwargs):
        super(Page, self).__init__(driver, timeout)
        self.base_url = base_url
        self.url_kwargs = url_kwargs

    @property
    def seed_url(self):
        """A URL that can be used to open the page.
        The URL is formatted from :py:attr:`URL_TEMPLATE`, which is then
        appended to :py:attr:`base_url` unless the template results in an
        absolute URL.
        :return: URL that can be used to open the page.
        :rtype: str
        """
        url = self.base_url
        if self.URL_TEMPLATE is not None:
            url = urlparse.urljoin(
                self.base_url, self.URL_TEMPLATE.format(**self.url_kwargs)
            )

        if not url:
            return None

        url_parts = list(urlparse.urlparse(url))
        query = urlparse.parse_qsl(url_parts[4])

        for k, v in self.url_kwargs.items():
            if v is None:
                continue
            if "{{{}}}".format(k) not in str(self.URL_TEMPLATE):
                for i in iterable(v):
                    query.append((k, i))

        url_parts[4] = urlencode(query)
        return urlparse.urlunparse(url_parts)

    def open(self):
        """Open the page.
        Navigates to :py:attr:`seed_url` and calls :py:func:`wait_for_page_to_load`.
        :return: The current page object.
        :rtype: :py:class:`Page`
        :raises: UsageError
        """
        if self.seed_url:
            self.driver_adapter.open(self.seed_url)
            self.wait_for_page_to_load()
            return self
        raise exception("Set a base URL or URL_TEMPLATE to open this page.")

    def wait_for_page_to_load(self):
        """Wait for the page to load."""
        self.wait.until(lambda _: self.loaded)

        return self

    @property
    def loaded(self):
        """Loaded state of the page.
        By default the driver will try to wait for any page loads to be
        complete, however it's not uncommon for it to return early. To address
        this you can override :py:attr:`loaded` to return ``True`` when the
        page has finished loading.
        :return: ``True`` if page is loaded, else ``False``.
        :rtype: bool
        Usage ::
          from selenium.webdriver.common.by import By
          class NewPage(Page):
              @property
              def loaded(self):
                  body = self.find_element(By.TAG_NAME, 'body')
                  return 'loaded' in body.get_attribute('class')
        """
        return True










