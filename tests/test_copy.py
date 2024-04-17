import pytest
from selenium.webdriver.common.by import By

# class TestLink:
@pytest.mark.usefixtures("driver")
def test_title(driver):
    """
    Verify click and title of page
    :return: None
    """
    driver.get("https://lambdatest.github.io/sample-todo-app/")
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, "li1").click()
    driver.find_element(By.NAME, "li2").click()
    title = "Sample page - lambdatest.com"
    assert title == driver.title


@pytest.mark.usefixtures("driver")
def test_item( driver):
    """
    Verify item submission
    :return: None
    """
    driver.get("https://lambdatest.github.io/sample-todo-app/")
    sample_text = "Happy Testing at LambdaTest"
    email_text_field = driver.find_element(By.ID, "sampletodotext")
    email_text_field.send_keys(sample_text)
    driver.find_element(By.ID, "addbutton").click()
    li6 = driver.find_element(By.CSS_SELECTOR, "input[name='li6'] + span").text
    assert sample_text == li6
