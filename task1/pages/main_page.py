__author__ = 'id301'

from .base_page import BasePage
from .locators import MainPageLocators
import allure

class MainPage(BasePage):

    def get_nominal_buttons(self):
        """Получение списка кнопок с номиналом"""
        return self.find_elements(MainPageLocators.NOMINAL_BUTTONS)

    def click_every_button(self, buttons_list):
        """Нажатие на каждую кнопку в переданном списке"""
        for button in buttons_list:
            with allure.step(f'Кнопка с номиналом {self.get_nominal_button_value(button)}: Нажатие на кнопку'):
                self.click_button(button)

    def get_nominal_button_value(self, button):
        """Получение номинала кнопки"""
        return button.text

    def get_nominal_input_value(self):
        """Получение номинала в инпуте"""
        return self.find_element(MainPageLocators.NOMINAL_INPUT).get_attribute("value")

    def check_input_equals_nominal_button(self):
        """Проверка номинала в инпуте, сравнение со значением номинала в активной кнопке"""
        button = self.find_element(MainPageLocators.ACTIVE_NOMINAL_BUTTON)
        button_value = self.get_nominal_button_value(button)
        input_value = self.get_nominal_input_value()
        assert input_value == button_value, f'Значение номинала кнопки {button_value} не соответствует номиналу' \
                                            f' в поле "Введите" - {input_value}'

    def check_is_button_active(self, button):
        """Проверка того, что переданная кнопка активна"""
        assert button == self.find_element(MainPageLocators.ACTIVE_NOMINAL_BUTTON), \
            f'Кнопка с номиналом {self.get_nominal_button_value(button)} не является активной'