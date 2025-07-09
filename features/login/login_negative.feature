Feature: Login functionality on saucedemo

  @smoke
  Scenario Outline: User logs in with invalid credentials
    Given the user is on the saucedemo login page
    When the user enters username "<username>" and password "<password>"
    Then the user should see an error message

    Examples:
      | username              | password       |
      | standard_user         | wrong_pass     |
      | locked_out_user       | secret_sauce   |
      |                       | secret_sauce   |
      | standard_user         |                |
      |                       |                |
      | !@#$%^&*()            | secret_sauce   |
      | standard_user         | !@#$%^&*()     |