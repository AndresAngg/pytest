from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

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
            print(f"Elemento no encontrado o cliqueable {locator}")
            raise e
        
    def hover_over_element(self, locator):
        element = self.wait_element_present(locator)
        ActionChains(self.driver).move_to_element(element).perform()
        
    def write_field(self, locator, value):
       element = self.wait_element_present(locator)
       element.clear()
       element.send_keys(value)
    
    def select_value_for_dropdown(self, locator, value):
        dropdownField = Select(self.wait_element_present(locator))
        dropdownField.select_by_visible_text(value)
        
    def select_index_for_dropdown(self, locator, index):
        dropdownnField = Select(self.wait_element_present(locator))
        dropdownnField.select_by_index(index)
        
    def get_options_dropdown(self, locator):
        dropdown = Select(self.wait_element_present(locator))
        return [option.text for option in dropdown.options]
    
    def get_txt_element(self, locator):
        return self.wait_element_present(locator)
    
    def reload_page(self):
        self.driver.refresh()