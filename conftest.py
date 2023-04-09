import allure

import pytest

from selene import browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from models.working_with_files import resources_dir


@allure.step('Open registration form')
@pytest.fixture(scope="session")
def open_browser():
    browser.config.window_height = 1800
    browser.config.window_width = 1800
    browser.config.hold_browser_open = True

    options = webdriver.ChromeOptions()

    prefs = {
        "download.default_directory": resources_dir,
        "download.prompt_for_download": False
    }

    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    browser.config.driver = driver

    browser.open("https://www.dssl.ru/products/")

    yield

    browser.quit()


