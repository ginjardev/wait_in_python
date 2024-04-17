from os import environ

import pytest
from selenium import webdriver


@pytest.fixture()
def driver(request):
    test_name = request.node.name
    build = environ.get("BUILD", "Sample PY Build")
    tunnel_id = environ.get("TUNNEL", False)
    username = environ.get("LT_USERNAME", None)
    access_key = environ.get("LT_ACCESS_KEY", None)

    selenium_endpoint = "http://{}:{}@hub.lambdatest.com/wd/hub".format(
        username, access_key
    )
    chrome_options = webdriver.ChromeOptions()
    option = {
        "platform": "Windows 10",
        "version": "latest",
        "name": test_name,
        "Build": build,
        "video": True,
        "visual": True,
        "network": True,
        "console": True,
    }
    chrome_options.set_capability("LT:Options", option)
    browser = webdriver.Remote(
        command_executor=selenium_endpoint, options=chrome_options
    )
    yield browser
    def fin(request, browser):
        if request.node.rep_call is not None and request.node.rep_call.failed:
            browser.execute_script("lambda-status=failed")
        else:
            browser.execute_script("lambda-status=passed")
            browser.quit()

    request.addfinalizer(lambda: fin(request, browser))


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # this sets the result as a test attribute for LambdaTest reporting.
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


@pytest.mark.usefixtures("driver")
def test_go(driver):
    driver.get("https://www.selenium.dev/selenium/web/dynamic.html")
    title = driver.title
    print(title)
    # if "Web Form" in title:
    #     set_test_status(driver, "passed", "Title matched")
    # else:
    #     set_test_status(driver, "failed", "Title did not match")
    # except Exception as err:
    #     print("Error:: ", err)
    #     set_test_status(driver, "failed", str(err))
