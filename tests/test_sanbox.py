import pytest
from pages.sanbox_page import SanboxPage
import time

def test_click_btn_hidden(sanbox_page):
    sanbox_page.navigate_sanbox()
    sanbox_page.click_btn_hidden()
    assert sanbox_page.get_txt_hidden().is_displayed()
    
    sanbox_page.select_check_box()
    sanbox_page.write_aburrido_field()