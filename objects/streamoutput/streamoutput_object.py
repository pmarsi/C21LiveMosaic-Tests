# -*- coding: UTF-8 -*-
__author__ = 'pmartin'
from selenium.webdriver.support.ui import Select
import time
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
sys.path.append('/Users/pedromartinsilva/Documents/C21LiveMosaic-Tests/objects')
from base import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class StreamOutput(BasePage):

	def goStreamOutputButton(self):
		return self.driver.find_element_by_xpath('//*[@id="btnStreamOutput"]/a').click()

	def getHeaderTitle(self):
		WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.ID,"main-content")))
		return self.driver.find_element_by_xpath('//*[@id="main-container"]/div[1]/h1').text

	def getActiveButton(self):
		return self.driver.find_element_by_id('switch_activeOnRounds')

	def getProtocolsButtons(self):
		return self.driver.find_elements_by_xpath('//*[@id="radioProtocol"]/label')

	def getProtocolList(self):
		protocol_list = []
		protocols = self.getProtocolsButtons()

		for i in range(len(protocols)):
			protocol_list.append(protocols[i].text)

		return protocol_list

	def getAddressURL(self):
		return self.driver.find_element_by_id('txtAddress')

	def fillAddressURL(self, address):
		return self.getAddressURL().send_keys(address)

	def getPort(self):
		return self.driver.find_element_by_id('txtPort')

	def fillPort(self, port):
		return self.getPort().send_keys(port)

	def getButtonRestart(self):
		return self.driver.find_element_by_xpath('//*[@id="frameMosaicStreamoutput"]/div[2]/div[1]/form/div[1]/div[2]/button').click()

	def getWidth(self):
		return self.driver.find_element_by_id('txtWidth')

	def getResolutionWidth(self, width):
		
		return self.getWidth().send_keys(width)

	def getHeigth(self):
		heigth_resolution = self.driver.find_element_by_xpath('//*[@id="labelHeight"]')
		heigth_int = int(heigth_resolution.text.split('x ')[1])
		return heigth_int

	def getCodecButton(self):

		return self.driver.find_elements_by_xpath('//*[@id="radioVideoCodec"]/label')

	def getCodecsList(self):
		list_codecs = []

		codecs = self.getCodecButton()
		for i in range(len(codecs)):

			list_codecs.append(codecs[i].text)

		return list_codecs

	def getLevel1Click(self):
		return self.driver.find_element_by_xpath('//*[@id="frameMosaicStreamoutput"]/div[2]/div[1]/form/div[9]/div/div/ul/li[1]/a').click()

	def clickLevelList(self):
		return self.driver.find_element_by_xpath('//*[@id="frameMosaicStreamoutput"]/div[2]/div[1]/form/div[9]/div/div/button').click()

	def getLevelList(self):
		list_levels = []
		self.clickLevelList()
		time.sleep(3)
		levels = self.driver.find_elements_by_xpath('//*[@id="frameMosaicStreamoutput"]/div[2]/div[1]/form/div[9]/div/div/ul/li')

		for i in range(len(levels)):

			list_levels.append(str(levels[i].text))

		return list_levels

	def getProfileButton(self):
		return self.driver.find_elements_by_xpath('//*[@id="radioProfile"]/label')

	def getProfileList(self):
		list_profiles = []

		profiles = self.getProfileButton()

		for i in range(len(profiles)):
			list_profiles.append(profiles[i].text)

		return list_profiles

	def getAudioCodec(self):
		return self.driver.find_elements_by_xpath('//*[@id="radioAudioCodec"]/label')

	def getAudioCodecList(self):
		list_audio = []

		audio_codec = self.getAudioCodec()

		for i in range(len(audio_codec)):
			list_audio.append(audio_codec[i].text)

		return list_audio
