from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FluentWait:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://ecommerce-playground.lambdatest.io/")

        value = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "nav-item"))
        )
        if value == True:
            print("Page Load Completed")
        else:
            raise ElementNotVisibleException
        
        self._my_account = self.driver.find_element(By.LINK_TEXT, "My account")
        self._password_input = driver.find_element(By.NAME, "password")

    def click_my_account(self):
        self._my_account.click()

    def get_password_input(self):
        return self._password_input
