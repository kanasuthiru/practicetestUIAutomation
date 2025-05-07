import os

from base.basepage import basePage


class Address_page(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def verify_address_page(self,b_address_exist=False,s_address_exist=False):
        assert self.get_element(locator_type="xpath",locator_value="//div[@class='woocommerce-MyAccount-content']/p").text.strip()=="The following addresses will be used on the checkout page by default."
        address_element=self.get_element(locator_type="xpath",locator_value="//div[@class='woocommerce-MyAccount-content']/div[contains(@class,'u-columns woocommerce-Addresses col2-set addresses')]")
        assert address_element.is_displayed()==True
        self.get_element(locator_value="//h3[text()='Billing Address']/..",locator_type="xpath").is_displayed()
        self.get_element(locator_value="//h3[text()='Shipping Address']/..",locator_type="xpath").is_displayed()
        if b_address_exist==False:
            assert self.get_element(locator_value="//h3[text()='Billing Address']/../../address",locator_type="xpath").text.strip()=="You have not set up this type of address yet."
        else:
            print("no code")
        if s_address_exist==False:
            assert self.get_element(locator_value="//h3[text()='Shipping Address']/../../address",locator_type="xpath").text.strip()=="You have not set up this type of address yet."
        else:
            print("no code")

    def click_on_billing_address_edit_link(self):
        current_page_url = self.driver.current_url
        self.click_element(locator_value="//h3[text()='Billing Address']/../a",locator_type="xpath")
        self.wait_until_url_change(current_page_url)
        assert self.driver.current_url == f"""{os.getenv("web_page_url")}my-account/edit-address/billing/"""

    def click_on_shipping_address_edit_link(self):
        current_page_url = self.driver.current_url
        self.click_element(locator_value="//h3[text()='Shipping Address']/../a",locator_type="xpath")
        self.wait_until_url_change(current_page_url)
        assert self.driver.current_url == f"""{os.getenv("web_page_url")}my-account/edit-address/shipping/"""


    def verify_saved_billing_Address(self,address_dict):
        address=self.get_element(locator_value="//h3[text()='Billing Address']/../../address", locator_type="xpath").text


    def verify_saved_shipping_address(self,address_dict):
        address=self.get_element(locator_value="//h3[text()='Shipping Address']/../../address",locator_type="xpath").text