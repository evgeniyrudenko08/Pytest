import time
from selenium import webdriver
import pytest

class TestSearchInGoogle():
    search = Main_Page.MainPage()
    def test_search(self):
        self.search.search('ChromeDriver')
        self.search.close()