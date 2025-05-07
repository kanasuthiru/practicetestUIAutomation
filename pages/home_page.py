import os

from base.basepage import basePage


class home_page(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_my_account_menu(self):
        current_page_url=self.driver.current_url
        self.click_element(locator_type="xpath",locator_value="//header[@id='header']//li/a[text()='My Account']",timeout=15)
        if current_page_url!=f"""{os.getenv("web_page_url")}my-account/""":
            self.wait_until_url_change(current_page_url)
            assert self.driver.current_url==f"""{os.getenv("web_page_url")}my-account/"""


    def verify_user_is_on_home_screen(self):
        home_page_shop_selenium_books_img=self.get_element(locator_type="xpath",locator_value="//img[@alt='Shop Selenium Books']",wait_action="visibility")
        assert home_page_shop_selenium_books_img.is_displayed()==True

    def click_on_my_shop_menu(self):
        current_page_url=self.driver.current_url
        self.click_element(locator_type="xpath",locator_value="//header[@id='header']//li/a[text()='Shop']",timeout=15)
        if current_page_url!=f"""{os.getenv("web_page_url")}shop/""":
            self.wait_until_url_change(current_page_url)
            assert self.driver.current_url==f"""{os.getenv("web_page_url")}shop/"""


    def click_on_cart_icon_menu(self):
        cart_item_count_text,cart_item_price_text=self.get_cart_item_count_and_amount_from_menu()
        current_page_url = self.driver.current_url
        self.click_element(locator_type="xpath",locator_value="//header[@id='header']//li/a[@title='View your shopping cart']",timeout=15)
        if cart_item_price_text == "₹0.00" and cart_item_count_text == "0 items":
            if current_page_url != f"""{os.getenv("web_page_url")}shop/""":
                self.wait_until_url_change(current_page_url)
                assert self.driver.current_url == f"""{os.getenv("web_page_url")}shop/"""
        else:
            if current_page_url!=f"""{os.getenv("web_page_url")}basket/""":
                self.wait_until_url_change(current_page_url)
                assert self.driver.current_url==f"""{os.getenv("web_page_url")}basket/"""


    def get_cart_item_count_and_amount_from_menu(self):
        cart_item_count_text=self.get_element(locator_type="xpath",locator_value="//header[@id='header']//li/a[@title='View your shopping cart']/span[@class='cartcontents']").text
        cart_item_price_text=self.get_element(locator_type="xpath",locator_value="//header[@id='header']//li/a[@title='View your shopping cart']/span[@class='amount']").text
        return cart_item_count_text,cart_item_price_text
