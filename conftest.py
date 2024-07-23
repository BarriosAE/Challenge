import pytest
from playwright.sync_api import Browser, sync_playwright
import allure

@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser: Browser):
    page = browser.new_page()
    yield page
    page.close()
