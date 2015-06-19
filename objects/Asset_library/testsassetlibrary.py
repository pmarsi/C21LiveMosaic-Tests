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
from asset_library_object import AssetLibrary
from main_control_object import MainControl
from backend import BackendCall, get_data


@ddt
class TestAssetLibrary(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.browser = webdriver.Chrome()
		cls.browser.maximize_window()
		cls.browser.implicitly_wait(60)
		cls.homepage = LoginPage(cls.browser)
		cls.homepage.navigate()
		cls.homepage2 =AssetLibrary(cls.browser)
		cls.homepage2.navigate()


	@data(*get_data("/Users/pedromartinsilva/Documents/C21LiveMosaic-Tests/objects/login/LoginData.xls", 0))
	@unpack
	def test_00_loginSuccess(self, username, password, message):
		self.homepage.login(username, password, message)
		#go to stream output menu
		self.homepage2.goAssetLibrary()

	'''
	def test_01_headerTitle(self):
		time.sleep(3)
		self.assertEqual(self.homepage2.getHeaderTitle(), "Asset library", 
					"Asset library "+"!= "+self.homepage2.getHeaderTitle())
		print "\n Header title: ", self.homepage2.getHeaderTitle()
	
	'''
	def test_02_checkNavigatorTabs(self):
		time.sleep(4)
		list_expected = ['Streams', 'Clips', 'Images']
		self.assertListEqual(list_expected, self.homepage2.getNavigatorTabsList())

	@data(*get_data("/Users/pedromartinsilva/Documents/C21LiveMosaic-Tests/objects/Asset_library/AssetData.xls", 0))
	@unpack
	def test_03_createNewStream(self, address, name):
		#get len stream list
		self.homepage2.getStreamItem(0)
		#Add stream
		self.homepage2.clickAddStreamButton()
		#fill Address URL
		self.homepage2.fillAddressURL(address)
		#fill Name
		self.homepage2.fillName(name)
		#select aspect ratio
		self.homepage2.getAspectRatioItems()[2].click()
		#accept
		self.homepage2.getAcceptButton()
		#get stream name
		time.sleep(5)
		#check stream configuration in backend
		print str(BackendCall('/livestreams')['data'])
		self.assertEqual(str(BackendCall('/livestreams')['data'][1]['name']), 
			str(name), "Different items saved in backend")
		self.assertEqual(str(BackendCall('/livestreams')['data'][1]['url']), 
			str(address), "Different items saved in backend")
		
		print self.homepage2.getStreamList()

		#check if stream is in the list
		for i in range(len(self.homepage2.getStreamList())):
			if self.homepage2.getStreamList()[i].split(' ')[0] == 'test-selenium':
				self.assertEqual(self.homepage2.getStreamList()[i].split(' ')[0], 'test-selenium', "fail")
				#select stream
				time.sleep(3)
				self.homepage2.getTable()[i].click()
				time.sleep(2)
				#delete stream
				self.homepage2.deleteStream()
				time.sleep(2)
				#alertify ok
				self.homepage2.alertifyOK()




		


	@classmethod
	def tearDownClass(cls):
		cls.browser.close()

if __name__ == "__main__":
	unittest.main(verbosity=2)
