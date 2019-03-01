from testsuites .base_testcase import BaseTestCase
from Pageobjects .Discuzbody import  HomePage
import time
import unittest
class Discuz4Search(BaseTestCase):
    def test_baidu_search(self):
        home_page=HomePage(self.driver)
        reust=home_page.search4()
        time.sleep(10)
        self.assertNotEqual(reust,'',msg=reust)
