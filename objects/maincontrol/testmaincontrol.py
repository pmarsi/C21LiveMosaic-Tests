# -*- coding: UTF-8 -*-
__author__ = 'pmartin'

import sys
import unittest, xlrd
from ddt import ddt, data, unpack
import os
import time
from selenium import webdriver
sys.path += ['../login', '../common']
from login_object import LoginPage, get_data
from main_control_object import MainControl
from backend import BackendCall

#get all tests from TestLoginTitle

list_expected = ['Control', 'Asset library', 'Stream output', 'Alerts', 'Diagnostics', 'Performance',
				'Logs', 'Users', 'Global settings']

@ddt
class TestMainControl(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.browser = webdriver.Chrome()
		cls.browser.maximize_window()
		cls.browser.implicitly_wait(30)
		cls.homepage = LoginPage(cls.browser)
		cls.homepage.navigate()
		cls.homepage2 = MainControl(cls.browser)
		cls.homepage2.navigate()

	@data(*get_data("/Users/pedromartinsilva/Desktop/objects/login/LoginData.xls", 0))
	@unpack
	def test_00_loginSuccess(self, username, password, message):
		self.homepage.login(username, password, message)

	def test_01_MenuElements(self):
		print "\nActual list: "+str(self.homepage2.get_menu_list())
		print "\nList expected: "+str(list_expected)
		self.assertEqual(self.homepage2.get_menu_list(), list_expected, "Expected 9 elements")

	def test_02_EditorWindow(self):
		#check if editor window is visible
		self.assertNotEqual(BackendCall('/config/screen')['data']['width'], 0, "Editor window fail")

	@classmethod
	def tearDownClass(cls):
		
		cls.browser.close()

if __name__ == '__main__':
	unittest.main(verbosity=2)

