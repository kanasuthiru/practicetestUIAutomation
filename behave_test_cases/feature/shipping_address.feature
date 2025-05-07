Feature: Edit shipping address

  @possitive
  Scenario Outline: validate user is able to add new shipping address
    Given user is on home screen page
    When register a new user account
    And  edit shipping address
    Then fill shipping address details and verify "<fields_and_value>"
   Examples:
      | fields_and_value |
     |   {'f_name': 'random', 'l_name': 'random', 'c_name': 'random', 'email_address': 'random', 'phone_number': 'random', 'country': 'random', 'street_address': 'random', 'address_2': 'random', 'city': 'random', 'state': "random", 'pincode': 'random'}               |

  @possitive
  Scenario Outline: validate user is able to add edit existing shipping address
    Given user is on home screen page
    When login with existing user
    And  edit shipping address
    Then  fill shipping address details and verify "<fields_and_value>"
    Examples:
      | fields_and_value |
     | {'f_name': 'random', 'l_name': 'random', 'c_name': 'random', 'email_address': 'random', 'phone_number': 'random', 'country': 'random', 'street_address': 'random', 'address_2': 'random', 'city': 'random', 'state': "random", 'pincode': 'random'}                 |

#
   @negative
  Scenario Outline: validate user should not be allowed to save shipping address
    Given user is on home screen page
    When register a new user account
    And  edit shipping address
    Then fill shipping address details and verify "<fields_and_value>"
Examples:
      | fields_and_value |
     |    { 'l_name': 'random', 'c_name': 'random',  'country': 'random', 'street_address': 'random','address_2': 'random', 'city': 'random', 'state': "random", 'pincode': 'random'}             |
     |{'f_name': '',  'c_name': 'random',  'country': 'random', 'street_address': 'random','address_2': 'random', 'city': 'random', 'state': "random", 'pincode': 'random'}|
      |{'f_name': '', 'l_name': 'random', 'c_name': 'random','country': 'random', 'address_2': 'random', 'city': 'random', 'state': "random", 'pincode': 'random'}])        |
    |       {}                                                                                                                                                              |






