import time
from selenium import webdriver
import pytest
import requests
from Lib.Pages import Main_Page
from Lib.Browser import browser
from Lib.Core import BaseTest

class TestGoogle():
    search = Main_Page.MainPage()
    def test_search(self):
        self.search.search('ChromeDriver')
        self.search.close()
    


    