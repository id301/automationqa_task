__author__ = 'id301'

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    def __init__(self, wd, url):
        self.wd = wd
        self.url = url

    def open(self):
        self.wd.get(self.url)

    def open_with_basic_auth(self, login, password):
        self.wd.get(f'http://{login}:{password}@{self.app.base_url}')

    def find_element(self, locator, time):
        return WebDriverWait(self.wd, time).until(EC.presence_of_element_located(locator),
                                                  message=f'Element with locator {locator} not found')

    def find_elements(self, locator, time):
        return WebDriverWait(self.wd, time).until(EC.presence_of_all_elements_located(locator),
                                                  message=f'Elements with locator {locator} not found')