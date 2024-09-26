from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import sync_playwright

# Load the feature file
scenarios('../features/google_login.feature')

# Given Step: Open Google login page
@given('the user is on the Google login page')
def open_google_login_page(page):
    page.goto("https://accounts.google.com/signin")
    page.wait_for_load_state()

# When Step: Enter valid credentials
@when('the user enters valid credentials')
def enter_valid_credentials(page):
    page.fill('input[type="email"]', "your-email@gmail.com")
    page.click('button:has-text("Next")')
    page.wait_for_selector('input[type="password"]')
    page.fill('input[type="password"]', "your-password")
    page.click('button:has-text("Next")')

# When Step: Enter invalid credentials
@when('the user enters invalid credentials')
def enter_invalid_credentials(page):
    page.fill('input[type="email"]', "invalid-email@gmail.com")
    page.click('button:has-text("Next")')
    page.wait_for_selector('input[type="password"]')
    page.fill('input[type="password"]', "invalid-password")
    page.click('button:has-text("Next")')

# Then Step: Verify successful login
@then('the user should be logged in successfully')
def verify_successful_login(page):
    page.wait_for_selector("text=Gmail")  # Adjust according to the page post-login
    assert "Gmail" in page.content()

# Then Step: Verify unsuccessful login
@then('the login attempt should fail')
def verify_unsuccessful_login(page):
    assert page.locator('div:has-text("Wrong password")').is_visible()  # Adjust based on error message
