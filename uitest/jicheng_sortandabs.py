import unittest
from uitest.abs_test import  test
import HTMLTestRunner
import os
from uitest .sort_test import  abtestcase
#goujian
cur_path=os.path.dirname(os.path.realpath (__file__))
report_path=os.path.join(cur_path ,"report")
if not os.path.exists(report_path): os.mkdir(report_path )
suite=unittest.TestSuite()
suite.addTest(unittest .makeSuite(test) )
suite.addTest(unittest .makeSuite(abtestcase) )
if __name__=="__main__":
    html_report=report_path +r"\result.html"
    fp =open(html_report ,"wb")
    runner=HTMLTestRunner .HTMLTestRunner(stream=fp,verbosity= 2,title="",description="用例执行情况")
    runner .run(suite)