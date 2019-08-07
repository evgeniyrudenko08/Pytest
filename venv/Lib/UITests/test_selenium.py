import time
from selenium import webdriver
import pytest
import requests
#from Lib.UITests import Selene

class TestGoogle():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome( r'C:\Users\evgeniy.rudenko\bin\chromedriver.exe' )
        driver.implicitly_wait(3)
        driver.maximize_window()
        yield
        driver.quit()
        print( "Test Completed" )

    def test_search(self, test_setup):
        driver.get('http://www.google.com')
        assert "Google" in driver.title
        search_box = driver.find_element_by_name('q')
        search_box.send_keys('ChromeDriver')
        search_box.submit()




