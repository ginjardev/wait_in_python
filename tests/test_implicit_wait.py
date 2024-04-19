import pytest
from pages.implicit_wait import *


@pytest.mark.usefixtures("driver")
def test_implicit_wait(driver):
	implicit_wait = ImplicitWait(driver)
	driver.implicitly_wait(3)
	implicit_wait.click_my_account()
	driver.implicitly_wait(3)
	value = driver.find_element(By.NAME, "email").is_displayed()
	assert value == True

