from pickle import EMPTY_LIST
from time import sleep

from base.basepage import basePage


class cart(basePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def remove_product_from_basket_using_remove_this_item(self,removal_product_name_list):
        bef_product_name_list,bef_product_present_in_basket_dict=self.get_added_product_present_in_baseket()
        cart_item_row_elements=self.getAllElements(locatorValue="//table[contains(@class,'responsive cart')]/tbody/tr[@class='cart_item']",locator_type="xpath")
        for index,cart_item_column_ele in enumerate(cart_item_row_elements):
            for name in removal_product_name_list:
                if name==self.get_element_with_in_element(element=cart_item_column_ele,locator_value="//td[@class='product-name']/a",locator_type="xpath").text:
                    self.get_element_with_in_element(element=cart_item_column_ele,locator_value="//td[@class='product-remove']/a",locator_type="xpath").click()
                    self.check_for_ele_displayed_or_not_displayed(locatorValue="//div[@class='blockUI']",locatorType="xpath",status_flag=False)
                    product_name_list,cart_item_dict=self.get_added_product_present_in_baseket()
                    assert name not in product_name_list
                    return bef_product_name_list,bef_product_present_in_basket_dict
        return bef_product_name_list,bef_product_present_in_basket_dict

    def increase_quantity_product_from_basket(self,product_name_dict):
        update_product_qty={}
        cart_item_row_elements=self.getAllElements(locatorValue="//table[contains(@class,'bef_product_name_list,bef_product_present_in_basket_dictresponsive cart')]/tbody/tr[@class='cart_item']",locator_type="xpath")
        for index,cart_item_column_ele in enumerate(cart_item_row_elements):
            for name,count in product_name_dict.items():
                if name==self.get_element_with_in_element(element=cart_item_column_ele,locator_value="//td[@class='product-name']/a",locator_type="xpath").text:
                    element=self.get_element_with_in_element(element=cart_item_column_ele,locator_value="//td[@class='product-quantity']/div/input",locator_type="xpath")
                    qty=element.get_attribute("value")
                    element.clear()
                    element.send_keys(int(qty)+count)
                    update_product_qty[name]=int(qty)+count
        return update_product_qty

    def decrease_quantity_product_from_basket(self,product_name_dict):
        update_product_qty={}
        cart_item_row_elements=self.getAllElements(locatorValue="//table[contains(@class,'responsive cart')]/tbody/tr[@class='cart_item']",locator_type="xpath")
        for index,cart_item_column_ele in enumerate(cart_item_row_elements):
            for name,count in product_name_dict.items():
                if name==self.get_element_with_in_element(element=cart_item_column_ele,locator_value="//td[@class='product-name']/a",locator_type="xpath").text:
                    element=self.get_element_with_in_element(element=cart_item_column_ele,locator_value="//td[@class='product-quantity']/div/input",locator_type="xpath")
                    qty=element.get_attribute("value")
                    element.clear()
                    element.send_keys(int(qty)-count)
                    update_product_qty[name]=int(qty)-count
        return update_product_qty

    def get_colum_names_or_position(self,name=None):
        column_names = []
        cart_table_elements = self.getAllElements(locatorValue="//table[contains(@class,'responsive cart')]//tr",
                                                 locator_type="xpath")
        cart_table_columns = self.get_element_with_in_element(cart_table_elements[0], locator_type="xpath",
                                                              locator_value="/th", multiple_elements=True)
        for index, table_column in enumerate(cart_table_columns):
            if name == table_column.get_attribute("class") or name == table_column.text:
                return index+1
            else:
                column_names.append(table_column.text)
        return column_names



    def get_added_product_present_in_baseket(self):
        product_present_in_basket_dict={}
        product_name_list=[]
        cart_item_row_elements=self.getAllElements(locatorValue="//table[contains(@class,'responsive cart')]/tbody/tr[@class='cart_item']",locator_type="xpath")
        for index,cart_item_column_ele in enumerate(cart_item_row_elements):
            name=self.get_element_with_in_element(element=cart_item_column_ele,locator_value="//td[@class='product-name']/a",locator_type="xpath").text
            price = self.get_element_with_in_element(element=cart_item_column_ele, locator_value="//td[@class='product-price']/span",locator_type="xpath").text
            quantity= self.get_element_with_in_element(element=cart_item_column_ele,locator_value="//td[@class='product-quantity']/div/input",locator_type="xpath").get_attribute("value")
            total= self.get_element_with_in_element(element=cart_item_column_ele,locator_value="//td[@class='product-subtotal']/span",locator_type="xpath").text
            product_name_list.append(name)
            product_present_in_basket_dict[f"product{index+1}"]={"name":name,"selling_price":price,"quantity":quantity,"item_total":total}
        return product_name_list,product_present_in_basket_dict

    def click_on_update_cart_in_basket_page(self):
        self.click_element(locator_value="//table[contains(@class,'responsive cart')]/tbody/tr[last()]//td/input[@name='update_cart']",locator_type="xpath")

    def verify_updated_cart(self,before_update_cart_details_dict,updated_product_qty_details=None,remove=True):
        product_name_list,product_present_in_basket_dict=self.get_added_product_present_in_baseket()
        assert "Basket updated."==self.get_element(locator_value="//div[@class='woocommerce-message']",locator_type="xpath")



    def verify_cart_is_empty(self,remove=True):
        if remove:
            assert "Android Quick Start Guide removed. Undo?"==self.get_element(locator_value="//div[@class='woocommerce-message']",locator_type="xpath").text.strip()
        else:
            assert "Basket updated." == self.get_element(locator_value="//div[@class='woocommerce-message']",locator_type="xpath",wait_action="visibility")
        empty_cart_text=self.get_element(locator_value="//p[@class='cart-empty']",locator_type="xpath",wait_action="visibility").text
        product_name_list, product_present_in_basket_dict = self.get_added_product_present_in_baseket()
        assert "Your basket is currently empty." == empty_cart_text.strip()
        assert not product_name_list and not product_present_in_basket_dict


    def verify_added_product_is_showing_in_cart(self,product_name,product_list_details,added_quantity):
        product_name_list,product_present_in_basket_dict=self.get_added_product_present_in_baseket()
        assert product_name in product_name_list
        product_details_in_basket = {v['name']: v for v in product_present_in_basket_dict.values()}
        product_details = {v['name']: v for v in product_list_details.values()}

        assert product_details[product_name]['name']==product_details_in_basket[product_name]['name']
        if product_details[product_name]['sale']:
            assert product_details[product_name]['selling_price']==product_details_in_basket[product_name]['selling_price']
            assert f"₹{(float(product_details[product_name]['selling_price'].replace('₹', '')) * added_quantity):.2f}"==product_details_in_basket[product_name]['item_total']

        else:
            assert product_details[product_name]['original_price'] == product_details_in_basket[product_name]['selling_price']
            assert f"₹{(float(product_details[product_name]['original_price'].replace('₹', '')) * added_quantity):.2f}"==product_details_in_basket[product_name]['item_total']












