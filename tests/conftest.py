import pytest
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FireFoxService
from pages.sanbox_page import SanboxPage
from pages.home_page import HomePage

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="edge",
        help="Type of browser: edge and firefox",
    )
    
@pytest.fixture(scope="session")
def browser(request):
    browser_type = request.config.getoption("--browser").lower()
    if browser_type == "edge":
        driver = webdriver.Edge(service=webdriver.EdgeService(EdgeChromiumDriverManager().install()))
    elif browser_type == "firefox":
        driver = webdriver.Firefox(service=webdriver.FirefoxService(GeckoDriverManager().install()))
        
    # driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def sanbox_page(browser):
    return SanboxPage(browser)

@pytest.fixture
def home_page(browser):
    return HomePage(browser)