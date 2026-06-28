import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import pytest

FEATURE_FILE = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "features", "login.feature")
)

scenarios(FEATURE_FILE)

@pytest.fixture
def test_context():
    return {}

# ------------------ STEPS ------------------

@given("user is on login page")
def open_login(page):
    page.goto("https://parabank.parasoft.com/parabank/index.htm")

@given("user has valid credentials")
def set_credentials(test_context):
    if "username" not in test_context:
        test_context["username"] = "john"
        test_context["password"] = "demo"


@when("user logs in with valid credentials")
def login_user(page, test_context):
    LoginPage(page).login(
        test_context["username"],
        test_context["password"]
    )


@then("user should see account balance")
def verify_balance(page):
    dashboard = DashboardPage(page)
    page.wait_for_load_state("networkidle")
    balance = dashboard.get_balance()
    assert balance is not None and balance != "", "Balance not displayed"