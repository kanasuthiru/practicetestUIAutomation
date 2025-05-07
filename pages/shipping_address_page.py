import os
import random

from base.basepage import basePage
from pages.myAccount_page import my_account
from utils.common import convert_dictionary_values_to_string
from faker import Faker

class shipping_address(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.faker=Faker()
        self.driver = driver
        self.before_edit_shipping_address={}
        self.after_edit_shipping_address={}

    def verify_components_on_shipping_address_page(self):
        self.is_shipping_first_name_field_visible()
        self.is_shipping_last_name_field_visible()
        self.is_shipping_company_field_visible()
        self._is_shipping_country_field_visible()
        self._is_shipping_address_1_field_visible()
        self._is_shipping_address_2_field_visible()
        self._is_shipping_city_field_visible()
        self._is_shipping_state_field_visible()
        self._is_shipping_postcode_field_visible()
        self._is_shipping_save_address_button_visible()
        return self.before_edit_shipping_address
        

    def click_on_save_address_button(self):
        current_page_url=self.driver.current_url
        self.click_element(locator_value="//input[@name='save_address' and @class='button']", locator_type="xpath")
        

    def verify_saved_address(self, current_page_url, address_dict):
        self.check_for_ele_displayed_or_not_displayed(locatorValue="//input[@name='save_address' and @class='button']",locatorType="xpath", status_flag=False)
        self.wait_until_url_change(current_page_url)
        assert self.driver.current_url == f"""{os.getenv("web_page_url")}my-account/"""
        assert "Address changed successfully." == self.get_element(locator_type="xpath",locator_value="//div[@class='woocommerce-message']",wait_action="visibility").text.strip()
        my_account(self.driver).click_on_address_link_from_my_account_menu()
        saved_address = self.get_element(locator_value="//h3[text()='Shipping Address']/../../address",locator_type="xpath").text
        print(saved_address == convert_dictionary_values_to_string(address_dict))
        print(convert_dictionary_values_to_string(address_dict))
        assert saved_address == convert_dictionary_values_to_string(address_dict)
     

    def enter_shipping_first_name(self,f_name=None):
        if f_name is not None:
            if f_name=="random":
                f_name=self.faker.first_name()
            self.send_text(text=f_name, locator_value="shipping_first_name", locator_type="id")
            assert self.get_attribute_value(attribute_name="value",locator_value="shipping_first_name",locator_type="id").strip()==f_name
        self.after_edit_shipping_address['f_name']=f_name


    def  enter_shipping_last_name(self,l_name=None):
        if l_name is not None:
            if l_name=="random":
                l_name=self.faker.last_name()
            self.send_text(text=l_name, locator_value="shipping_last_name", locator_type="id")
            assert self.get_attribute_value(attribute_name="value",locator_value="shipping_last_name",locator_type="id").strip()==l_name
        self.after_edit_shipping_address['l_name'] = l_name
        



    def enter_shipping_company_name(self,c_name=None):
        if c_name is not None:
            if c_name=="random":
                c_name=self.faker.company()
            self.send_text(text=c_name, locator_value="shipping_company", locator_type="id")
            assert self.get_attribute_value(attribute_name="value", locator_value="shipping_company", locator_type="id").strip()==c_name
        self.after_edit_shipping_address['c_name'] = c_name
    


    def select_country_from_the_dropdown(self, country):
        pass



    def enter_shipping_street_address(self, street_address=None):
        if street_address is not None:
            if street_address == "random":
                street_address = self.faker.street_address()
            self.send_text(text=street_address, locator_value="shipping_address_1", locator_type="id")
            assert self.get_attribute_value(attribute_name="value", locator_value="shipping_address_1",
                                            locator_type="id").strip() == street_address
        self.after_edit_shipping_address['street_address'] = street_address


        
        
    def enter_shipping_optional_address(self,address_2=None):
        if address_2 is not None:
            if address_2=="random":
                address_2="some_new address"
            self.send_text(text=address_2, locator_value="shipping_address_2", locator_type="id")
            print(self.get_attribute_value(attribute_name="value", locator_value="shipping_address_2", locator_type="id").strip(),"......",address_2,"..............")
            print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
            assert self.get_attribute_value(attribute_name="value", locator_value="shipping_address_2", locator_type="id").strip()==address_2.strip()
        self.after_edit_shipping_address['address_2'] = address_2


        
    def enter_shipping_city_or_town(self,city_name):
        if city_name is not None:
            if city_name=="random":
                city_name="random city"
            self.send_text(text=city_name, locator_value="shipping_city", locator_type="id")
            assert self.get_attribute_value(attribute_name="value", locator_value="shipping_city", locator_type="id").strip()==city_name
        self.after_edit_shipping_address['city_name'] = city_name


    def select_shipping_state_or_county_from_the_dropdown(self,state_name):
        state_name_text=self.get_element(locator_value="select2-chosen-2",locator_type="id").text
        print(state_name_text)
        print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
        self.after_edit_shipping_address['state'] = state_name_text
        


    def enter_shipping_pincode(self,pincode=None):
        if pincode is not None:
            if pincode=="random":
                pincode=random.randint(111111,999999)
                print(pincode)
            self.send_text(text=pincode, locator_value="shipping_postcode", locator_type="id")
            print(self.get_attribute_value(attribute_name="value", locator_value="shipping_postcode", locator_type="id"),pincode)
            assert self.get_attribute_value(attribute_name="value", locator_value="shipping_postcode", locator_type="id").strip()==f"{pincode}".strip()
        self.after_edit_shipping_address['pincode'] = pincode
        print(self.after_edit_shipping_address)
        print("asdfghjkwertyuiosdfghjk.................................................")


    def is_shipping_first_name_field_visible(self):
        self.check_for_ele_displayed_or_not_displayed(locatorValue="shipping_first_name_field", locatorType="id")
        f_name = self.get_attribute_value(attribute_name="value", locator_value="shipping_first_name", locator_type="id")
        self.before_edit_shipping_address['f_name'] = f_name
        print("First Name", self.get_element(locator_value="//p[@id='shipping_first_name_field']/label",
                                             locator_type="xpath").text.strip())
        assert "First Name *" == self.get_element(locator_value="//p[@id='shipping_first_name_field']/label",
                                                  locator_type="xpath").text.strip()

    def is_shipping_last_name_field_visible(self):
        self.check_for_ele_displayed_or_not_displayed(locatorValue="shipping_last_name_field", locatorType="id")
        l_name = self.get_attribute_value(attribute_name="value", locator_value="shipping_last_name", locator_type="id")
        self.before_edit_shipping_address['l_name'] = l_name
        print("Last Name", self.get_element(locator_value="//p[@id='shipping_last_name_field']/label",
                                            locator_type="xpath").text.strip())
        assert "Last Name *" == self.get_element(locator_value="//p[@id='shipping_last_name_field']/label",
                                                 locator_type="xpath").text.strip()
        

   

    

    def is_shipping_company_field_visible(self):
        self.check_for_ele_displayed_or_not_displayed(locatorValue="shipping_company_field",locatorType="id")
        c_name=self.get_attribute_value(attribute_name="value",locator_value="shipping_company",locator_type="id")
        self.before_edit_shipping_address['c_name']=c_name
        print("Company Name",self.get_element(locator_value="//p[@id='shipping_company_field']/label",locator_type="xpath").text.strip())
        assert "Company Name"==self.get_element(locator_value="//p[@id='shipping_company_field']/label",locator_type="xpath").text.strip()
        
        
    def _is_shipping_country_field_visible(self):
        self.check_for_ele_displayed_or_not_displayed(locatorValue="shipping_country_field",locatorType="id")
        selected_country = self.get_attribute_value(attribute_name="value", locator_value="select2-chosen-1",
                                                  locator_type="id")
        self.before_edit_shipping_address["country"] = selected_country
        print("Country *",self.get_element(locator_value="//p[@id='shipping_country_field']/label",locator_type="xpath").text.strip())
        assert "Country *"==self.get_element(locator_value="//p[@id='shipping_country_field']/label",locator_type="xpath").text.strip()
 

    def _is_shipping_address_1_field_visible(self):
        self.check_for_ele_displayed_or_not_displayed(locatorValue="shipping_address_1_field",locatorType="id")
        address=self.get_attribute_value(attribute_name="value",locator_value="shipping_address_1",locator_type="id")
        self.before_edit_shipping_address['street_address']=address
        print("Address",self.get_element(locator_value="//p[@id='shipping_address_1_field']/label",locator_type="xpath").text.strip())
        assert "Address *"==self.get_element(locator_value="//p[@id='shipping_address_1_field']/label",locator_type="xpath").text.strip()


    def _is_shipping_address_2_field_visible(self):
        self.check_for_ele_displayed_or_not_displayed(locatorValue="shipping_address_2_field",locatorType="id")
        optional_address=self.get_attribute_value(attribute_name="value",locator_value="shipping_address_2",locator_type="id")
        self.before_edit_shipping_address["address_2"]=optional_address
        print(optional_address)



    def _is_shipping_city_field_visible(self):
        self.check_for_ele_displayed_or_not_displayed(locatorValue="shipping_city_field",locatorType="id")
        city=self.get_attribute_value(attribute_name="value",locator_value="shipping_city",locator_type="id")
        self.before_edit_shipping_address["city"]=city
        print("Town / City",self.get_element(locator_value="//p[@id='shipping_city_field']/label",locator_type="xpath").text.strip())
        assert "Town / City *"==self.get_element(locator_value="//p[@id='shipping_city_field']/label",locator_type="xpath").text.strip()


    def _is_shipping_state_field_visible(self):
        self.check_for_ele_displayed_or_not_displayed(locatorValue="shipping_state_field",locatorType="id")
        selected_state=self.get_attribute_value(attribute_name="value",locator_value="select2-chosen-2",locator_type="id")

        self.before_edit_shipping_address["state"]=selected_state
        print("State / County",self.get_element(locator_value="//p[@id='shipping_state_field']/label",locator_type="xpath").text.strip())
        assert "State / County *"==self.get_element(locator_value="//p[@id='shipping_state_field']/label",locator_type="xpath").text.strip()


    def _is_shipping_postcode_field_visible(self):
        self.check_for_ele_displayed_or_not_displayed(locatorValue="shipping_postcode_field",locatorType="id")
        input_text=self.get_attribute_value(attribute_name="value",locator_value="shipping_postcode",locator_type="id")
        self.before_edit_shipping_address["pincode"]=input_text
        print("Postcode / ZIP",self.get_element(locator_value="//p[@id='shipping_postcode_field']/label",locator_type="xpath").text.strip())
        assert "Postcode / ZIP *"==self.get_element(locator_value="//p[@id='shipping_postcode_field']/label",locator_type="xpath").text.strip()


    def _is_shipping_save_address_button_visible(self):
        self.check_for_ele_displayed_or_not_displayed(locatorValue="//input[@name='save_address' and @class='button']",locatorType="xpath")

        


    def enter_only_shipping_address_details(self,address_dict,user_email_address):
        self.fields=address_dict.keys()
        self.enter_shipping_first_name(address_dict.get('f_name'))
        self.enter_shipping_last_name(address_dict.get(f'l_name'))
        self.enter_shipping_company_name(address_dict.get('c_name'))
        self.select_country_from_the_dropdown(address_dict.get('country'))
        self.enter_shipping_street_address(address_dict.get('street_address'))
        self.enter_shipping_optional_address(address_dict.get('address_2'))
        self.enter_shipping_city_or_town(address_dict.get('city'))
        self.select_shipping_state_or_county_from_the_dropdown(address_dict.get('state'))
        self.enter_shipping_pincode(address_dict.get('pincode'))
        fields_not_filled=[field for field, value in self.after_edit_shipping_address.items() if value is None]
        print(fields_not_filled)
        print("dfghjk........................")
        current_url_page=self.driver.current_url
        self.click_on_save_address_button()
        if fields_not_filled:
            assert self.driver.current_url==current_url_page
            self.verify_error_message(fields_not_filled)
            return self.after_edit_shipping_address

        else:
            self.verify_saved_address(current_page_url=current_url_page,address_dict=self.after_edit_shipping_address)
            return self.after_edit_shipping_address




    def verify_error_message(self,expected_fields):

        text_mapping = {"f_name": "First Name", "l_name": "Last Name",
                        "street_address": "Address", "city_name": "Town / City", "pincode": "Postcode / ZIP"}
        expected_fields = [field for field in expected_fields if field in text_mapping.keys()]

        error_eles=self.getAllElements(locatorValue="//ul[@class='woocommerce-error']/li",locator_type="xpath")
        for index ,error_msg in enumerate(error_eles):
            print(error_msg.text)
            print("..........................")
            if expected_fields[index] in text_mapping.keys():
                print(f"{text_mapping[expected_fields[index]]} is a required field.")
                assert error_msg.text==f"{text_mapping[expected_fields[index]]} is a required field."