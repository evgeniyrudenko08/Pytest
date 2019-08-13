import requests
import json
import jsonpath
from Lib.RESTAPI import UserModel
import pytest
import allure_pytest
from pytest import ExitCode

class TestAPI():
    def test_createOfUser(self, caplog):
            user = UserModel.User()
            url = "http://users.bugred.ru/tasks/rest/doregister"
            s = json.dumps(user.__dict__)
            request_json = json.loads(s)           
            response = requests.post(url,request_json)            
            response_json = json.loads(response.text)
            assert (response_json['email'] == user.email), "No user is created"

    def test_deleteAvatar(self):
            url = "http://users.bugred.ru/tasks/rest/deleteavatar/?email=test780@test50.com"
            response = requests.delete(url)
            response_json = response.status_code
            assert response_json == 200