from selenium.webdriver.common.by import By

class SmartWait():

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://ecommerce-playground.lambdatest.io/")
        self.blog_link = driver.find_element(By.LINK_TEXT, "Blog")

    def click_blog_link(self):
        self.blog_link.click()

    def click_first_post(self):
        self.driver.find_element(By.TAG_NAME, "h4").click()
