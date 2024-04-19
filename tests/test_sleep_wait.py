import pytest
from selenium.webdriver.common.by import By
from pages.sleep_wait import *
import time


@pytest.mark.usefixtures("driver")
def test_sleep_wait(driver):
    elements_count = SleepWait(driver)
    time.sleep(5)
    count = elements_count.get_elements_count()
    print(count)
    assert count == 128
