from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementNotVisibleException,
    ElementNotInteractableException,
    NoSuchElementException,
)

def test_eight_components():
    driver = webdriver.Chrome()

    driver.get("https://ecommerce-playground.lambdatest.io/")
    driver.implicitly_wait(3)
    driver.find_element(By.LINK_TEXT, "My account").click()
    driver.implicitly_wait(3)
    value = driver.find_element(By.NAME, "email").is_displayed()
    assert value == True
    # print(len(ls), ls)
    # for i in ls:
    #     print('oi', i)

    # title = driver.title
    # assert title == "Web form"

    # driver.implicitly_wait(0.5)

    # text_box = driver.find_element(by=By.NAME, value="my-text")
    # submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    # text_box.send_keys("Selenium")
    # submit_button.click()

    # message = driver.find_element(by=By.ID, value="message")
    # value = message.text
    # assert value == "Received!"

    driver.quit()


def test_explicitwait():
    driver = webdriver.Chrome()
    driver.get("https://ecommerce-playground.lambdatest.io/")
    driver.find_element(By.LINK_TEXT, "My account").click()
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "email"))
    )
    email_input.send_keys("johndoe@gmail.com")
    email_input.get_property("value") == "johndoe@gmail.com"

    driver.quit()


def test_fluentwait():
    driver = webdriver.Chrome()
    driver.get("https://ecommerce-playground.lambdatest.io/")
    driver.find_element(By.LINK_TEXT, "My account").click()
    password_input = driver.find_element(By.NAME, "password")
    exceptions = [ElementNotVisibleException,
    ElementNotInteractableException,
    NoSuchElementException,]
    WebDriverWait(driver, 10, poll_frequency=2, 
                  ignored_exceptions=exceptions).until(
                      lambda el: password_input.is_displayed()
    )
    passwd = "password"
    password_input.send_keys(passwd)
    assert password_input.get_property("value") == passwd
    driver.quit()