from testsuites .base_testcase import BaseTestCase
from Pageobjects .Discuzbody import  HomePage
import time
import unittest
class Discuz1Search(BaseTestCase):
    def test_baidu_search(self):
        home_page=HomePage(self.driver)
        relytext=home_page.search1('liwei','123456','老弟来了','老弟你好啊拦截啊苏打绿阿娇','老弟阿斯达克，jadksvkvanlskfdv.ankv ')
        self.assertEqual(relytext, '发表回复', msg=relytext)