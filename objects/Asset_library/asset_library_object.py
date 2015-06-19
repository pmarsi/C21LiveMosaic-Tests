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

	def getNavigatorTabs(self):
		return self.driver.find_elements_by_xpath('//*[@id="menuNavigator"]/li')

	def getNavigatorTabsList(self):
		list_tabs = []

		tabs = self.getNavigatorTabs()

		for i in range(len(tabs)):
			list_tabs.append(tabs[i].text)

		return list_tabs

	def getStreamItem(self, item):
		return self.getNavigatorTabs()[int(item)].click()

	def clickAddStreamButton(self):
		return self.driver.find_element_by_xpath('//*[@id="btnAdd"]').click()

	def getTitleAddStreamPage(self):
		return self.driver.find_element_by_xpath('//*[@id="load-stream-title"]').text

	def fillAddressURL(self, address):
		return self.driver.find_element_by_xpath('//*[@id="sourceURLInput"]').send_keys(address)

	def fillName(self, name):
		return self.driver.find_element_by_xpath('//*[@id="nameInput"]').send_keys(name)

	def getAspectRatioItems(self):
		return self.driver.find_elements_by_xpath('//*[@id="radioAspectratio"]/label')

	def getAcceptButton(self):
		return self.driver.find_element_by_id('btnAccept').click()

	def getStreamList(self):
		list_streams = []
		time.sleep(3)
		streams = self.driver.find_elements_by_xpath('//*[@id="tbodyStreams"]/tr')

		for i in range(len(streams)):
			list_streams.append(streams[i].text)

		return list_streams

	def getTable(self):
		return self.driver.find_elements_by_xpath('//*[@id="tbodyStreams"]/tr')

	def deleteStream(self):
		return self.driver.find_element_by_xpath('//*[@id="frameMosaicAsset"]/div[2]/div[1]/div[3]/button').click()

	def alertifyOK(self):
		return self.driver.find_element_by_id('alertify-ok').click()
	

