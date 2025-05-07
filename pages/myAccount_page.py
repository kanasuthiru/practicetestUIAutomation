import os
import random
import re
from faker import Faker
from base.basepage import basePage
from pages.home_page import home_page
from utils import common


class my_account(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.my_account_after_login_text=None


    def enter_login_user_name(self,user_name):
        self.send_text(text=user_name, locator_value="username", locator_type="id")
        assert self.get_attribute_value("value",locator_value="username",locator_type="id",wait_action="visibility")==user_name,f"{self.get_attribute_value('value')}......"



    def enter_login_password(self,password):
        self.send_text(text=password, locator_value="password", locator_type="id")
        assert self.get_attribute_value("value",locator_value="password",locator_type="id",wait_action="visibility") == password


    def click_on_login_button(self):
        username =self.get_attribute_value("value", locator_value="username", locator_type="id", wait_action="visibility")
        password =self.get_attribute_value("value", locator_value="password", locator_type="id", wait_action="visibility")
        self.click_element(locator_type="xpath",locator_value="//input[@type='submit' and @name='login']")
        return username,password


    def verify_my_account_page_components_before_login_or_register(self):
        pass


    def verify_my_account_page_components_after_login_or_register(self):
        pass

    def verify_user_logged_in_successfully(self,username):
        print(username)
        username=common.get_username_if_email(username)
        print(username)
        self.wait_for_element(locator_type="xpath", locator_value="//div[@class='woocommerce-MyAccount-content']",
                              wait_action="visibility")
        my_account_after_login_text = f"""Hello {username} (not {username}? Sign out)\nFrom your account dashboard you can view your recent orders, manage your shipping and billing addresses and edit your password and account details."""
        print(my_account_after_login_text)
        my_account_loggedin_user_text=self.get_element(locator_type="xpath",locator_value="//div[@class='woocommerce-MyAccount-content']",wait_action="visibility").text
        print(my_account_after_login_text)
        assert my_account_loggedin_user_text.strip()==my_account_after_login_text.strip(),f"""text mismatch --- stored_variable value {my_account_after_login_text} --- ui text {my_account_loggedin_user_text}"""


    def verify_user_is_on_login_screen(self):
        self.wait_for_element(locator_type="xpath", locator_value="//div[@class='woocommerce-MyAccount-content']",
                              wait_action="invisibility")
        self.get_element(locator_type="xpath", locator_value="//div[@class='woocommerce']",
                         wait_action="visibility").is_displayed()


    def verify_error_message(self,context,reason,component="login"):
        warning_message_flag=False
        if component!="login"and reason == "invalid_email_address":
            reason,warning_message_flag=common.get_reason_and_ui_input_warningmessage_or_warning_message_flag(context)
        if warning_message_flag:
            error_message_from_ui=self.get_attribute_value("validationMessage", locator_value="reg_email", locator_type="id",
                                    wait_action="visibility")
        else:
            error_message_from_ui = self.get_element(locator_type="xpath",
                                                     locator_value="//ul[@class='woocommerce-error']/li").text
        print("...................................................................")
        print(reason)
        print(component)
        print(error_message_from_ui)
        print("sdfghjkl")
        print(".......................................................................")

        error_message_text=common.get_login_failure_reason(context,reason,component)
        assert error_message_text==error_message_from_ui,f" text mismatch ---error_message_text- {error_message_text}--error_message_from_ui--{error_message_from_ui}"




    def verify_password_field_type_value(self,field="login"):
        assert self.get_attribute_value("type",locator_value="password",locator_type="id",wait_action="visibility") =="password"

    def click_on_sign_out_link(self):
        self.click_element(locator_type="xpath",locator_value="//a[text()='Sign out']")

#Register component
    def enter_register_email_address(self,user_name):
        if "random" in user_name:
            fake = Faker()
            user_name = f"{fake.first_name()}{random.randint(1, 9999)}@yahoo.com"
        self.send_text(text=user_name, locator_value="reg_email", locator_type="id")
        assert self.get_attribute_value("value",locator_value="reg_email",locator_type="id",wait_action="visibility")==user_name,f"{self.get_attribute_value('value')}......"



    def enter_register_password(self,password):
        if "random" in password:
            password=common.generate_random_password_for_register()
        self.send_text(text=password, locator_value="reg_password", locator_type="id")
        assert self.get_attribute_value("value",locator_value="reg_password",locator_type="id",wait_action="visibility") == password
        self.click_element(locator_type="xpath", locator_value="//div[@class='woocommerce']")

    def check_for_password_strength(self):
        password_strength=self.get_element(locator_type="xpath",locator_value="//div[contains(@class,'woocommerce-password-strength')]").text
        class_attribute_value = self.get_attribute_value("class", locator_value="//div[contains(@class,'woocommerce-password-strength')]", locator_type="xpath",
                                                    wait_action="visibility")



    def click_on_register_button(self):
        email_address =self.get_attribute_value("value", locator_value="reg_email", locator_type="id", wait_action="visibility")
        password =self.get_attribute_value("value", locator_value="reg_password", locator_type="id", wait_action="visibility")
        self.click_element(locator_type="xpath",locator_value="//input[@type='submit' and @name='register']")
        return email_address,password

    def click_on_address_link_from_my_account_menu(self):
        current_page_url = self.driver.current_url
        self.click_element(locator_value="//a[text()='Addresses']",locator_type="xpath")
        if current_page_url != f"""{os.getenv("web_page_url")}my-account/edit-address/""":
            self.wait_until_url_change(current_page_url)
            assert self.driver.current_url == f"""{os.getenv("web_page_url")}my-account/edit-address/"""

    def register_new_user(self,user_name,password):
          home_page(self.driver).click_on_my_account_menu()
          self.enter_register_email_address(user_name=user_name)
          self.enter_register_password(password)
          self.check_for_password_strength()
          email_address,password=self.click_on_register_button()
          self.verify_user_logged_in_successfully(email_address)
          return email_address,password

    def login_to_web_page(self,user_name,password):
        home_page(self.driver).click_on_my_account_menu()
        self.enter_login_user_name(user_name=user_name)
        self.enter_login_password(password=password)
        self.click_on_login_button()
        self.verify_user_logged_in_successfully(user_name)
        return user_name,password






