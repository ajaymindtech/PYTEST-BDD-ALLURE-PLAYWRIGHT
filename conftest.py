import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)
            if "allure" in item.funcargs:
                allure.attach.file(screenshot_path, name="screenshot", attachment_type=allure.attachment_type.PNG)
