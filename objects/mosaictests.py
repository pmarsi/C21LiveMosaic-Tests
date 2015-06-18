import unittest
import HTMLTestRunner
import os
import sys
sys.path += ['login', 'maincontrol', 'streamoutput', 'common']
from testlogin import TestLogin
from testmaincontrol import TestMainControl
from teststreamoutput import TestStreamOutput
dir = os.getcwd()

#Load all tests suites
logintests = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
maincontroltests = unittest.TestLoader().loadTestsFromTestCase(TestMainControl)
streamoutputtests = unittest.TestLoader().loadTestsFromTestCase(TestStreamOutput)

smoke_tests = unittest.TestSuite([logintests, maincontroltests, streamoutputtests])

# open the report file
outfile = open("/Users/pedromartinsilva/Documents/C21LiveMosaic-Tests/objects/mosaictests.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(
            stream = outfile,
            title = "Test Report",
            description = 'Front-end Tests')
# run the suite
runner.run(smoke_tests)
