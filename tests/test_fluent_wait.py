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
	password_input =  driver.find_element(By.NAME, "password")
	exceptions = [ElementNotVisibleException, ElementNotInteractableException, NoSuchElementException]
	WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=exceptions).until(
		lambda el: password_input.is_displayed()
	)
	passwd = "password"
	password_input.send_keys(passwd)
	assert password_input.get_property("value") == passwd
