Feature: feature to check login functionality

  Scenario: Check login successfully with valid credential
    Given open a browser
    When user is on login page
    And user enters "kakaderiddhi18@gmail.com" and "Riddhi@123"
    And Click on the login button
    Then user is navigate to the homepage

  Scenario Outline: Check login with invalid credential
    Given open a browser
    When user is on login page
    And user enters "<username>" and "<password>"
    And Click on the login button
    Then user is navigate to the homepage

    Examples:
      |  username     | password |
      | Kakaderiddhi  | 12345    |
      | kriddhi        | 374327   |


