import pytest
from pytest_bdd import scenarios, given
from playwright.sync_api import sync_playwright
import os

# Load feature files for both Amazon and Google login tests
scenarios('../tests/features/amazon_login.feature')
scenarios('../tests/features/google_login.feature')

# Fixture for browser setup
@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to `True` for headless mode
        page = browser.new_page()
        yield page
        browser.close()

# Step to open Amazon login page and save screenshot
@given('the user is on the Amazon login page')
def open_amazon_login_page(browser):
    # Step 1: Navigate to Amazon login page
    browser.goto("https://www.amazon.com/ap/signin")
    
    # Step 2: Wait for 2 minutes (120000 milliseconds) or 2 seconds for testing
    browser.wait_for_timeout(2000)  # Adjust to 120000 for 2 minutes wait

    # Step 3: Define the screenshot directory and save the screenshot
    screenshot_dir = os.path.join(os.getcwd(), "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)  # Ensure directory exists
    screenshot_path = os.path.join(screenshot_dir, "amazon_login_page.png")
    browser.screenshot(path=screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")

# Step to open Google login page and save screenshot
@given('the user is on the Google login page')
def open_google_login_page(browser):
    # Step 1: Navigate to Google login page
    browser.goto("https://accounts.google.com/signin")
    
    # Step 2: Wait for 2 minutes (120000 milliseconds) or 2 seconds for testing
    browser.wait_for_timeout(2000)  # Adjust to 120000 for 2 minutes wait

    # Step 3: Define the screenshot directory and save the screenshot
    screenshot_dir = os.path.join(os.getcwd(), "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)  # Ensure directory exists
    screenshot_path = os.path.join(screenshot_dir, "google_login_page.png")
    browser.screenshot(path=screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")
