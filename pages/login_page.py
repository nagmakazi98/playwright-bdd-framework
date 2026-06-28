from pages.base_page import BasePage

class LoginPage(BasePage):

    def login(self, username, password):
        self.page.fill("input[name='username']", username)
        self.page.fill("input[name='password']", password)
        self.page.click("input[value='Log In']")