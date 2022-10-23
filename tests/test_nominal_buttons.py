__author__ = 'id301'

import allure

@allure.feature('Кнопки с номиналом карты')
def test_nominal_buttons(app_task1):
    with allure.step('Для каждой кнопки с номиналом'):
        for button in app_task1.nominal_div.get_buttons():
            button_value = app_task1.nominal_div.get_button_value(button)
            with allure.step(f'Кнопка с номиналом {button_value}: Нажатие на кнопку'):
                app_task1.nominal_div.click_button(button)
            with allure.step(f'Кнопка с номиналом {button_value}: Сравнение с номиналом в поле "Введите"'):
                assert button_value == app_task1.nominal_div.get_input_value(), f'Значение номинала кнопки {button_value} ' \
                                f'не соответствует номиналу в поле "Введите" {app_task1.nominal_div.get_input_value()}'
            with allure.step(f'Кнопка с номиналом {button_value}: Проверка состояния "активности" кнопки'):
                assert app_task1.nominal_div.is_button_active(button), f'Кнопка с номиналом {button_value} не является активной'