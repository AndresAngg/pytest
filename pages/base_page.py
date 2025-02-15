from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        
    def navigate_to(self, url):
        self.driver.get(url)
        
    def wait_element_present(self, locator, timeout=10):
        try:    
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except Exception as e:
            print(f"Elemento no encontrado: {locator}")
            raise e
        
    def click_element(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            ).click()

        except Exception as e:
            print(f"Elemento no cliqueable {locator}")
            raise e
        
    def write_field(self, locator, value):
        self.wait_element_present(locator).send_keys(value)