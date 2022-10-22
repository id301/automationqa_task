__author__ = 'id301'

def test_nominal_buttons(app):
    for button in app.nominal_div.get_buttons():
        app.nominal_div.click_button(button)
        assert app.nominal_div.get_button_value(button) == app.nominal_div.get_input_value()
        assert app.nominal_div.is_button_active(button)