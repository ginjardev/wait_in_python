import pytest
from pages.explicit_wait import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("driver")
def test_explicit_wait(driver):
    explicit_wait = ExplicitWait(driver)
    explicit_wait.click_my_account()

    # explicit wait method 
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "email"))
    )

    email = "jondoe@gmail.com"
    email_input.send_keys()
    assert email_input.get_property("value") == email, f"Expected email value to equal {email}"


@pytest.mark.usefixtures("driver")
def test_explicit_wait_for_button(driver):
    explicit_wait = ExplicitWait(driver)
    explicit_wait.click_my_account()

    # explicit wait
    button_status = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']"))
    )

    assert button_status == True, f"Expected {button_status} to be True"
