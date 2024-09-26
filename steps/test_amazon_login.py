from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import sync_playwright

# Link the feature file to this test
scenarios('../features/amazon_login.feature')

@given('the user is on the Amazon login page')
def open_amazon_login_page(page):
    page.goto("https://www.amazon.com/ap/signin")
    page.wait_for_load_state()

@when('the user enters valid credentials')
def enter_valid_credentials(page):
    page.fill('input[name="email"]', 'valid-email@example.com')
    page.fill('input[name="password"]', 'valid-password')
    page.click('input#signInSubmit')

@then('the user should be logged in successfully')
def verify_successful_login(page):
    assert "Your Account" in page.content()

@then('take screenshot on failure')
def take_screenshot_on_failure(page):
    # Capture screenshot if there's a failure
    page.screenshot(path='screenshots/failure.png')
