import time
from selenium import webdriver
import pytest
import requests
from Lib.Pages import Main_Page
from Lib.Browser import browser

class TestGoogle():
    search = Main_Page.MainPage()

    def test_search(self, tearDown):
        self.search.search('ChromeDriver')
    
    @pytest.fixture()
    def tearDown(self):
        yield 
        self.search.close()
    