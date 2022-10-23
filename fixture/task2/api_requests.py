__author__ = 'id301'

import requests
from model.js_test_task import JsTestTask


class ApiRequests:

    def __init__(self, config):
        self.base_url = config['baseUrl']
        self.js_test_task_method = config['method']
        self.search_param = config['search']
        self.sort_field_param = config['sort_field']

    def get_products(self, search='', sort_field=''):
        """Метод для отправки запроса на метод  API `js-test-task`"""
        search_text = (self.search_param + search) if search != '' else ''
        sort_field_text = (self.sort_field_param + sort_field) if sort_field else ''
        response = requests.get(f'{self.base_url}{self.js_test_task_method}?{search_text}&{sort_field_text}')
        print(f'{self.base_url}{self.js_test_task_method}?{search_text}&{sort_field_text}')
        lst_models = []
        for product in response.json()['products']:
            lst_models.append(JsTestTask.parse_obj(product))
        return lst_models