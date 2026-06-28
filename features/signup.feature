Feature: Parabank Signup

  Scenario: User should be able to sign up successfully
    Given user is on parabank homepage
    When user navigates to signup page
    And user enters valid registration details
    Then account should be created successfully