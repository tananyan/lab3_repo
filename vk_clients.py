from base import *
from exceptions import *
from datetime import datetime
import requests


class GettingID(BaseClient):
    v = 5.58
    user_id = None

    def __init__(self, username):
        super().__init__('https://api.vk.com/method/', 'users.get', 'GET')
        self.user_id = username

    def get_params(self):
        return {'user_ids': self.user_id, 'v': self.v}

    def _get_data(self, method, http_method):
        r = requests.get(self.generate_url(method), self.get_params())
        return self.response_handler(r)

    def response_handler(self, response):
        res_dic = response.json()
        if not res_dic.get('error') is None:
            err = res_dic.get('error')
            err_msg = err.get('error_msg')
            raise API_Exception(err_msg)
        else:
            return res_dic.get('response')[0]


class GettingFriends(BaseClient):
    user_id = None
    fields = 'bdate'
    v = 5.68

    def __init__(self, user_id):
        super().__init__('https://api.vk.com/method/', 'friends.get', 'GET')
        self.user_id = user_id

    def get_params(self):
        return {'user_id': self.user_id, 'v': self.v, 'fields': self.fields}

    def _get_data(self, method, http_method):
        r = requests.get(self.generate_url(method), self.get_params())
        return self.response_handler(r)

    def response_handler(self, response):
        res_dic = response.json()
        if not res_dic.get('error') is None:
            err = res_dic.get('error')
            err_msg = err.get('error_msg')
            raise API_Exception(err_msg)
        else:
            return res_dic.get('response').get('items')