__author__ = 'id301'

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, wd, url):
        self.wd = wd
        self.url = url

    def open(self):
        """Открытие страницы"""
        self.wd.get(self.url)

    def open_with_basic_auth(self, login, password):
        """Открытие страницы с basic auth"""
        self.wd.get(f'http://{login}:{password}@{self.url}')

    def click_button(self, button):
        """Нажатие на переданную кнопку"""
        button.click()

    def find_element(self, locator, time=5):
        """Обертка для поиска одного элемента с явным ожиданием"""
        return WebDriverWait(self.wd, time).until(EC.presence_of_element_located(locator),
                                                  message=f'Element with locator {locator} not found')

    def find_elements(self, locator, time=5):
        """Обертка для поиска нескольких элементов с явным ожиданием"""
        return WebDriverWait(self.wd, time).until(EC.presence_of_all_elements_located(locator),
                                                  message=f'Elements with locator {locator} not found')