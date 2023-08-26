Feature: add new bank account

  @bank
  Scenario: adding with valid details
    Given I logged in and got navigated to Home page
    When I click on my account and go to payment options and click on manage bank accounts
    And I enter all the valid details
    Then account added message should be displayed

