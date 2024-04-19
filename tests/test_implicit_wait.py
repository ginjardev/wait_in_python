import pytest
from pages.implicit_wait import *


@pytest.mark.usefixtures("driver")
def test_implicit_wait(driver):
    implicit_wait = ImplicitWait(driver)
    implicit_wait.click_my_account()
    
    # driver implicit wait method
    driver.implicitly_wait(3)
    
    is_email_displayed = implicit_wait.is_email_displayed()
    assert is_email_displayed == True, f"Expected {is_email_displayed} to equal True"
