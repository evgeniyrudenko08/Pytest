import requests
import json
import jsonpath
from Lib.RESTAPI import UserModel
import pytest
import allure_pytest

class TestAPI():
    def test_createOfUser(self):
            user = UserModel.User()
            url = "http://users.bugred.ru/tasks/rest/doregister"
            s = json.dumps(user.__dict__)
            request_json = json.loads(s)
            response = requests.post(url,request_json)
            assert str(response) == "<Response [200]>"
            response_json = json.loads(response.text)
            assert response_json['name'] == user.name

    def test_deleteAvatar(self):
            url = "http://users.bugred.ru/tasks/rest/deleteavatar/?email=test780@test50.com"
            response = requests.delete(url)
            response_json = response.status_code
            assert response_json == 200
