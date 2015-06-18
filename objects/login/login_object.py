# -*- coding: UTF-8 -*-
__author__ = 'pmartin'
from selenium.webdriver.support.ui import Select
import sys
sys.path.append('/Users/pedromartinsilva/Documents/C21LiveMosaic-Tests/objects')
from base import BasePage
import time


class LoginPage(BasePage):


	def getTitle(self):
		return self.driver.title

	def getTitleWelcome(self):
		return self.driver.find_element_by_css_selector('h1.title').text

	def getImageWelcome(self):
		return self.driver.find_element_by_css_selector('img.screenshot')

	def getDescriptionWelcome(self):
		return self.driver.find_element_by_css_selector('p.description').text

	def getUsername(self):
		return self.driver.find_element_by_id('txtLoginUsername')

	def getPassword(self):
		return self.driver.find_element_by_id('txtLoginPassword')

	def fillUsername(self, username):
		return self.getUsername().send_keys(username)

	def fillPassword(self, password):
		return self.getPassword().send_keys(password)

	def getSubmitButton(self):
		return self.driver.find_element_by_id('btnLogin').click()

	def getAlertError(self):
		return self.driver.find_element_by_class_name('alertify-message').is_displayed()

	def getAlertButton(self):
		return self.driver.find_element_by_xpath('//*[@id="alertify-ok"]').click()
	
	#exception, add a button of other page, but I need it


	def login(self, username, password, data=None):
		self.fillUsername(username)
		self.fillPassword(password)
		self.getSubmitButton()
		time.sleep(1)
		return self.getTitle()

