import sys
sys.path .append('F:/ui')
import HTMLTestRunner
import unittest
import os
from testsuites.test_Discuz1 import Discuz1Search
from testsuites.test_Discuz2  import Discuz2Search
from testsuites.test_Discuz3  import Discuz3Search
from testsuites.test_Discuz4  import Discuz4Search
#构造存储路径
cur_path=os.path.dirname(os.path.realpath(__file__))
report_path=os.path.join(cur_path,"report")
if not os.path.exists(report_path):os.mkdir(report_path)
#构造测试套件
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(Discuz1Search))
suite.addTest(unittest.makeSuite(Discuz2Search))
suite.addTest(unittest.makeSuite(Discuz3Search))
suite.addTest(unittest.makeSuite(Discuz4Search))
#执行
if __name__=='__main__':
    html_report=report_path+r'\report.html'
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="测试Discuz",description="测试")
    runner.run(suite)