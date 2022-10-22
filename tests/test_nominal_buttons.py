__author__ = 'id301'

import allure

@allure.feature('Кнопки с номиналом карты')
def test_nominal_buttons(app):
    with allure.step('Для каждой кнопки с номиналом'):
        for button in app.nominal_div.get_buttons():
            button_value = app.nominal_div.get_button_value(button)
            with allure.step(f'Кнопка с номиналом {button_value}: Нажатие на кнопку'):
                app.nominal_div.click_button(button)
            with allure.step(f'Кнопка с номиналом {button_value}: Сравнение с номиналом в поле "Введите"'):
                assert button_value == app.nominal_div.get_input_value()
            with allure.step(f'Кнопка с номиналом {button_value}: Проверка состояния "активности" кнопки'):
                assert app.nominal_div.is_button_active(button)