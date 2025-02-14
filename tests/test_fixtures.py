import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.keys import Keys as keys

@pytest.fixture(params=["Comida","Selenium","Cypress"])
def params_browser(request):
    return request.param

@pytest.fixture
def browser():
    serviceEdg = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=serviceEdg)
    driver.get("https://www.google.com")
    yield driver
    driver.quit()

def searchGoogle(browser, params_browser):
    searchField = browser.find_element("name", "q")
    searchField.send_keys(params_browser + keys.ENTER)