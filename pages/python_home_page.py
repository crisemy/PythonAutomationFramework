from selenium.webdriver.common.by import By

from PythonProjects.config_options import ConfigOptions

from .base_element import BaseElement
from .base_page import BasePage


class PythonHomePage(BasePage, ConfigOptions):
    url = ConfigOptions.base_url

    @property
    def search_input(self):
        locator = (By.CSS_SELECTOR, 'input#id-search-field') # I'm sending the locator to search for AND the value
        return BaseElement(self.driver, by=locator[0], value=locator[1]) # Returns the by, driver and value

    @property
    def go_button(self):
        locator = (By.ID, 'submit') # I'm sending the locator to search for AND the value
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    # #03: Search: Searching by Empty Values

    # Clicking on the Logo to start searching right from the Home Page
    @property
    def go_logo_image(self):
        locator = (By.CLASS_NAME, "python-logo")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    # Compare whether the Title exists or not
    @property
    def assert_title(self):
        # Searches by Title - H2 in this case

        locator = (By.CSS_SELECTOR, 'h2')
        return BaseElement(self.driver, by=locator[0], value=locator[1])
