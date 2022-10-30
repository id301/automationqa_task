__author__ = 'id301'

import pytest
import json
import os.path
from selenium import webdriver
from task2.api_requests import ApiRequests
from task1.utils import Session


@pytest.fixture(scope='session')
def browser():
    wd = webdriver.Chrome()
    yield wd
    wd.quit()

@pytest.fixture(scope='session')
def session():
    return Session()


@pytest.fixture(scope='session')
def setup_task2():
    config = load_confing_task2()
    fixture = ApiRequests(config)
    return fixture

def load_confing_task2():
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'task2/config_task2.json')
    with open(config_file) as f:
        config = json.load(f)
    return config