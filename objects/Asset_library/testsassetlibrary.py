# -*- coding: UTF-8 -*-
__author__ = 'pmartin'
import unittest, xlrd
from ddt import ddt, data, unpack
import os
import sys
import time
from selenium import webdriver
sys.path += ['../login', '../maincontrol', '../common']
from login_object import LoginPage
from asset_library_object import StreamOutput
from main_control_object import MainControl
from backend import BackendCall, get_data



@ddt
class TestAssetLibrary(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.browser = webdriver.Chrome()
		cls.browser.maximize_window()
		cls.browser.implicitly_wait(30)
		cls.homepage = LoginPage(cls.browser)
		cls.homepage.navigate()
		cls.homepage2 =StreamOutput(cls.browser)
		cls.homepage2.navigate()
		cls.homepage3 = MainControl(cls.browser)
		cls.homepage3.navigate()

	@data(*get_data("/Users/pedromartinsilva/Documents/C21LiveMosaic-Tests/objects/login/LoginData.xls", 0))
	@unpack
	def test_00_loginSuccess(self, username, password, message):
		self.homepage.login(username, password, message)
		#go to stream output menu
		self.homepage2.goAssetLibrary()

	def test_01_headerTitle(self):
		self.assertEqual(self.homepage2.getHeaderTitle(), "Asset library", "Title is different")
		print "\n Header title: ", self.homepage2.getHeaderTitle()
