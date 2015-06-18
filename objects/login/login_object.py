# -*- coding: UTF-8 -*-
__author__ = 'pmartin'
from selenium.webdriver.support.ui import Select
import time
import xlrd

#define get_data function

def get_data(file_name, sheet):
	# create an empty list to store rows
	rows = []
	#open the specified Excel spreadsheet as workbook
	book = xlrd.open_workbook(file_name)
	#get the first sheet
	sheet = book.sheet_by_index(sheet)
	#iterate through the sheet and get data from rows in list
	for i in range(1, sheet.nrows):
		rows.append(list(sheet.row_values(i, 0, sheet.ncols)))

	return rows

class BasePage(object):
    url = 'http://ofimostest01.cires21.com'

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self.url)


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

