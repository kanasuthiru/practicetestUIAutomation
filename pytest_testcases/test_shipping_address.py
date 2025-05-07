import pytest
class TestShiAppingddress:

    @pytest.mark.parametrize("address_dict",[{'f_name': 'random', 'l_name': 'random', 'c_name': 'random', 'country': 'random', 'street_address': 'random', 'address_2': 'random', 'city': 'random', 'state': "random", 'pincode': 'random'}])
    @pytest.mark.ship
    def test_to_validate_user_is_able_to_add_new_shipping_address(self,open_url,shipping_address_page,address_page,homepage,my_account_page,address_dict):
        user_name,password=my_account_page.register_new_user("random","random")
        print(user_name,password)
        my_account_page.click_on_address_link_from_my_account_menu()
        address_page.verify_address_page()
        address_page.click_on_shipping_address_edit_link()
        before_edit_address_details=shipping_address_page.verify_components_on_shipping_address_page()
        print(before_edit_address_details)
        after_edit_address_details=shipping_address_page.enter_only_shipping_address_details(address_dict,user_name)

    @pytest.mark.parametrize("address_dict",
                             [{ 'l_name': 'random', 'c_name': 'random',  'country': 'random', 'street_address': 'random',
                               'address_2': 'random', 'city': 'random', 'state': "random", 'pincode': 'random'},{'f_name': '',  'c_name': 'random',  'country': 'random', 'street_address': 'random',
                               'address_2': 'random', 'city': 'random', 'state': "random", 'pincode': 'random'},{'f_name': '', 'l_name': 'random', 'c_name': 'random',
                                'country': 'random', 'street_address': 'random',
                               'address_2': 'random', 'city': 'random', 'state': "random", 'pincode': 'random'},{'f_name': '', 'l_name': 'random', 'c_name': 'random',
                                'country': 'random', 'address_2': 'random', 'city': 'random', 'state': "random", 'pincode': 'random'},{}])
    @pytest.mark.bill_negative
    def test_to_validate_shipping_address_save_should_fail_due_to_empty_value_fields(self, open_url, shipping_address_page, address_page,
                                                                 homepage, my_account_page, address_dict):
        user_name, password = my_account_page.register_new_user("random", "random")
        print(user_name, password)
        my_account_page.click_on_address_link_from_my_account_menu()
        address_page.verify_address_page(b_address_exist=True)
        address_page.click_on_shipping_address_edit_link()
        before_edit_address_details = shipping_address_page.verify_components_on_shipping_address_page()
        print(before_edit_address_details)
        after_edit_address_details = shipping_address_page.enter_only_shipping_address_details(address_dict, user_name)

    @pytest.mark.bill
    def test_to_validate_edit_existing_address(self, open_url,shipping_address_page, address_page,homepage, my_account_page,address_dict):
        user_name, password = my_account_page.login_to_web_page("map", "Kanasu!58")
        print(user_name, password)
        my_account_page.click_on_address_link_from_my_account_menu()
        address_page.verify_address_page()
        address_page.click_on_shipping_address_edit_link()
        before_edit_address_details = shipping_address_page.verify_components_on_shipping_address_page()
        print(before_edit_address_details)
        after_edit_address_details = shipping_address_page.enter_only_shipping_address_details(address_dict, user_name)