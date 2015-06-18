# -*- coding: UTF-8 -*-
__author__ = 'pmartin'
from selenium.webdriver.support.ui import Select
import time
from base import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class AssetLibrary(BasePage):

	def goAssetLibrary(self):
		#go asset library menu
		return self.driver.find_element_by_xpath('//*[@id="btnConfiguration"]/a').click()

	def getHeaderTitle(self):
		WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.ID,"menuNavigator")))
		return self.driver.find_element_by_id('headerTitle').text

