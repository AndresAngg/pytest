import pytest
from pages.sanbox_page import SanboxPage

def test_click_btn_hidden(sanbox_page):
    sanbox_page.click_btn_hidden()
    assert sanbox_page.get_txt_hidden().is_displayed()
    
    sanbox_page.select_check_box()