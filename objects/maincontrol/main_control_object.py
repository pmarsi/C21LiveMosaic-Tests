# -*- coding: UTF-8 -*-
__author__ = 'pmartin'
from selenium.webdriver.support.ui import Select


class BasePage(object):
    url = 'http://ofimostest01.cires21.com'

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self.url)

class MainControl(BasePage):

	def get_menu_list(self):
		#create empty list to add the elements
		menu_list = []

		#get menu elements
		items = self.driver.find_elements_by_xpath('//*[@id="menus"]/div/ul/li')

		for i in range(len(items)):
			menu_list.append(items[i].text)

		return menu_list

	def get_editor_window(self):
		
		return self.driver.find_element_by_id('editor-window')

	def getButtonControl(self):

		return self.driver.find_element_by_xpath('//*[@id="btnControl"]/a/span[2]').click()

	def settingsButtonControl(self):

		return self.driver.find_element_by_xpath('//*[@id="btnSettings"]/span').click()

	def screenWeigth(self):
		weigth = self.driver.find_element_by_id('spanScreenWidth').text
		return weigth

	def screenHeigth(self):
		heigth = self.driver.find_element_by_id('spanScreenHeight').text
		return heigth

	def getCancelButton(self):
		return self.driver.find_element_by_xpath('//*[@id="add-settings-modal"]/div/div/div[3]/div[2]/button[2]').click()

	def getExitButton(self):
		return self.driver.find_element_by_xpath('//*[@id="btnLogout"]/a').click()

