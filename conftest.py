__author__ = 'id301'

import pytest
import json
import os.path
from selenium import webdriver
from fixture.task2.api_requests import ApiRequests
from utils import Session


@pytest.fixture(scope='session')
def browser():
    wd = webdriver.Chrome()
    yield wd
    wd.quit()

@pytest.fixture(scope='session')
def session():
    return Session()

def load_confing_task1():
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config_task1.json')
    with open(config_file) as f:
        config = json.load(f)
    return config


@pytest.fixture(scope='session')
def setup_task2():
    config = load_confing_task2()
    fixture = ApiRequests(config)
    return fixture

def load_confing_task2():
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config_task2.json')
    with open(config_file) as f:
        config = json.load(f)
    return config