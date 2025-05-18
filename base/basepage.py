from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    ElementNotVisibleException, NoSuchElementException,
    ElementNotSelectableException, StaleElementReferenceException
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

from utils.logger import setup_logging


class basePage:
    def __init__(self,driver):
        self.driver=driver


    # Get the root logger (or you can create/get a named logger)

    def wait_for_element(self, locator_value, locator_type, wait_action=None, time_out=5, scroll_to_view=True):
        try:
            wait = WebDriverWait(self.driver, timeout=time_out, poll_frequency=.1,
                                 ignored_exceptions=[StaleElementReferenceException, ElementNotVisibleException,
                                                     ElementNotSelectableException, NoSuchElementException])
            locator_type = self.get_locator_type(locator_type)
            element = None
            if wait_action=="clickable":
                element = wait.until(EC.element_to_be_clickable((locator_type, locator_value)))
            elif    wait_action=="visibility":
                element= wait.until(EC.visibility_of_element_located((locator_type,locator_value)))
            elif wait_action=="invisibility":
                element=wait.until(EC.invisibility_of_element((locator_type,locator_value)))
            elif  wait_action is None:
                element=self.driver.find_element(locator_type,locator_value)
                sleep(.5)
            return element
        except Exception as e:
            setup_logging().error("wait_for_element failed.")
            setup_logging().error(f"Locator: {locator_type}='{locator_value}', Action: {wait_action}")
            setup_logging().exception(e)
        assert  False


    def get_element(self,locator_value,locator_type,wait_action=None,timeout=5):
        try:
            element=self.wait_for_element(locator_value,locator_type,wait_action=wait_action,time_out=timeout)
            return element
        except Exception as e:
            assert  False
    def move_to_element(self,locator_value,locator_type):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_element(locator_value=locator_value,locator_type=locator_type)).click().perform()
        sleep(10)

    def getAllElements(self, locatorValue,locator_type, time_out=5):
        locator_type = self.get_locator_type(locator_type)
        try:
            eles = self.driver.find_elements(locator_type, locatorValue)
            return eles
        except Exception as e:
            self.takeScreenshot("xpath")
            assert False


    def  click_element(self,locator_value,locator_type,wait_action="clickable",timeout=5):
        try:
            element=self.get_element(locator_value, locator_type, wait_action, timeout)
            element.click()
        except Exception as e:
            assert False

    def send_text(self,text,locator_value,locator_type,wait_action="clickable",time_out=10):
        try:
            element=self.get_element(locator_value,locator_type,wait_action=wait_action,timeout=time_out)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            assert False

    def get_attribute_value(self,attribute_name,locator_type="xpath",locator_value=None,wait_action="visibility",time_out=10):
        try:
            element=self.get_element(locator_value,locator_type,wait_action=wait_action,timeout=time_out)
            attribute_value=element.get_attribute(attribute_name)
            return attribute_value
        except Exception as e:
            assert False



    def wait_until_url_change(self, current_url):
        WebDriverWait(self.driver, 10).until(EC.url_changes(current_url))
        assert current_url!=self.driver.current_url

    def attribute_to_be_changed(self, locatorValue, locatorType, attribute_name,old_attribute_value,required_text=None):
        attribute_value=self.get_attribute_value(attribute_name=attribute_name,locator_type=locatorType,locator_value=locatorValue)
        if required_text is not None:
            return attribute_value==required_text
        return attribute_value!=old_attribute_value


    def wait_until_attribute_value_changes(self,before_attribute_value,locator_type,locator_value,attribute_name,required_text=None,time_out=20):
        WebDriverWait(self.driver, timeout=time_out, poll_frequency=.1).until(
            lambda driver: self.attribute_to_be_changed(locatorValue=locator_value, locatorType=locator_type,attribute_name=attribute_name,old_attribute_value=before_attribute_value,required_text=required_text) == True)


    def check_for_ele_displayed_or_not_displayed(self, locatorValue, locatorType="xpath", status_flag=True, timeout=20):
        try:
            WebDriverWait(self.driver, timeout, poll_frequency=.1).until(
                lambda driver: self.is_element_displayed(locatorValue, locatorType, status_flag) == True)
            # self.log.info(
            #     f"Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + f" is present and {'Displayed' if status_flag == True else 'not Displayed'}.")
        except Exception as e:
            # self.log.error(
            #     f"Element with LocatorType: {locatorType} and with the locatorValue : {locatorValue} is {'Displayed' if status_flag == True else 'Not Displayed'} Error: {str(e)}")
            # self.takeScreenshot(f"Enabled_or_Disabled_element_status")
            assert False



    def is_element_displayed(self, locatorValue, locatorType, status_flag, timeout=5):
        status = True
        if not status_flag:
            eles = self.getAllElements(locatorValue=locatorValue,locator_type=locatorType)
            if len(eles) == 0:
                status = False
        else:
            element = self.get_element(locator_value=locatorValue, locator_type=locatorType, timeout=timeout, wait_action="visibility")
            status = element.is_displayed()
        return status == status_flag

    def get_element_with_in_element(self,element, locator_value, locator_type,multiple_elements=False):
        try:
            locator_type = self.get_locator_type(locator_type)
            if multiple_elements:
                return element.find_elements(locator_type, locator_value)
            else:
                return element.find_element(locator_type,locator_value)
        except Exception  as e:
            assert False


    def get_locator_type(self, locator_type):
        locator_type_dict = {
            "id": By.ID,
            "xpath": By.XPATH,
            "name": By.NAME,
            "class": By.CLASS_NAME,
            "tag_name": By.TAG_NAME,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT,
            "css_selector": By.CSS_SELECTOR
        }
        return locator_type_dict.get(locator_type.lower(),None)





