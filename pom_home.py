from selenium import webdriver
from Pages.python_home_page import PythonHomePage

# Test Set-up
browser = webdriver.Chrome()

python_home_page = PythonHomePage(driver=browser)
python_home_page.go()

python_home_page.search_input.input_text("Jobs")
python_home_page.go_button.click()

# Closing the Browser
browser.quit()