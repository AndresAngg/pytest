import pytest
from selenium import webdriver
# from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Edge(service=webdriver.EdgeService(EdgeChromiumDriverManager().install()))
    # driver.implicitly_wait(10)
    driver.get("https://thefreerangetester.github.io/sandbox-automation-testing/")
    yield driver
    driver.quit()


def test_select_checkbox(driver):
    
    # linkResources = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Recursos']"))
    # )
    # linkResources.click()
    # linkSanbox = WebDriverWait(driver, 30).until(
    #     EC.presence_of_element_located((By.XPATH, "//h3[normalize-space()='Automation Sandbox']"))
    # )
    # linkSanbox.click()
    btnAwait = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Hacé click para generar un ID dinámico y mostrar el elemento oculto']"))
    )
    btnAwait.click()
    txtAwait = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[@id='hidden-element']"))
    )
    checkBox1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='checkbox-1']"))
    )
    checkBox1.click()
    
    checkRadio1 = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//label[@for='formRadio1']"))
    )
    checkRadio1.click()
    assert txtAwait.text == "OMG, aparezco después de 3 segundos de haber hecho click en el botón 👻."
    assert txtAwait.is_displayed()
    assert checkRadio1.is_enabled()
    assert checkBox1.is_selected()
    