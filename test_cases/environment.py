from behave.model import Scenario
from behave.model_core import Status
from selenium import webdriver

from base.basepage import basePage
from pages.home_page import home_page
from pages.myAccount_page import my_account


def before_all(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


def before_scenario(context,scenario):
    print("dfghjkl")
    print(scenario.name)
    print(scenario.status,Status.passed)
    print("hjklhghioiuy")
    print("......................................")
    print("sdfghjkl")
    context.bp=basePage(context.driver)
    context.hp=home_page(context.driver)
    context.myAcc=my_account(context.driver)
    context.username=None
    context.email_address=None

def after_scenario(context, scenario):
    scenario_name=scenario.name.split(" -- ")[0]
    if scenario_name in ["validate user is able to login with Valid Credentials","validate user is able to Register an Account"]:
        if context.bp.get_element(locator_type="xpath", locator_value="//div[@class='woocommerce-MyAccount-content']",
                              wait_action="visibility").is_displayed():
            context.myAcc.click_on_sign_out_link()
            context.myAcc.verify_user_is_on_login_screen()
            print("asdfghj")
            print("dfghjkl")

def after_all(context):
    context.driver.quit()