import unittest
from selenium import webdriver
from framework.browser_engine import  BrowserEngine
s=BrowserEngine()
class BaseTestCase(unittest.TestCase ):
    def setUp(self):
        self.driver=s.open_browser()
    def tearDown(self):
        self.driver=s.quit_browser()

