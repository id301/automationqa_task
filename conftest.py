__author__ = 'id301'

import pytest
import json
import os.path
from fixture.task1.application import Application


@pytest.fixture
def app_task1(request):
    config = load_confing_task1()
    fixture = Application(config['baseUrl'])
    fixture.session.login(config['login'], config['password'])
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def load_confing_task1():
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config_task1.json')
    with open(config_file) as f:
        config = json.load(f)
    return config