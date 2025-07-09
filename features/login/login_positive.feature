Feature: Login functionality on saucedemo

  @smoke
  Scenario Outline: User logs in with different credentials
    Given the user is on the saucedemo login page
    When the user enters username "<username>" and password "<password>"
    Then the user should see the products page

    Examples:
      | username        | password       |
      | standard_user   | secret_sauce   |
      | performance_glitch_user | secret_sauce |