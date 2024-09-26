import pytest
from pytest_bdd import scenarios, given
from playwright.sync_api import sync_playwright

# Load the feature files for both Amazon and Google login tests
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
    # Step 1: Navigate to Amazon login page
    browser.goto("https://www.amazon.com/ap/signin")
    
    # Step 2: Wait for 2 minutes (120000 milliseconds)
    browser.wait_for_timeout(120000)  # 2 minutes wait

    # Step 3: Take a screenshot after waiting
    browser.screenshot(path="amazon_login_page.png")
    print("Screenshot saved as amazon_login_page.png")

# Step to open Google login page
@given('the user is on the Google login page')
def open_google_login_page(browser):
    # Step 1: Navigate to Google login page
    browser.goto("https://accounts.google.com/signin")
    
    # Step 2: Wait for 2 minutes (120000 milliseconds)
    browser.wait_for_timeout(120000)  # 2 minutes wait

    # Step 3: Take a screenshot after waiting
    browser.screenshot(path="google_login_page.png")
    print("Screenshot saved as google_login_page.png")
