Feature: Edit billing address
  @positive
  Scenario Outline: validate user is able to add new billing address
    Given user is on home screen page
    When  register a new user account
    And  edit Billing address
    Then  enter Billing address details and verify "<fields_and_value>"
    Examples:
      | fields_and_value |
    |     {'f_name': 'random', 'l_name': 'random', 'c_name': 'random', 'email_address': 'random', 'phone_number': 'random', 'country': 'random', 'street_address': 'random', 'address_2': 'random', 'city': 'random', 'state': "random", 'pincode': 'random'}]   |

  @positive
  Scenario Outline: validate user is able to add edit existing billing address
    Given user is on home screen page
    When login with existing user
    And  edit Billing address
    Then enter Billing address details and verify "<fields_and_value>"
    Examples:
       | fields_and_value |
     |  {'f_name': 'random', 'l_name': 'random', 'c_name': 'random', 'email_address': 'random', 'phone_number': 'random', 'country': 'random', 'street_address': 'random', 'address_2': 'random', 'city': 'random', 'state': "random", 'pincode': 'random'}   |


  @negative
  Scenario Outline: validate billing address should not allowed to  save without filling mandatory fields
    Given user is on home screen page
    When register a new user account
    And  edit Billing address
    Then enter Billing address details and verify "<fields_and_value>"

    Examples:
      |fields_and_value  |
      |  [{ 'l_name': 'random', 'c_name': 'random', 'email_address': 'random',phone_number': 'random', 'country': 'random', 'street_address': 'random','address_2': 'random', 'city': 'random', 'state': "random", 'pincode': 'random'}|
    |   {'f_name': '',  'c_name': 'random', 'email_address': 'random','phone_number': 'random', 'country': 'random', 'street_address': 'random','address_2': 'random', 'city': 'random', 'state': "random", 'pincode': 'random'}
  |{'f_name': '', 'l_name': 'random', 'c_name': 'random', 'email_address': 'random','country': 'random', 'street_address': 'random','address_2': 'random', 'city': 'random', 'state': "random", 'pincode': 'random'}|
  |{'f_name': '', 'l_name': 'random', 'c_name': 'random', 'email_address': 'random','phone_number': 'random', 'country': 'random','address_2': 'random', 'city': 'random', 'state': "random", 'pincode': 'random'},{}])|



  @negative
  Scenario Outline: validate user should not be allowed to save billing address
    Given user is on home screen page
    When register a new user account
    And edit Billing address
    Then enter Billing address details and verify "<fields_and_value>"
    Examples:
      | fields_and_value |
    |  {}              |