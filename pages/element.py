from .WebView import WebView

class Element(WebView):

    def __init__(self, page, value):
        super(Element, self).__init__(page.driver, page.timeout)
        self.page = page
        self.value = value
