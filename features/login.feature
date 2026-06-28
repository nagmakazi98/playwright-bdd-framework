Feature: Parabank Login

  Scenario: User logs in and views balance
    Given user is on login page
    And user has valid credentials
    When user logs in with valid credentials
    Then user should see account balance