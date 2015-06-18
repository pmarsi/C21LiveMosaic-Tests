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
from streamoutput_object import StreamOutput
from main_control_object import MainControl
from backend import BackendCall, get_data

dir_data = "/Users/pedromartinsilva/Documents/C21LiveMosaic-Tests/objects/streamoutput/Address.xls"

@ddt
class TestStreamOutput(unittest.TestCase):

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
		self.homepage2.goStreamOutputButton()

	def test_01_headerTitle(self):
		time.sleep(3)
		self.assertEqual(self.homepage2.getHeaderTitle(), "Stream output", "Expected Stream output title")
		print "\n Header Title: ", self.homepage2.getHeaderTitle()


	def test_02_streamOutputButton(self):
		#click button on/off
		if self.homepage2.getActiveButton().get_attribute('class') == 'switch btn-group active':
			print "button actived --> switch off"
			self.homepage2.getActiveButton().click()
			#call to backend to get the response
			time.sleep(3)
			self.assertEqual(str(BackendCall('/config/streaming')['data']['enabled']), "False", "Expected enabled == false")
		else:
			print "button not actived --> switch on"
			self.homepage2.getActiveButton().click()
			self.assertEqual(str(BackendCall('/config/streaming')['data']['enabled']), "True", "Expected enabled = true")

	def test_03_listProtocols(self):
		list_expected = ['HTTP', 'UDP', 'RTP']
		#check number of protocols defined
		self.assertEqual(len(self.homepage2.getProtocolList()), 3, "Expected 3 protocols")
		self.assertEqual(self.homepage2.getProtocolList(), list_expected, "Expected the same protocols")

	def test_04_changeProtocol(self):
		#click UDP protocol
		self.homepage2.getProtocolsButtons()[1].click()
		print str(BackendCall('/config/streaming')['data']['protocol'])
		#check the response of backend
		self.assertEqual(str(BackendCall('/config/streaming')['data']['protocol']), 
					"UDP".lower(), "Expected UDP protocol in backend")

	@data(*get_data(dir_data, 0))
	@unpack
	def test_05_changeURL(self, address):
		#clear data from input text
		self.homepage2.getAddressURL().clear()
		#fill input text with new data
		self.homepage2.fillAddressURL(str(address))
		self.homepage2.getButtonRestart()
		time.sleep(4)
		print str(BackendCall('/config/streaming')['data']['address'])
		self.assertEqual(str(BackendCall('/config/streaming')['data']['address']), str(address), 
					"IP address error")

	@data(*get_data(dir_data, 1))
	@unpack
	def test_06_changePort(self, port):
		self.homepage2.getPort().clear()
		time.sleep(3)
		self.homepage2.fillPort(int(port))
		self.homepage2.getButtonRestart()
		time.sleep(3)
		print "\n Element saved in backend: ", str(BackendCall('/config/streaming')['data']['port'])
		self.assertEqual(str(BackendCall('/config/streaming')['data']['port']), str(int(port)), 
				"Port format Incorrect")


	@data(*get_data(dir_data, 2))
	@unpack
	def test_07_changeWidth(self, width):
		#Cleaning of input text
		self.homepage2.getWidth().clear()
		#call function to insert values
		time.sleep(3)
		self.homepage2.getResolutionWidth(int(width))
		self.homepage2.getButtonRestart()
		time.sleep(4)
		print "\n Element inserted in web: ", str(width)
		print "\n Element saved in backend: ", str(BackendCall('/config/streaming')['data']['width'])
		self.assertEqual(str(BackendCall('/config/streaming')['data']['width']), str(int(width)), 
				"Width format incorrect")

	def test_08_checkVideoCodecs(self):
		list_expected = ['H.264', 'MPEG-2', 'MPEG-4']
		time.sleep(3)
		self.assertEqual(self.homepage2.getCodecsList(), list_expected, "Expected same values")

	def test_09_changeVideoCodec(self):
		self.homepage2.getCodecButton()[1].click()
		print str(BackendCall('/config/streaming')['data']['videocodec'])
		self.assertEqual(str(BackendCall('/config/streaming')['data']['videocodec']), 
				"mpgv", "Expected h264 codec in backend")

	
	def test_10_checkH264Levels(self):
		expected_levels = ['1.0', '1.1', '1.2', '1.3', '2.0', '2.1', '2.2', '3.0', '3.1', '3.2', '4.0', '4.1', '4.2', '5.0', '5.1']
		print "\nCurrent list: ", self.homepage2.getLevelList()
		print "\nExpected list: ", expected_levels
		self.assertEqual(len(self.homepage2.getLevelList()), len(expected_levels), "Expected same number of levels")

	def test_11_chageH264Level(self):
		#click to open the list
		self.homepage2.clickLevelList()
		#click one level
		self.homepage2.getLevel1Click()
		time.sleep(3)

		#check the level in backend
		print "\n Level selected: ", str(BackendCall('/config/streaming')['data']['h264options']['level'])
		self.assertEqual(str(BackendCall('/config/streaming')['data']['h264options']['level']), '1.0', "Expected true")

	@data(*get_data(dir_data, 3))
	@unpack
	def test_12_checkVideoProfile(self, indice, profile):
		list_expected = ['Baseline', 'Main', 'High']
		print "\n Current Video profiles: ", self.homepage2.getProfileList()
		print "\n Expected video profiles: ", list_expected

		self.assertEqual(self.homepage2.getProfileList(), list_expected, "Lists are differents: "
				+str(list_expected)+"!="+str(self.homepage2.getProfileList()))
		##########test2##########
		#change VideoProfile
		self.homepage2.getProfileButton()[int(indice)].click()
		self.homepage2.getButtonRestart()
		time.sleep(4)
		print "Element selected in web: ", self.homepage2.getProfileButton()[int(indice)].text
		print "Element saved in backend: ", str(BackendCall('/config/streaming')['data']['h264options']['profile'])
		self.assertEqual(str(BackendCall('/config/streaming')['data']['h264options']['profile']), 
			profile.lower(), "Expected same values")


	def test_13_checkAudioCodec(self):
		codecs_expected = ['AAC', 'MP3']

		self.assertEqual(self.homepage2.getAudioCodecList(), codecs_expected, 
				"Codecs expected and actuals are different")

		#select audio codec
		self.homepage2.getAudioCodec()[0].click()
		self.homepage2.getButtonRestart()
		time.sleep(3)
		print "\n Element selected in web: ", self.homepage2.getAudioCodec()[0].text
		print "\n Element saved in backend: ", str(BackendCall('/config/streaming')['data']['audiocodec'])
		self.assertEqual(str(BackendCall('/config/streaming')['data']['audiocodec']), 'mp4a', 
				'audio codecs are differents')
	


	@classmethod
	def tearDownClass(cls):
		cls.browser.close()

if __name__ == "__main__":
	unittest.main(verbosity=2)