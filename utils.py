import os.path
import json


class Session:

    def __init__(self):
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config_task1.json')
        with open(config_file) as f:
            config = json.load(f)
        self.BASE_URL = config['baseUrl']
        self.LOGIN = config['login']
        self.PASSWORD = config['password']


