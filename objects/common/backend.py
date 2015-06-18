import unittest
import time
import urllib2
import urlparse
import urllib
import json
import hashlib
import requests
import cookielib
from cookielib import CookieJar
import os
import xlrd


def BackendCall(apifunction):
    urlauth='http://ofimostest01.cires21.com/c21apiv2/security/login'
    urlbase = 'http://ofimostest01.cires21.com/c21apiv2'
    username = 'c21support'
    password = '$21$00support'
    value_crypt = hashlib.sha512(password).hexdigest()
    data = json.dumps({ 'username': username, 'password': value_crypt })
    #OBTENER LA COOKIE
    session = requests.session()
        
    p = session.post(urlauth, data, headers={'Content-Type': 'application/json'} )
        
    cookie = requests.utils.dict_from_cookiejar(session.cookies)
    #print cookie.items()
        
    """formateo la cookie"""
    for par,val in cookie.items():
        cookie_format = "{par}={val}".format(par=par, val=val)

    urlrequest = urlbase+apifunction
    #print urlrequest
    req2 = urllib2.Request(urlrequest)
    req2.add_header('User-Agent', 'python-requests/2.6.2 CPython/2.7.6 Darwin/14.3.0')
    req2.add_header('Cookie', cookie_format)
    req2.add_header('Accept', '*/*')
    response = json.loads(urllib2.urlopen(req2).read())
    return response

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