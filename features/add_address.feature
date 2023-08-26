Feature: print transactions history

  @address
  Scenario: adding new address
    Given I logged into my account and got navigated to Homepage
    When I click on my account and go to address option
    And click on add a new address
    Then entered all the details and added it