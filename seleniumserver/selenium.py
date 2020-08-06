from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def get_driver(selenium_grid_url="http://localhost:4445/wd/hub"):
    capabilities = DesiredCapabilities.CHROME.copy()
    driver = webdriver.Remote(desired_capabilities=capabilities,
                              command_executor=selenium_grid_url)
    return driver
