Feature: Login functionality

  @smoke
  Scenario: User logs in with wrong password
    Given the user is on the saucedemo login page
    When the user logs in with username "standard_user" and password "wrong_pass"
    Then the user should see an error message
