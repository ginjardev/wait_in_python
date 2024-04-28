import pytest
from pages.smartwait import *

@pytest.mark.usefixtures("driver")
def test_blog_navigation(driver):
	smartwait = SmartWait(driver)
	smartwait.click_blog_link()
	smartwait.click_first_post()
	assert "amet volutpat" in driver.title, "Expected 'amet volutpat' in title"

    

