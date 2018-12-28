from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage

class PythonHomePage(BasePage):
    url = 'https://www.python.org/'

    @property
    def search_input(self):
        locator = (By.CSS_SELECTOR, 'input#id-search-field') # I'm sending the locator to search for AND the value
        return BaseElement(self.driver, by=locator[0], value=locator[1]) # Returns the by, driver and value

    @property
    def go_button(self):
        locator = (By.ID, 'submit') # I'm sending the locator to search for AND the value
        return BaseElement(self.driver, by=locator[0], value=locator[1]) # Returns the by, driver and value