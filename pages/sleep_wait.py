from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SleepWait:

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
        
        self._elements = self.driver.find_elements(By.CLASS_NAME, value="title")
        self._elements_count = len(self._elements)

    def get_elements_count(self):
        return self._elements_count
