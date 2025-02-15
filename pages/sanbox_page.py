from selenium.webdriver.common.by import By
from .base_page import BasePage

class SanboxPage(BasePage):
    BTN_HIDDEN = (By.XPATH, "//button[normalize-space()='Hacé click para generar un ID dinámico y mostrar el elemento oculto']")
    TXT_HIDDEN = (By.XPATH, "//p[@id='hidden-element']")
    CHECK_BOX = (By.XPATH, "//input[@id='checkbox-1']")
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def click_btn_hidden(self):
        click_btn_hidden = self.wait_element_present(self.BTN_HIDDEN)
        click_btn_hidden.click()
    
    def get_txt_hidden(self):
        return self.wait_element_present(self.TXT_HIDDEN)
    
    def select_check_box(self):
        checkbox = self.wait_element_present(self.CHECK_BOX)
        checkbox.click()