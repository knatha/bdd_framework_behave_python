Feature: Login functionality

  @smoke
  Scenario: User logs in
    Given the user is on the saucedemo login page
    When the user logs in
    Then the user should see the products page