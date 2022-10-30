__author__ = 'id301'

import allure
from fixture.task1.pages.main_page import MainPage


@allure.feature('Кнопки с номиналом карты')
def test_nominal_buttons(browser, session):
    main_page = MainPage(browser, session.BASE_URL)
    main_page.open_with_basic_auth(session.LOGIN, session.PASSWORD)
    with allure.step('Для каждой кнопки с номиналом'):
        for button in main_page.get_nominal_buttons():
            with allure.step(f'Кнопка с номиналом {main_page.get_nominal_button_value(button)}: Нажатие на кнопку'):
                main_page.click_button(button)
            with allure.step(f'Кнопка с номиналом {main_page.get_nominal_button_value(button)}: Сравнение с номиналом в поле "Введите"'):
                main_page.check_input_equals_nominal_button()
            with allure.step(f'Кнопка с номиналом {main_page.get_nominal_button_value(button)}: Проверка состояния "активности" кнопки'):
                main_page.check_is_button_active(button)