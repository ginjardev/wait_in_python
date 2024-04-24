import pytest
from pages.explicit_wait import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("driver")
def test_explicit_wait_email_input(driver):
    explicit_wait = ExplicitWait(driver)
    explicit_wait.click_my_account()

    # explicit wait method 
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "email"))
    )

    email = "jondoe@gmail.com"
    email_input.send_keys(email)
    assert email_input.get_property("value") == email, f"Expected email value to equal {email}"


@pytest.mark.usefixtures("driver")
def test_explicit_wait_for_button(driver):
    explicit_wait = ExplicitWait(driver)
    explicit_wait.click_my_account()

    # explicit wait
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']"))
    )
    button = explicit_wait.get_submit_button()
    button_text = button.get_attribute('value')
    assert button_text == "Login", f"Expected {button_text} to be Login"
