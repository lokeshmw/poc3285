Feature: change address

  @change_address
  Scenario: changing delivery address
    Given I logged into account and got navigated to the Homepage
    When I clicked on delivery address option
    And changed the address to what is requested
