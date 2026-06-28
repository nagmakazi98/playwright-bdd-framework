from pages.base_page import BasePage

class DashboardPage(BasePage):

    def get_balance(self):
        balance = self.page.locator("#accountTable >> tbody >> tr >> td:nth-child(2)").first.inner_text()
        print(f"Account Balance: {balance}")
        return balance