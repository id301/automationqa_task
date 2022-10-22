__author__ = 'id301'

class Session:

    def __init__(self, app):
        self.app = app

    def login(self, login, password):
            wd = self.app.wd
            wd.get(f'http://{login}:{password}@{self.app.base_url}')

