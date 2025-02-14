import pytest
from selenium import webdriver
# from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = webdriver.EdgeService(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

@pytest.mark.Navigation
def navigation_to():
    driver.get("https://www.freerangetesters.com/")
    driver.find_element(By.XPATH, "//a[@class='sc-hzvwrc tJYrK sc-fkSzgi sc-hUiJjc dOXKtQ eEDazS'][normalize-space()='Cursos']").click()
    driver.find_element(By.XPATH, "//h3[normalize-space()='Introducción al Testing de Software']").click()
    driver.find_element(By.XPATH, "//a[@class='sc-dODueM iZnoyb']").click()
    btn = driver.find_element(By.XPATH, "//div[@data-toggle='tooltip']")
    assert btn.is_enabled()
