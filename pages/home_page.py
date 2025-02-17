from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    
    LINK_COURSES = (By.XPATH, "//a[normalize-space()='Cursos']")
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def navigate_home(self):
        self.navigate_to("https://www.freerangetesters.com/")
    
    def click_courses_link_nav(self):
        self.click_element(self.LINK_COURSES)