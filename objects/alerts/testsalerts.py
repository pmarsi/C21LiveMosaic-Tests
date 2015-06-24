# -*- coding: UTF-8 -*-
__author__ = 'pmartin'
import unittest, xlrd
from ddt import ddt, data, unpack
import os
import sys
import time
from selenium import webdriver
sys.path += ['../login', '../maincontrol', '../common', '../alerts']
from login_object import LoginPage
from alerts_object import Alerts
from main_control_object import MainControl
from backend import BackendCall, get_data

@ddt
class TestAlerts(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.browser = webdriver.Chrome()
		cls.browser.maximize_window()
		cls.browser.implicitly_wait(60)
		cls.homepage = LoginPage(cls.browser)
		cls.homepage.navigate()
		cls.homepage2 = Alerts(cls.browser)
		cls.homepage2.navigate()

	@data(*get_data("/Users/pedromartinsilva/Documents/C21LiveMosaic-Tests/objects/login/LoginData.xls", 0))
	@unpack
	def test_00_loginSuccess(self, username, password, message):
		self.homepage.login(username, password, message)
		#go to stream output menu
		time.sleep(3)
		self.homepage2.goToAlerts()

	def test_01_checkTitle(self):
		print "\nTitle: ", self.homepage2.getTitleAlerts()
		self.assertEqual(self.homepage2.getTitleAlerts(), "Alerts", "Title of the page has been changed")

	def test_02_checkAlertsList(self):
		list_expected = ['Stream', 'Video loss', 'Audio loss', 'Frozen video', 'Silence', 'Subtitles']
		print "\nList of alerts: ", self.homepage2.getAlertsName()
		self.assertEqual(list_expected, self.homepage2.getAlertsName())

	def test_03_checkToleranceList(self):
		#list_expected = [5,10,15,20,30,60,120,300,600]
		print "\nNumber of tolerance options: ", str(len(self.homepage2.getToleranceValue()))
		self.assertEqual(str(len(self.homepage2.getToleranceValue())), '9', 'There are less elements than expected')

	def test_04_checkAlertOffStream(self):
		self.homepage2.getButtonOffStream()
		time.sleep(3)
		self.assertEqual(str(BackendCall('/config/alerts')['data']['stream']['time']), '0', 'fail')
		print "\nTime tolerance: ", str(BackendCall('/config/alerts')['data']['stream']['time'])


	def test_05_checkToleranceValue(self):
		#select an option using select_by_value+
		self.homepage2.getToleranceButton()
		self.homepage2.getToleranceList()[3].click()
		time.sleep(3)
		self.assertEqual(str(BackendCall('/config/alerts')['data']['stream']['time']), '20')

	def test_06_checkAlerts(self):
		for i in range(len(self.homepage2.getCheckAlerts())):
			print i
			self.homepage2.getCheckAlerts()[i].click()
			time.sleep(3)
			print str(BackendCall('/config/alerts')['data']['stream'])
		





	@classmethod
	def tearDownClass(cls):
		cls.browser.close()

if __name__ == "__main__":
	unittest.main(verbosity=2)