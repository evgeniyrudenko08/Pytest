from selenium.webdriver.common.by import By
from selenium import webdriver
from Lib.Browser.browser import Browser

class MainPage(Browser):
    locators = {
        'search_box': (By.NAME, 'q'),
        'search_button': (By.NAME, 'btnK')
    }

    def search(self, value):
        self.send_keys(value, *self.locators.get('search_box'))
        self.click(*self.locators.get('search_button'))

  
