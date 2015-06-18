# -*- coding: UTF-8 -*-
__author__ = 'pmartin'
from selenium.webdriver.support.ui import Select
import time
from base import BasePage


class AssetLibrary(BasePage):

	def goAssetLibrary(self):
		#go asset library menu
		return self.driver.find_element_by_xpath('//*[@id="btnConfiguration"]/a').click()

	def getHeaderTitle(self):

		return self.driver.find_element_by_id('headerTitle').text

