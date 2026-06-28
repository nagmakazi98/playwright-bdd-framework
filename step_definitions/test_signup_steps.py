import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pytest_bdd import scenarios, given, when, then
from pages.signup_page import SignupPage
import pytest

FEATURE_FILE = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "features", "signup.feature")
)

scenarios(FEATURE_FILE)

@pytest.fixture
def test_context():
    return {}

# ------------------ STEPS ------------------

@given("user is on parabank homepage")
def open_home(page):
    page.goto("https://parabank.parasoft.com/parabank/index.htm")


@when("user navigates to signup page")
def go_to_signup(page):
    SignupPage(page).navigate_to_signup()


@when("user enters valid registration details")
def fill_form(page, test_context):
    signup = SignupPage(page)
    
    username, password = signup.fill_registration_form()

    #Store data for reuse
    test_context["username"] = username
    test_context["password"] = password


@then("account should be created successfully")
def verify_signup(page):
    signup = SignupPage(page)
    page.wait_for_load_state("networkidle")

    assert signup.verify_account_created(), "Account creation failed"