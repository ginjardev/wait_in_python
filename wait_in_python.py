from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title
print(title)
text_box = driver.find_element(by=By.NAME, value="my-text")
print(text_box)