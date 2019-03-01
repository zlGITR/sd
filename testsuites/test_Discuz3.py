from testsuites .base_testcase import BaseTestCase
from Pageobjects .Discuzbody import  HomePage
import time
import unittest
class Discuz3Search(BaseTestCase):
    def test_baidu_search(self):
        home_page=HomePage(self.driver)
        s=home_page.search3('admin','123456','haotest')
        time.sleep(4)
        self.assertEqual(s,'haotest',msg=s)