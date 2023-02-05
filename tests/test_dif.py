import pytest
from selene.support.shared import browser
from selene import by


@pytest.fixture
def desktop_s():
    browser.config.window_height = 900
    browser.config.window_width = 1680


@pytest.fixture
def mobile_s():
    browser.config.window_width = 375
    browser.config.window_height = 667


def test_git_sing_in_button_work_desktop(desktop_s):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_git_sing_in_button_work_mobile(mobile_s):
    browser.open('https://github.com')
    browser.element(by.link_text("Sign up")).click()
    browser.element(by.link_text("Sign in →")).click()
