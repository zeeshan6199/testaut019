import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

@pytest.fixture(autouse=True)
def _page_defaults(page:Page):
    page.set_default_timeout(10000)
    page.set_default_navigation_timeout(15000)
    yield

@pytest.fixture
def postive_logged_in(page):
    """Return a page that is already logged in."""
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    return page

@pytest.fixture
def negative_logged_in(page):
    """Return a page that is already logged in."""
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("stan", "secret_sauce")
    return page


    