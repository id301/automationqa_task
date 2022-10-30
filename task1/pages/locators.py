__author__ = 'id301'

from selenium.webdriver.common.by import By


class MainPageLocators():
    NOMINAL_BUTTONS = (By.CSS_SELECTOR, 'button.par-options__button')
    ACTIVE_NOMINAL_BUTTON = (By.CSS_SELECTOR, 'button.par-options__button.par-options__button--active')
    NOMINAL_INPUT = (By.CSS_SELECTOR, '#range-value-input')