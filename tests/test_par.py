import pytest
from selene.support.shared import browser
from selene import by


@pytest.fixture(params=["desktop", "mobile"])
def browser_config_param(request):
    if request.param == "desktop":
        browser.config.window_width = 1680
        browser.config.window_height = 900
    elif request.param == "mobile":
        browser.config.window_width = 375
        browser.config.window_height = 667


@pytest.mark.parametrize('browser_config_param', ['desktop'], indirect=True)
def test_git_sing_in_button_work_desktop(browser_config_param):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize('browser_config_param', ['mobile'], indirect=True)
def test_git_sing_in_button_work_mobile(browser_config_param):
    browser.open('https://github.com')
    browser.element(by.link_text("Sign up")).click()
    browser.element(by.link_text("Sign in →")).click()