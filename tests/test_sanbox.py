import pytest

@pytest.mark.sanbox
def test_click_btn_hidden(sanbox_page):
    sanbox_page.navigate_sanbox()
    sanbox_page.click_btn_hidden()
    assert sanbox_page.get_txt_hidden().is_displayed()

@pytest.mark.sanbox
def test_select_check_box_and_radio(sanbox_page):
    sanbox_page.select_check_box("Pasta")
    sanbox_page.select_check_box("Hamburguesa")
    sanbox_page.select_check_box("Torta")
    sanbox_page.select_radio_button("Si")
    
@pytest.mark.sanbox
def test_write_field_aburrido(sanbox_page):
    sanbox_page.write_aburrido_field()
    
@pytest.mark.sanbox
def test_validate_dropdown_deporte(sanbox_page):
    options = sanbox_page.get_options_dropdown_deporte()
    options_expected = ["Seleccioná un deporte", "Fútbol", "Tennis", "Basketball"]
    
    assert all (
        option in options for option in options_expected
    ), "Faltan opciones o no concuerdan con las esperadas"
    sanbox_page.select_dropdown_deporte("Fútbol")
    
@pytest.mark.sanbox
def test_popup(sanbox_page):
    sanbox_page.open_popup()
    tiitle_expected = "Popup de ejemplo"
    assert tiitle_expected in sanbox_page.get_title_popup()
    
@pytest.mark.sanboxtable
def test_value_cell_table_change(sanbox_page):
    sanbox_page.navigate_sanbox()
    value_cell_antes = sanbox_page.get_value_cell_table(2,1)
    sanbox_page.reload_page()
    value_cell_despues = sanbox_page.get_value_cell_table(2,1)
    assert (value_cell_antes != value_cell_despues), f"Los campos son iguales {value_cell_antes} - despues {value_cell_despues}"
    