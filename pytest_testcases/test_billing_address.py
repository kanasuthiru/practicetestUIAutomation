import pytest
class TestBillingAddress:

    @pytest.mark.parametrize("address_dict",[{'f_name': 'random', 'l_name': 'random', 'c_name': 'random', 'email_address': 'random', 'phone_number': 'random', 'country': 'random', 'street_address': 'random', 'address_2': 'random', 'city': 'random', 'state': "random", 'pincode': 'random'}])
    @pytest.mark.positive
    def test_to_validate_user_is_able_to_add_new_billing_address(self,open_url,billing_address_page,address_page,homepage,my_account_page,address_dict):
        user_name,password=my_account_page.register_new_user("random","random")
        my_account_page.click_on_address_link_from_my_account_menu()
        address_page.verify_address_page()
        address_page.click_on_billing_address_edit_link()
        before_edit_address_details=billing_address_page.verify_components_on_billing_address_page()
        after_edit_address_details=billing_address_page.enter_only_billing_address_details(address_dict,user_name)

    @pytest.mark.parametrize("address_dict",
                             [{ 'l_name': 'random', 'c_name': 'random', 'email_address': 'random',
                               'phone_number': 'random', 'country': 'random', 'street_address': 'random',
                               'address_2': 'random', 'city': 'random', 'state': "random", 'pincode': 'random'},{'f_name': '',  'c_name': 'random', 'email_address': 'random',
                               'phone_number': 'random', 'country': 'random', 'street_address': 'random',
                               'address_2': 'random', 'city': 'random', 'state': "random", 'pincode': 'random'},{'f_name': '', 'l_name': 'random', 'c_name': 'random', 'email_address': 'random',
                                'country': 'random', 'street_address': 'random',
                               'address_2': 'random', 'city': 'random', 'state': "random", 'pincode': 'random'},{'f_name': '', 'l_name': 'random', 'c_name': 'random', 'email_address': 'random',
                               'phone_number': 'random', 'country': 'random',
                               'address_2': 'random', 'city': 'random', 'state': "random", 'pincode': 'random'},{}])
    @pytest.mark.negative
    def test_to_validate_billing_address_save_should_fail_due_mandatory_fields_empty(self, open_url, billing_address_page, address_page,
                                                                 homepage, my_account_page, address_dict):
        user_name, password = my_account_page.register_new_user("random", "random")
        my_account_page.click_on_address_link_from_my_account_menu()
        address_page.verify_address_page(b_address_exist=True)
        address_page.click_on_billing_address_edit_link()
        before_edit_address_details = billing_address_page.verify_components_on_billing_address_page()
        after_edit_address_details = billing_address_page.enter_only_billing_address_details(address_dict, user_name)

    @pytest.mark.positive
    def test_to_validate_edit_existing_address(self, open_url,billing_address_page, address_page,homepage, my_account_page,address_dict):
        user_name, password = my_account_page.login_to_web_page("map", "Kanasu!58")

        my_account_page.click_on_address_link_from_my_account_menu()
        address_page.verify_address_page()
        address_page.click_on_billing_address_edit_link()
        before_edit_address_details = billing_address_page.verify_components_on_billing_address_page()
        after_edit_address_details = billing_address_page.enter_only_billing_address_details(address_dict, user_name)











