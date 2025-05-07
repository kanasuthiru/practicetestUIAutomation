Feature: Login to Automation Practice Site

  @positive
  Scenario Outline:validate user is able to login with Valid Credentials
    Given user is on home screen page
    When user clicks on My Account menu
    And enters registered "<UserName>" and valid "<Password>"
    And clicks on the login button
    Then User("<UserName>") should successfully login to the web page
    Examples:
      | UserName |Password|
      |    map |   Kanasu!58|

 @negative
  Scenario Outline:validate user is not able to login with invalid Username
    Given user is on home screen page
    When user clicks on My Account menu
    And enters invalid "<UserName>" and valid "<Password>"
    And clicks on the login button
    Then User should not be allowed to login to web page "non_registered_username"
    Examples:
      |UserName |Password     |
      |  map 33   | Kanasu!58 |



  @negative
  Scenario Outline:validate user is not able to login with invalid username and password
    Given user is on home screen page
    When user clicks on My Account menu
    And enters  invalid "<UserName>" and invalid "<Password>"
    And clicks on the login button
    Then User should not be allowed to login to web page "invalid-username_and_password"
    Examples:
      |UserName |Password     |
      |  map123    | Kanasu!8  |


  @negativee
  Scenario Outline:validate user is not able to login with invalid password
    Given user is on home screen page
    When user clicks on My Account menu
    And enters valid "<UserName>" and invalid "<Password>"
    And clicks on the login button
    Then User should not be allowed to login to web page "wrong_password"
    Examples:
      |UserName |Password     |
      |  map    | Kanasu!8    |


  @negative
  Scenario Outline:validate user is not able to login by only entering valid password
    Given user is on home screen page
    When user clicks on My Account menu
    And enters "<Password>" into password field
    And clicks on the login button
    Then User should not be allowed to login to web page "empty_username"
    Examples:
      |Password     |
      | Kanasu!58   |

  @negative
  Scenario Outline:validate user is not able to login without entering the creds
    Given user is on home screen page
    When user clicks on My Account menu
    And enters  "<UserName>" into username field
    And clicks on the login button
    Then User should not be allowed to login to web page "empty_password"
    Examples:
      |UserName |
      |  map    |

  @negative
  Scenario:validate user is not able to login without entering the creds
    Given user is on home screen page
    When user clicks on My Account menu
    And clicks on the login button
    Then User should not be allowed to login to web page "empty_username_and_password"

  @positive
  Scenario: Verify password input is masked
    Given user is on home screen page
    When user clicks on My Account menu
    And the user enters a "<password>" in the password field
    Then the password field should be masked

   @negative
  Scenario Outline: Validate Login Authentication by signing out after login and navigating back to previous page
    Given user is on home screen page
    When user login to web page "<UserName>" "<Password>"
    And click on sign out
    And click on browser back navigation once user signed out from the account
    Then  User should be on Login or register in my account UI
    Examples:
      | UserName |Password|
      |    map |   Kanasu!58  |


#think about some low network scenario or without
  #logs
  #report
  #git
