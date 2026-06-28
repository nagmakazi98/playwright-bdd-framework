Feature: User onboarding and login

Scenario: User signs up and then logs in successfully
  Given user is on signup page
  When user enters valid registration details
  Then account should be created successfully
  When user logs in with valid credentials
  Then user should see account balance