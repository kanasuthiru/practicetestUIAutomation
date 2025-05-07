from time import sleep

from behave import *
from dotenv import load_dotenv
load_dotenv()
import os

class Register:



    @when(u'enters non register "{email_address}" and "{Password}"')
    def step_impl(context,email_address,Password):
        context.myAcc.enter_register_email_address(context,email_address)
        context.myAcc.enter_register_password(context,Password)
        context.myAcc.check_for_password_strength()


    @when(u'clicks on the Register button')
    def step_impl(context):
        context.email_address,context.password=context.myAcc.click_on_register_button()

    @then(u'User("{email_address}") will be registered successfully and will be navigated to the Home page')
    def step_impl(context,email_address):
        if "random" in email_address:
            UserName=context.email_address
        context.myAcc.verify_user_logged_in_successfully(username=UserName)
        # context.myAcc.click_on_sign_out_link()
        # context.myAcc.verify_user_is_on_login_screen()
        # context.execute_steps("""
        #              When user clicks on My Account menu
        #              When enters registered "{UserName}" and valid "{Password}"
        #              When clicks on the login button
        #              Then User("{UserName}") should successfully login to the web page
        #         """.format(UserName=UserName, Password=context.password))





    @when(u'enters invalid non register "{email_address}" and valid "{Password}"')
    def step_impl(context,email_address,Password):
        context.myAcc.enter_register_email_address(context, email_address)
        context.myAcc.enter_register_password(context, Password)


    @then(u'Registration must fail with a warning message "{reason}"')
    def step_impl(context,reason):
        context.myAcc.verify_user_is_on_login_screen()
        context.myAcc.verify_error_message(context, reason,component="register")

    @when(u'enters "{password}" into register password field')
    def step_impl(context,password):
        context.myAcc.enter_register_password(context, password)

    @when(u'enters "{email_address}" into register email address field')
    def step_impl(context,email_address):
        context.myAcc.enter_register_email_address(context, email_address)




