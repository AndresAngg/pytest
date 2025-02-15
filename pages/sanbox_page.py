from selenium.webdriver.common.by import By
from .base_page import BasePage

class SanboxPage(BasePage):
    BTN_HIDDEN = (By.XPATH, "//button[normalize-space()='Hacé click para generar un ID dinámico y mostrar el elemento oculto']")
    TXT_HIDDEN = (By.XPATH, "//p[@id='hidden-element']")
    CHECK_BOX = (By.XPATH, "//input[@id='checkbox-1']")
    ABURRIDO_FIELD = (By.XPATH, "//input[@id='formBasicText']")
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def navigate_sanbox(self):
        self.navigate_to("https://thefreerangetester.github.io/sandbox-automation-testing/")
        
    def click_btn_hidden(self):
        self.click_element(self.BTN_HIDDEN)
    
    def get_txt_hidden(self):
        return self.wait_element_present(self.TXT_HIDDEN)
    
    def select_check_box(self):
        self.click_element(self.CHECK_BOX)
    
    def write_aburrido_field(self):
        self.write_field(self.ABURRIDO_FIELD, "Este es un texto de prueba aburrido 👻.")