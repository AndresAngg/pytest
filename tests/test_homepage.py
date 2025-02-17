import pytest

def test_navigate_courses(home_page):
    home_page.navigate_home()
    home_page.click_courses_link_nav()