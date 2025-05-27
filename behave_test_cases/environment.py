from behave.model import Scenario
from behave.model_core import Status
from selenium import webdriver
import allure
from behave.model import Status
from selenium.webdriver.chrome.options import Options

from base.basepage import basePage
from conftest import shop_page
from pages.basket_page import cart
from pages.billing_address_page import billing_address
from pages.home_page import home_page
from pages.myAccount_page import my_account
from pages.shipping_address_page import shipping_address
from pages.shop_page import shop
import tempfile

def before_all(context):
    options = Options()
    # Create a unique temporary directory for Chrome user data
    options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")
    context.driver = webdriver.Chrome(options=options)
    context.driver.maximize_window()


def before_scenario(context,scenario):
    context.bp=basePage(context.driver)
    context.hp=home_page(context.driver)
    context.myAcc=my_account(context.driver)
    context.ship=shipping_address(context.driver)
    context.bill=billing_address(context.driver)
    context.shop=shop(context.driver)
    context.cart=cart(context.driver)
    context.username=None
    context.email_address=None

def after_scenario(context, scenario):
    if scenario.status == Status.failed:
        screenshot = context.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
    scenario_name=scenario.name.split(" -- ")[0]
    if scenario_name in ["validate user is able to login with Valid Credentials","validate user is able to Register an Account"]:
        if context.bp.get_element(locator_type="xpath", locator_value="//div[@class='woocommerce-MyAccount-content']",
                              wait_action="visibility").is_displayed():
            context.myAcc.click_on_sign_out_link()
            context.myAcc.verify_user_is_on_login_screen()




def after_all(context):
    context.driver.quit()