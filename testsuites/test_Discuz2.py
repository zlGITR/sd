from testsuites .base_testcase import BaseTestCase
from Pageobjects.Discuzbody  import  HomePage
import time
import unittest
class Discuz2Search(BaseTestCase):
    def test_baidu_search(self):
        home_page=HomePage(self.driver)
        reply=home_page.search2('admin','123456','薇','liwei','北京你好','大哥哥大姐姐过年好几分钟；的发展科比三大板块东南快报美丽的负面口碑兄弟们卡拉巴赫是下副本马克思')
        self.assertEqual(reply, '发表回复', msg=reply)