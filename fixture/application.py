__author__ = 'id301'

from selenium import webdriver
from fixture.session import Session
from fixture.nominal_div import NominalDiv

class Application:

    def __init__(self, base_url):
        self.wd = webdriver.Chrome()
        self.session = Session(self)
        self.nominal_div = NominalDiv(self)
        self.base_url = base_url


    def destroy(self):
        self.wd.quit()