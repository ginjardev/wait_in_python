from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ImplicitWait:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://ecommerce-playground.lambdatest.io/")

        # Ensure page load complete
        driver.set_page_load_timeout(10)

        self._my_account = self.driver.find_element(By.LINK_TEXT, "My account")

    def click_my_account(self):
        self._my_account.click()

    def is_email_displayed(self):
        return self.driver.find_element(By.NAME, "email").is_displayed()
