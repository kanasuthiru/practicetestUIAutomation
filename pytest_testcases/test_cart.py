


import pytest
class TestCart:
    product_names = [
        'Android Quick Start Guide'
    ]

    @pytest.mark.positive
    @pytest.mark.parametrize("product_name", product_names)
    def test_add_item_into_cart_with_out_login_from_shop_page(self,open_url,homepage,shop_page,product_name,basket_page):
        homepage.click_on_my_shop_menu()
        product_dict=shop_page.get_all_products_name_and_its_price_from_shop_page()
        product_names = [product['name'] for product in product_dict.values()]
        count=shop_page.click_on_add_basket(product_name)
        shop_page.check_for_view_basket_component_in_shop_page(product_name)
        # =homepage.get_cart_item_count_and_amount_from_menu()
        shop_page.click_on_view_basket_in_shop_page(product_name)
        basket_page.verify_added_product_is_showing_in_cart(product_name,product_dict,added_quantity=count)




    @pytest.mark.parametrize("product_name", product_names)
    @pytest.mark.positive
    def test_to_empty_cart_by_removing_items(self,open_url,homepage,basket_page,shop_page,product_name):
        homepage.click_on_my_shop_menu()
        product_dict = shop_page.get_all_products_name_and_its_price_from_shop_page()
        count = shop_page.click_on_add_basket(product_name)
        shop_page.check_for_view_basket_component_in_shop_page(product_name)
        # =homepage.get_cart_item_count_and_amount_from_menu()
        shop_page.click_on_view_basket_in_shop_page(product_name)
        basket_page.verify_added_product_is_showing_in_cart(product_name, product_dict, added_quantity=count)
        bef_product_name_list,bef_product_present_in_basket_dict=basket_page.remove_product_from_basket_using_remove_this_item([product_name])
        basket_page.verify_cart_is_empty(remove=True)



    @pytest.mark.positive
    @pytest.mark.parametrize("product_info", [
        {'Android Quick Start Guide': 1, 'HTML5 Forms': 2},
    ])
    def test_to_increase_quantity_of_item_from_the_cart(self,open_url,homepage,basket_page,shop_page,product_info):
        homepage.click_on_my_shop_menu()
        product_dict = shop_page.get_all_products_name_and_its_price_from_shop_page()
        for product_name,value in product_info.items() :
            count = shop_page.click_on_add_basket(product_name)
            shop_page.check_for_view_basket_component_in_shop_page(product_name)
        # =homepage.get_cart_item_count_and_amount_from_menu()
            homepage.click_on_cart_icon_menu()
            basket_page.verify_added_product_is_showing_in_cart(product_name, product_dict, added_quantity=count)
        basket_page.increase_quantity_product_from_basket(product_info)
        basket_page.click_on_update_cart_in_basket_page()
        basket_page.verify_updated_cart()









