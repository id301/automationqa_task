__author__ = 'id301'

import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application('qa.digift.ru/')
    fixture.session.login('HR', 'test')
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
