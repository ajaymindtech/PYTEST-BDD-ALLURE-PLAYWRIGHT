Feature: Google Login

  Scenario: Successful login with valid credentials
    Given the user is on the Google login page
    When the user enters valid credentials
    Then the user should be logged in successfully

  Scenario: Unsuccessful login with invalid credentials
    Given the user is on the Google login page
    When the user enters invalid credentials
    Then the login attempt should fail
