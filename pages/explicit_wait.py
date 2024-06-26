from selenium.webdriver.common.by import By

class ExplicitWait:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://ecommerce-playground.lambdatest.io/")

        # Ensure complete page load
        driver.set_page_load_timeout(10)

        self._my_account = self.driver.find_element(By.LINK_TEXT, "My account")

    def click_my_account(self):
        self._my_account.click()

    def get_submit_button(self):
        return self.driver.find_element(By.XPATH, "//input[@type='submit']")
