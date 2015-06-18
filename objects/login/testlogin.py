# -*- coding: UTF-8 -*-
__author__ = 'pmartin'
import unittest
from ddt import ddt, data, unpack
import os
import sys
import time
from selenium import webdriver
from login_object import LoginPage, get_data
sys.path.append('../maincontrol')
from main_control_object import MainControl


@ddt
class TestLogin(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.browser = webdriver.Chrome()
		cls.browser.maximize_window()
		cls.browser.implicitly_wait(30)
		cls.homepage = LoginPage(cls.browser)
		cls.homepage.navigate()
		cls.homepage2 = MainControl(cls.browser)
		cls.homepage2.navigate()
	
	def test_01_title_login(self):
		self.assertEqual(self.homepage.getTitle(), "Cires21", "Expected true, but false")
		print "\nTitle page login: "+self.homepage.getTitle()

	def test_02_title_welcome(self):
		self.assertEqual(self.homepage.getTitleWelcome(), "Welcome", "Expected true, but "+self.homepage.getTitleWelcome())
		print "\nTitle Welcome is: "+self.homepage.getTitleWelcome()


	def test_03_image_welcome(self):
		img = self.homepage.getImageWelcome().get_attribute('src').split('/')[5]
		self.assertTrue(self.homepage.getImageWelcome().is_displayed(), "Expected true, but imagen isn't display")
		self.assertEqual(img, 'welcome.png', "Expected true, but")
		print "\nName of image file: "+img

	def test_04_description_welcome(self):
		self.assertEqual(self.homepage.getDescriptionWelcome(), 
			"The most advanced solution for live streaming monitoring.", "The description isn't match")
		print "\nText description: "+self.homepage.getDescriptionWelcome()


	@data(*get_data("/Users/pedromartinsilva/Desktop/objects/login/LoginData.xls", 0))
	@unpack
	def test_05_loginSuccess(self, username, password, message):
		title = self.homepage.login(username, password, message)
		print "\ntitle after login: "+title
		self.assertNotEqual(title, "Cires21", "Expected different title")
		self.homepage2.getExitButton()

	@data(*get_data("/Users/pedromartinsilva/Desktop/objects/login/LoginData.xls", 1))
	@unpack
	def test_06_loginFail(self, username, password):
		self.homepage.login(username, password)
		self.assertTrue(self.homepage.getAlertError, "Expected alert login error")
		self.homepage.getAlertButton()
		self.homepage.getUsername().clear()
		self.homepage.getPassword().clear()

	@classmethod
	def tearDownClass(cls):
		
		cls.browser.close()

if __name__ == '__main__':
	unittest.main(verbosity=2)
