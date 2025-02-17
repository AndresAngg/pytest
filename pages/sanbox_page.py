from selenium.webdriver.common.by import By
from .base_page import BasePage

class SanboxPage(BasePage):
    BTN_HIDDEN = (By.XPATH, "//button[normalize-space()='Hacé click para generar un ID dinámico y mostrar el elemento oculto']")
    TXT_HIDDEN = (By.XPATH, "//p[@id='hidden-element']")
    ABURRIDO_FIELD = (By.XPATH, "//input[@id='formBasicText']")
    POPUP_BTN = (By.XPATH, "//button[normalize-space()='Mostrar popup']")
    TITLE_POPUP = (By.XPATH, "//div[@id='contained-modal-title-vcenter']")
    DEPORTE_DROPDOWN = (By.ID, "formBasicSelect")
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def navigate_sanbox(self):
        self.navigate_to("https://thefreerangetester.github.io/sandbox-automation-testing/")
        
    def click_btn_hidden(self):
        self.click_element(self.BTN_HIDDEN)
    
    def get_txt_hidden(self):
        return self.wait_element_present(self.TXT_HIDDEN)
    
    def select_check_box(self, param):
        checkbox_locator = (By.XPATH, f"//label[contains(., '{param}')]/preceding-sibling::input[@type='checkbox']")
        self.click_element(checkbox_locator)
    
    def select_radio_button(self, param):
        assert param in ["Si", "No"], "Tiene que ser Si o No"
        checkbox_locator = (By.XPATH, f"//label[contains(., '{param}')]/preceding-sibling::input[@type='radio']")
        self.click_element(checkbox_locator)
    
    def get_options_dropdown_deporte(self):
        return self.get_options_dropdown(self.DEPORTE_DROPDOWN)
        
    def select_dropdown_deporte(self, value):
        self.select_value_for_dropdown(self.DEPORTE_DROPDOWN, value)
    
    def write_aburrido_field(self):
        self.write_field(self.ABURRIDO_FIELD, "Este es un texto de prueba aburrido")
    
    def open_popup(self):
        self.hover_over_element(self.POPUP_BTN)
        self.click_element(self.POPUP_BTN)
        
    def get_btn_pupup(self):
        return self.wait_element_present(self.POPUP_BTN)
    
    def get_title_popup(self):
        return self.get_txt_element(self.TITLE_POPUP).text
    
    def get_value_cell_table(self, fil, col):
        xpath_cell = f"//table[1]/tbody[1]/tr[{fil}]/td[{col}]"
        
        celda = self.wait_element_present((By.XPATH, xpath_cell))
        return celda.text if celda else None