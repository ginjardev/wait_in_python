import pytest
from pages.explicit_wait import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.mark.usefixtures("driver")
def test_explicit_wait(driver):
    explicit_wait = ExplicitWait(driver)
    explicit_wait.click_my_account()
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "email"))
    )
    email = "jondoe@gmail.com"
    email_input.send_keys()
    assert email_input.get_property("value") == email
    
