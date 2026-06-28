from pages.base_page import BasePage
import random

class SignupPage(BasePage):

    def navigate_to_signup(self):
        self.page.click("text=Register")

    def fill_registration_form(self):
        rand = random.randint(1000, 9999)

        self.username = f"user{rand}"
        self.password = "Test@123"

        self.page.fill("#customer\\.firstName", "Test")
        self.page.fill("#customer\\.lastName", "User")
        self.page.fill("#customer\\.address\\.street", "Street 1")
        self.page.fill("#customer\\.address\\.city", "Mumbai")
        self.page.fill("#customer\\.address\\.state", "MH")
        self.page.fill("#customer\\.address\\.zipCode", "400001")
        self.page.fill("#customer\\.phoneNumber", "9999999999")
        self.page.fill("#customer\\.ssn", "1234")

        self.page.fill("#customer\\.username", self.username)
        self.page.fill("#customer\\.password", self.password)
        self.page.fill("#repeatedPassword", self.password)

        self.page.click("input[value='Register']")

        return self.username, self.password

    def verify_account_created(self):
        return self.page.locator("text=Your account was created successfully").is_visible()