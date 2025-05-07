import os
import time

from pkg_resources import require
from selenium.webdriver.support.expected_conditions import element_attribute_to_include

from base.basepage import basePage


class shop(basePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def click_on_add_basket(self,product_name):
        add_basket_for_product_path=f"//ul[@class='products masonry-done']/li//h3[text()='{product_name}']/../..//a[text()='Add to basket']"
        class_attribute_value_before=self.get_attribute_value(attribute_name="class",locator_value=f"//ul[@class='products masonry-done']/li//h3[text()='{product_name}']/../..//a[text()='Add to basket']",locator_type="xpath")
        self.click_element(locator_value=f"//ul[@class='products masonry-done']/li//h3[text()='{product_name}']/../..//a[text()='Add to basket']",locator_type="xpath")
        self.wait_until_attribute_value_changes(before_attribute_value=class_attribute_value_before,attribute_name="class",locator_value=add_basket_for_product_path,locator_type="xpath",required_text="button product_type_simple add_to_cart_button ajax_add_to_cart added")
        class_attribute_value_after=self.get_attribute_value(attribute_name="class",locator_value=f"//ul[@class='products masonry-done']/li//h3[text()='{product_name}']/../..//a[text()='Add to basket']",locator_type="xpath")
        assert "add_to_cart added" in class_attribute_value_after
        return 1

    def get_all_products_name_and_its_price_from_shop_page(self):
        product_dict={}
        product_path = "//ul[@class='products masonry-done']/li"
        product_elements=self.getAllElements(locatorValue=product_path,locator_type="xpath")
        for index in range(0,len(product_elements)):
            product_on_sale=False
            product_name=self.get_element(locator_value=f"//ul[@class='products masonry-done']/li[{str(index+1)}]//h3",locator_type="xpath").text
            product_on_sale_ele=self.getAllElements(locatorValue=f"//ul[@class='products masonry-done']/li[{str(index+1)}]//span[@class='onsale']",locator_type="xpath")
            if len(product_on_sale_ele)!=0:
                product_on_sale=True
                original_product_price=self.get_element(locator_value=f"//ul[@class='products masonry-done']/li[{str(index+1)}]//span[@class='price']/del/span",locator_type="xpath").text
                product_selling_price = self.get_element(locator_value=f"//ul[@class='products masonry-done']/li[1]//span[@class='price']/ins/span",locator_type="xpath").text
            else:
                product_selling_price=original_product_price=self.get_element(locator_value=f"//ul[@class='products masonry-done']/li[{str(index+1)}]//span[@class='price']",locator_type="xpath").text
            product_dict[f"product{index+1}"]={"name":product_name,"sale":product_on_sale,"selling_price":product_selling_price,"original_price":original_product_price}
        return product_dict

    def check_for_view_basket_component_in_shop_page(self,product_name):
        class_attribute_value = self.get_attribute_value(attribute_name="class",
                                                               locator_value=f"//ul[@class='products masonry-done']/li//h3[text()='{product_name}']/../..//a[text()='Add to basket']",
                                                               locator_type="xpath")

        if "add_to_cart added" in class_attribute_value:
            self.check_for_ele_displayed_or_not_displayed(locatorValue=f"//ul[@class='products masonry-done']/li//h3[text()='{product_name}']/../..//a[text()='View Basket']",locatorType="xpath")
        else:
            self.check_for_ele_displayed_or_not_displayed(locatorValue=f"//ul[@class='products masonry-done']/li//h3[text()='{product_name}']/../..//a[text()='View Basket'])",locatorType="xpath",status_flag=False)


    def click_on_view_basket_in_shop_page(self,product_name):
        current_page_url = self.driver.current_url
        self.click_element(locator_value=f"//ul[@class='products masonry-done']/li//h3[text()='{product_name}']/../..//a[text()='View Basket']",locator_type="xpath")
        if current_page_url != f"""{os.getenv("web_page_url")}basket/""":
            self.wait_until_url_change(current_page_url)
            assert self.driver.current_url == f"""{os.getenv("web_page_url")}basket/"""

