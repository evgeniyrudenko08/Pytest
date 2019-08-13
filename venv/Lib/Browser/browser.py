import time
from selenium import webdriver
import pytest
import requests
import os
import time
from selenium import webdriver
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class Browser(object):
    _instance = None
    driver = None

    @classmethod
    def __init__(cls):
        if not cls.driver:
            cls.driver = webdriver.Chrome(r'C:\Users\evgeniy.rudenko\bin\chromedriver.exe')
            cls.driver.implicitly_wait(3)
            cls.driver.set_page_load_timeout(15)
            cls.driver.get('http://www.google.com')

    @classmethod
    def close(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None
        
    def get_driver(self):
        return self.driver

    def get(self, url):
        self.driver.get(url)

    def refresh(self):
        self.driver.refresh()

    def delete_all_cookies(self):
        self.driver.delete_all_cookies()

    def title(self):
        return self.driver.title

    # CLICK:
    def click(self, *locator):
        try:
            self.driver.find_element(*locator).click()
        except WebDriverException as e:
            if 'Other element would receive the click' in e.msg:
                time.sleep(3)
                self.driver.find_element(*locator).click()

    # SEND KEYS
    def send_keys(self, value='', *locator):
        self.driver.find_element(*locator).send_keys(value)
