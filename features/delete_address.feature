Feature: Deleting  address

  @delete_address
  Scenario: Deleting address and verifying
    Given I logged in into my account and got navigated to Homepage
    When I clicked on my account and then to address option
    And deleted a address which is requested
    Then validating the deleted message