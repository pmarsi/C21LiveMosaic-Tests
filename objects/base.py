# -*- coding: UTF-8 -*-
__author__ = 'pmartin'
from selenium.webdriver.support.ui import Select
import time


class BasePage(object):
    url = 'http://ofimostest01.cires21.com'

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self.url)