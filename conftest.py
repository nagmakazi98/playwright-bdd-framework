import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        yield page

        # take screenshot only if test fails
        if request.node.rep_call.failed:
            page.screenshot(path=f"reports/{request.node.name}.png")

        browser.close()


# hook to capture test result
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


# @pytest.fixture(scope="function")
# def context():
#     return {}

@pytest.fixture
def test_context():
    return {}