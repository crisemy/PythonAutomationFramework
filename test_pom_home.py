import os
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config_options import ConfigOptions
from pages.python_home_page import PythonHomePage


def _build_driver(headless: bool):
    """Selenium 4: Selenium Manager auto-resolves chromedriver, no $PATH setup."""
    options = ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    # Service() with no args => Selenium Manager picks the right driver.
    return webdriver.Chrome(service=ChromeService(), options=options)


@pytest.fixture()
def environment_setup(headless):
    use_headless = headless or os.getenv("HEADLESS", "").lower() in ("1", "true", "yes")
    browser = _build_driver(use_headless)

    # Keep original flow: page object + go() + maximize (skip maximize in headless)
    python_home_page = PythonHomePage(driver=browser)
    python_home_page.go()
    if not use_headless:
        try:
            browser.maximize_window()
        except Exception:
            browser.set_window_size(1920, 1080)

    yield python_home_page

    # Screenshot to repo-relative path (was hardcoded macOS path in 2023)
    screenshot_dir = Path(__file__).resolve().parent / "screenshot"
    screenshot_dir.mkdir(parents=True, exist_ok=True)
    try:
        browser.get_screenshot_as_file(str(screenshot_dir / "FinalScreen.png"))
    finally:
        browser.quit()


def test_search_option(environment_setup):
    python_home_page = environment_setup
    driver = python_home_page.driver

    # Searching by Jobs
    python_home_page.search_input.input_text("Jobs")
    python_home_page.go_button.click()
    # 2026 fix: wait for navigation — old code read the first homepage h2 ("Get Started")
    WebDriverWait(driver, ConfigOptions.timeout).until(EC.url_contains("/search"))

    # #03: Searching: Search by Empty Values
    # Assert the Title of the Page
    assert python_home_page.assert_title.text == "Search Python.org", "Unexpected Error"

    # Click the Logo
    try:
        python_home_page.go_logo_image.click()
        print("Matching the LOGO")
    except Exception as e:
        print("WRONG Matching > LOGO", format(e))
    WebDriverWait(driver, ConfigOptions.timeout).until(EC.url_matches(r"https?://(www\.)?python\.org/?$"))

    # Search by Empty Values
    python_home_page.go_button.click()
    WebDriverWait(driver, ConfigOptions.timeout).until(EC.url_contains("/search"))

    # Assert the Title of the Page - Otherwise it will throw an error
    assert python_home_page.assert_title.text == "Search Python.org", "Unexpected Error"


def test_config_loads_base_url():
    assert ConfigOptions.base_url == "https://python.org"
