Feature: Register to Automation Practice Site

  @positive
  Scenario Outline:validate user is able to Register an Account
    Given user is on home screen page
    When user clicks on My Account menu
    And enters non register "<UserName>" and "<Password>"
    And clicks on the Register button
    Then User("<UserName>") will be registered successfully and will be navigated to the Home page
    Examples:
      | UserName |Password|
      |   random | random|

  @negative
  Scenario Outline:validate user should not be allowed to register with invalid email_id
    Given user is on home screen page
    When user clicks on My Account menu
    And enters invalid non register "<email_address>" and valid "<Password>"
    And clicks on the Register button
    Then Registration must fail with a warning message "invalid_email_address"
    Examples:
      | email_address           |Password|
      |   plainaddress          | random|
      |     abc@.com            | random |
      |    @no-local-part.com   | random |
      |    annd.com             | random |
      |   username@com          |random  |
      |  user name@example.com	|random  |
      |username@ex!ample.com	|random  |
      |   abc@ggg..com          |random  |

  @negative
  Scenario Outline:validate user should not be allowed to register without email address
    Given user is on home screen page
    When user clicks on My Account menu
    And enters "<password>" into register password field
    And clicks on the Register button
    Then Registration must fail with a warning message "empty_email_address"
    Examples:
      |password|
      | random|

  @negative
  Scenario Outline:validate user should not be allowed to register without email address
    Given user is on home screen page
    When user clicks on My Account menu
    And enters "<email_address>" into register email address field
    And clicks on the Register button
    Then Registration must fail with a warning message "empty_password"
    Examples:
      |email_address|
      | random|

   @negative
  Scenario:validate user should not be allowed to register without email address
    Given user is on home screen page
    When user clicks on My Account menu
    And clicks on the Register button
    Then Registration must fail with a warning message "empty_email_address_and_password"
