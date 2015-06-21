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
		time.sleep(3)
		self.homepage2.goAssetLibrary()


	def test_01_headerTitle(self):
		time.sleep(3)
		self.assertEqual(self.homepage2.getHeaderTitle(), "Asset library", 
					"Asset library "+"!= "+self.homepage2.getHeaderTitle())
		print "\n Header title: ", self.homepage2.getHeaderTitle()
	
	def test_02_checkNavigatorTabs(self):
		list_expected = ['Streams', 'Clips', 'Images']
		self.assertListEqual(list_expected, self.homepage2.getNavigatorTabsList())

	@data(*get_data("/Users/pedromartinsilva/Documents/C21LiveMosaic-Tests/objects/Asset_library/AssetData.xls", 0))
	@unpack
	def test_03_checkNewStream(self, address, name, sheet):
		
		self.homepage2.createNewStream(address, name, sheet)
		#get stream name
		stream_list_before = self.homepage2.getStreamList()
		print "\nStream list: ", stream_list_before

		for i in range(len(BackendCall('/livestreams')['data'])):
			if BackendCall('/livestreams')['data'][i]['name'] == str(name) and BackendCall('/livestreams')['data'][i]['url'] == str(address):
				print "\nNew stream saved in backend: ", str(BackendCall('/livestreams')['data'][i])
				self.assertEqual(str(BackendCall('/livestreams')['data'][i]['name']), 
					str(name), "Different items saved in backend")
				self.assertEqual(str(BackendCall('/livestreams')['data'][i]['url']), 
					str(address), "Different items saved in backend")

		#check if stream is in the list
		for i in range(len(self.homepage2.getStreamList())):
			if self.homepage2.getStreamList()[i].split(' ')[0] == str(name):
				print "\nNew stream saved in frontend: ", self.homepage2.getStreamList()[i].split(' ')
				self.assertEqual(self.homepage2.getStreamList()[i].split(' ')[0], str(name), "fail")
				#select stream
				time.sleep(3)
				self.homepage2.getTable()[i].click()
				time.sleep(2)
				#delete stream
				print "\nDeleting..."
				self.homepage2.deleteStream()
				time.sleep(3)
				#alertify ok
				self.homepage2.alertifyOK()
		#Check stream deleted in frontend
		print "\nStream list: ", self.homepage2.getStreamList()
		self.assertNotEqual(stream_list_before, self.homepage2.getStreamList(), "fail")

		def test_04_editStream(self, name, stream, ):
			#steps:
			#create new stream
			#select stream
			#click edit button
			#change data
			#click button accept
			#compare streams in frontend


	@classmethod
	def tearDownClass(cls):
		cls.browser.close()

if __name__ == "__main__":
	unittest.main(verbosity=2)
