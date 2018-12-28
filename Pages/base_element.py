from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseElement(object):
    def __init__(self, driver, value, by):
        self.driver = driver
        self.value = value
        self.by = by

        self.locator = (self.by, self.value)
        self.web_element = None

        self.find()

    # Explicit wait for finding a Locator
    def find(self):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator=self.locator))

        self.web_element = element
        return None

    # We send the keys we tyte to the web_element
    def input_text(self, txt):
        self.web_element.send_keys(txt)
        return None

    # Explicit wait for an element to be clickable
    def click(self):
        element = WebDriverWait(self.driver, 5). until(EC.element_to_be_clickable(locator=self.locator))
        element.click()
        return None

    # Simply returning a text. An Explicit won't be needed
    @property
    def text(self):
        text = self.web_element.text
        return text
