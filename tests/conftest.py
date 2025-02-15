import pytest
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from pages.sanbox_page import SanboxPage

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Edge(service=webdriver.EdgeService(EdgeChromiumDriverManager().install()))
    # driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def sanbox_page(browser):
    return SanboxPage(browser)