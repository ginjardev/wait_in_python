import pytest
from pages.fluent_wait import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (
    ElementNotVisibleException,
    ElementNotInteractableException,
    NoSuchElementException,
)


@pytest.mark.usefixtures("driver")
def test_fluent_wait(driver):
    fluent_wait = FluentWait(driver)
    fluent_wait.click_my_account()
    password_input = fluent_wait.get_password_input()
    
	# exceptions you want to ignore quietly
    exceptions = [
        ElementNotVisibleException,
        ElementNotInteractableException,
        NoSuchElementException,
    ]
    # fluent wait method involves providing
    # arguments for poll_frequency and ignored_exceptions
    WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=exceptions).until(
        lambda el: password_input.is_displayed()
    )
    
    my_password = "password"
    password_input.send_keys(my_password)
    assert password_input.get_property("value") == my_password, f"Expected password value to equal {my_password}"
