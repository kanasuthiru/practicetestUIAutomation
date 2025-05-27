import os

from dotenv import load_dotenv

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages import *
from pages.basket_page import cart
from pages.address_page import Address_page
from pages.billing_address_page import billing_address
from pages.home_page import home_page
from pages.myAccount_page import my_account
from pages.shipping_address_page import shipping_address
from pages.shop_page import shop
from selenium.webdriver.chrome.options import Options
load_dotenv()
import os


@pytest.fixture(scope="session")
def driver():
    print("\n[Setup] Launching browser for the entire test suite")  # Optional: run in background

    # extension_path = '/home/thriveni/Desktop/my-extension.crx'

    # Get the base directory of your project (assuming this file is somewhere inside)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Adjust the number of os.path.dirname() calls to go up to your project root

    extension_path = os.path.join(base_dir, 'my-extension.crx')
    # Set up Chrome options to load the extension
    chrome_options = Options()
    chrome_options.add_extension(extension_path)
    chrome_options.add_experimental_option(
        "prefs",
        {"extensions.onboarding.enabled": False,"autofill.profile_enabled": False}
    )
    # Initialize WebDriver with the options
    driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()
    initial_windows = driver.window_handles
    WebDriverWait(driver, 10).until(
        lambda d: len(d.window_handles) > len(initial_windows)
    )

    # Identify the new tab
    new_windows = [w for w in driver.window_handles if w not in initial_windows]
    if new_windows:
        driver.switch_to.window(new_windows[0])
        driver.close()  # close the extension’s tab

    # Switch back to your main window
    driver.switch_to.window(initial_windows[0])

    #
    yield driver
    print("\n[Teardown] Quitting browser after test suite")
    driver.quit()

@pytest.fixture
def open_url(driver):
    url = os.getenv("web_page_url")  # Fetch URL from the environment variable
    if not url:
        raise ValueError("The environment variable 'web_page_url' is not set.")
    driver.get(url)
    return driver

@pytest.fixture(scope="function")
def billing_address_page(driver):
    page = billing_address(driver)
    return page

@pytest.fixture(scope="function")
def shipping_address_page(driver):
    page = shipping_address(driver)
    return page

@pytest.fixture(scope="function")
def my_account_page(driver):
    page = my_account(driver)
    return  page


@pytest.fixture(scope="function")
def address_page(driver):
    page = Address_page(driver)
    return page

# Fixture for LoginPage
@pytest.fixture(scope="function")
def shop_page(driver):
    page = shop(driver)
    return page
@pytest.fixture(scope="function")
def basket_page(driver):
    page = cart(driver)
    return page

@pytest.fixture(scope="function")
def homepage(driver):
    page = home_page(driver)
    return page