from selenium import webdriver
from PythonProjects.pages.python_home_page import PythonHomePage
from PythonProjects.config_options import ConfigOptions

import pytest

@pytest.fixture()

def environment_setup():

    # global Variable to use in another functions
    global python_home_page

    # Test Set-up
    browser = webdriver.Chrome()

    python_home_page = PythonHomePage(driver=browser)
    python_home_page.go()


    '''
    browser = ConfigOptions.web_d
    print(browser)
    config_options = ConfigOptions(driver=browser)
    config_options.go()
    '''

    # Maximize browser
    browser.maximize_window()

    # The Yield command establishes that whatever you write it'll be executed AFTER your Test.
    # In this case, after the test_search_option Function.
    yield

    # 09: Taking screenshots and Saving them in a specific folder
    browser.get_screenshot_as_file("/Users/cristiannadj/Desktop/crisArch/pythonCourse/IntelliJIDE/ElegantBrowserAutomation/pythonSite/PythonProjects/screenshot/FinalScreen.png")
    # Closing the Browser
    browser.quit()

def test_search_option(environment_setup):
    # Searching by Jobs
    python_home_page.search_input.input_text("Jobs")
    python_home_page.go_button.click()

    # #03: Searching: Search by Empty Values
    # Assert the Title of the Page
    assert python_home_page.assert_title.text == 'Search Python.org' , 'Unexpected Error'

    # Click the Logo
    try:
        python_home_page.go_logo_image.click()
        print('Matching the LOGO')
    except Exception as e:
        print('WRONG Matching > LOGO', format(e))

    # Search by Empty Values
    python_home_page.go_button.click()

    # Assert the Title of the Page - Otherwise it will throw an error
    assert python_home_page.assert_title.text == 'Search Python.org', 'Unexpected Error'