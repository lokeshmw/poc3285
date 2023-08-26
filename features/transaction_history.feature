Feature: print transactions history

  @transactions
  Scenario: getting details
    Given I logged in to my account and got navigated to Home page
    When I click on my account and go to amazon pay option
    And click on transactions
    Then all transactions are printed