from time import sleep

from behave import *
from dotenv import load_dotenv
load_dotenv()
import os

class Login:

    @given(u'user is on home screen page')
    def open_browser(context):
        context.driver.get(os.getenv("web_page_url"))
        assert os.getenv("web_page_url") == context.driver.current_url
        context.hp.verify_user_is_on_home_screen()

    @when(u'user clicks on My Account menu')
    def step_impl(context):
        context.hp.click_on_my_account_menu()



    @when(u'enters registered "{UserName}" and valid "{Password}"')
    def step_impl(context,UserName,Password):
        print(UserName)
        context.myAcc.enter_login_user_name(context,UserName)
        context.myAcc.enter_login_password(context,Password)


    @when(u'clicks on the login button')
    def step_impl(context):
        context.username,context.password=context.myAcc.click_on_login_button()



    @then(u'User("{UserName}") should successfully login to the web page')
    def step_impl(context,UserName):
        context.myAcc.verify_user_logged_in_successfully(UserName)


    @when(u'enters invalid "{UserName}" and valid "{Password}"')
    def step_impl(context,UserName,Password):
        context.myAcc.enter_login_user_name(context,UserName)
        context.myAcc.enter_login_password(context,Password)

    @then(u'User should not be allowed to login to web page "{reason}"')
    def step_impl(context,reason):
        context.myAcc.verify_user_is_on_login_screen()
        context.myAcc.verify_error_message(context,reason)


    @when(u'enters  invalid "{UserName}" and invalid "{Password}"')
    def step_impl(context,UserName,Password):
        context.myAcc.enter_login_user_name(context,UserName)
        context.myAcc.enter_login_password(context,Password)

    @when(u'enters valid "{UserName}" and invalid "{Password}"')
    def step_impl(context,UserName,Password):
        context.myAcc.enter_login_user_name(context,UserName)
        context.myAcc.enter_login_password(context,Password)

    @when(u'enters "{Password}" into password field')
    def step_impl(context,Password):
        context.myAcc.enter_login_password(context,Password)

    @when(u'enters  "{UserName}" into username field')
    def step_impl(context,UserName):
        context.myAcc.enter_login_user_name(context,UserName)



    @when(u'the user enters a "{Password}" in the password field')
    def step_impl(context,Password):
        context.myAcc.enter_login_password(context,Password)


    @then(u'the password field should be masked')
    def password_type_verification(context):
        context.myAcc.verify_password_field_type_value()


    @when(u'user login to web page "{UserName}" "{Password}"')
    def step_impl(context,UserName,Password):
        context.execute_steps("""
             When user clicks on My Account menu
             When enters registered "{UserName}" and valid "{Password}"
             When clicks on the login button
             Then User("{UserName}") should successfully login to the web page
        """.format(UserName=UserName,Password=Password))

    @when(u'click on sign out')
    def step_impl(context):
        context.myAcc.click_on_sign_Out_link()

    @when(u'click on browser back navigation once user signed out from the account')
    def step_impl(context):
        context.driver.back()

    @then(u'User should be on Login or register in my account UI')
    def step_impl(context):
        context.myAcc.verify_user_is_on_login_screen()


    # @when(u'the user enters a "{password}" in the password field')
    # def step_impl(context,password):
    #     context.myAcc.enter_login_password(context,password)
