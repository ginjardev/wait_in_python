import pytest
from pages.sleep_wait import *
import time


@pytest.mark.usefixtures("driver")
def test_sleep_wait(driver):
    class_title_elements_count = 128
    elements_count = SleepWait(driver)

    # Python sleep method used to wait
    time.sleep(5) 

    count = elements_count.get_elements_count()
    assert count == class_title_elements_count\
    , f"Expected {count} to be {class_title_elements_count}"
