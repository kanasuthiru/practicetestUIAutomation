import ast

from behave import *
from dotenv import load_dotenv

load_dotenv()
import os


class Shipping_and_Billing:

    @when(u'register a new user account')
    def step_impl(context):
        context.email_address, context.password = context.myAcc.register_new_user(user_name="random", password="random")
        context.myAcc.click_on_address_link_from_my_account_menu()
        context.add.verify_address_page()

    @when(u'edit shipping address')
    def step_impl(context):
        context.add.click_on_shipping_address_edit_link()


    @then(u'fill shipping address details and verify "{fields_and_value}"')
    def step_impl(context,fields_and_value):
        context.before_edit_address_details = context.ship.verify_components_on_shipping_address_page()
        context.ship.enter_only_shipping_address_details(addcress_dict=ast.literal_eval(fields_and_value))

    @when(u'edit Billing address')
    def step_impl(context):
        context.add.click_on_billi_adngdress_edit_link()

    @then(u'enter Billing address details and verify "{fields_and_value}"')
    def step_impl(context,fields_and_value):
        context.before_edit_address_details = context.ship.verify_components_on_billing_address_page()
        context.ship.enter_only_billing_address_details(addcress_dict=ast.literal_eval(fields_and_value))

    @when(u'login with existing user')
    def step_impl(context):
        context.email_address, context.password = context.myAcc.login_to_web_page(user_name="map", password="Kanasu!58")
        context.myAcc.click_on_address_link_from_my_account_menu()
        context.add.verify_address_page()



