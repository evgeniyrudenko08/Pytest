import time
from selenium import webdriver
import pytest
import requests
from Lib.Pages import Main_Page
from Lib.Browser.browser import Browser

class BaseTest(Browser):
    def test_setup(self):
        global driver
        yield
        self.close()

    