__author__ = 'id301'

from selenium.webdriver.common.by import By

class NominalDiv:

    def __init__(self, app):
        self.app = app


    def get_buttons(self):
        """Получение списка кнопок с номиналом"""
        wd = self.app.wd
        lst = []
        lst += wd.find_elements(By.CLASS_NAME, 'par-options__button')
        lst += wd.find_elements(By.CLASS_NAME, 'par-options__button par-options__button--active')
        return lst

    def click_button(self, button):
        """Нажатие на переданную кнопку button с номиналом"""
        button.click()

    def get_button_value(self, button):
        """Получение номинала переданной кнопки button"""
        return button.text

    def get_input_value(self):
        """Получение номинала из поля ввода"""
        wd = self.app.wd
        input_value = wd.find_element(By.ID, 'range-value-input').get_attribute("value")
        return input_value

    def is_button_active(self, button):
        """Возвращает True, если переданная кнопка button активна, и False - в обратном случае"""
        return True if button.get_attribute("class") == 'par-options__button par-options__button--active' else False