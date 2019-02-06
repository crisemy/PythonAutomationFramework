from selenium import webdriver
from Pages.python_home_page import PythonHomePage

# Test Set-up
browser = webdriver.Chrome()

python_home_page = PythonHomePage(driver=browser)
python_home_page.go()

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

# Assert the Title of the Page
assert python_home_page.assert_title.text == 'Search Python.org' , 'Unexpected Error'

# Closing the Browser
browser.quit()