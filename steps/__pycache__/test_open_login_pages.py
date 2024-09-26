from pytest_bdd import scenarios, given
from playwright.sync_api import sync_playwright

# Load feature files
scenarios('../features/amazon_login.feature')
scenarios('../features/google_login.feature')

# Fixture for browser setup
@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to `True` for headless mode
        page = browser.new_page()
        yield page
        browser.close()

# Step to open Amazon login page
@given('the user is on the Amazon login page')
def open_amazon_login_page(browser):
    browser.goto("https://www.amazon.com/ap/signin")

# Step to open Google login page
@given('the user is on the Google login page')
def open_google_login_page(browser):
    browser.goto("https://accounts.google.com/signin")
