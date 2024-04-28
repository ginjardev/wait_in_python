from selenium.webdriver.common.by import By

class SleepWait:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://ecommerce-playground.lambdatest.io/")
        
        self._elements = self.driver.find_elements(By.CLASS_NAME, value="info")
        self._elements_count = len(self._elements)

    def get_elements_count(self):
        return self._elements_count
