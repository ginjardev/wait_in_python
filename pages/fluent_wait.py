from selenium.webdriver.common.by import By

class FluentWait:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://ecommerce-playground.lambdatest.io/")

        # Ensure page load complete
        driver.set_page_load_timeout(10)
        self._my_account = self.driver.find_element(By.LINK_TEXT, "My account")

    def click_my_account(self):
        self._my_account.click()

    def get_password_input(self):
        return self.driver.find_element(By.NAME, "password")
