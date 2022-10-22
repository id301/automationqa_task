__author__ = 'id301'

import pytest
import json
import os.path
from fixture.application import Application


@pytest.fixture
def app(request):
    config = load_confing()
    fixture = Application(config['baseUrl'])
    fixture.session.login(config['login'], config['password'])
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def load_confing():
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
    with open(config_file) as f:
        config = json.load(f)
    return config