# -*- coding: UTF-8 -*-
__author__ = 'pmartin'
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from base import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import sys
sys.path += ['../login', '../maincontrol', '../common']
from backend import get_data

class Alerts(BasePage):

	def goToAlerts(self):
		return self.driver.find_element_by_xpath('//*[@id="btnAlerts"]/a/span[2]').click()
	#get title
	def getTitleAlerts(self):
		return self.driver.find_element_by_id('headerTitle').text

	def getListAlerts(self):
		return self.driver.find_elements_by_xpath('//*[@id="tbodyAlerts"]/tr')

	def getAlertsName(self):
		list_alerts = []
		#alerts_name = []
		alerts = self.getListAlerts()
		for i in range(len(alerts)):
			list_alerts.append(alerts[i].text.split('\n')[0])

		return list_alerts

	def getToleranceValue(self):
		tolerance_list = []
		select_tolerance = Select(self.driver.find_element_by_xpath('//*[@id="radiodropdownstream"]/select'))
		for i in range(len(select_tolerance.options)):
			tolerance_list.append(str(select_tolerance.options[i].text))

		return tolerance_list

	def getToleranceButton(self):
		return self.driver.find_element_by_xpath('//*[@id="radiodropdownstream"]/div/button').click()

	def getToleranceList(self):
		return self.driver.find_elements_by_xpath('//*[@id="radiodropdownstream"]/div/ul/li/a')

	def selectToleranceValue(self, value):
		select_tolerance = Select(self.driver.find_element_by_xpath('//*[@id="radiodropdownstream"]/select'))
		return select_tolerance.select_by_index(value)

	def getButtonOffStream(self):
		return self.driver.find_element_by_xpath('//*[@id="radiodropdownstream"]/button').click()

	def getCheckAlerts(self):
		return self.driver.find_elements_by_xpath('//*[@id="tbodyAlerts"]/tr[1]/td')