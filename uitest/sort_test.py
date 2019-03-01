import unittest
from uitest.sort import sort
from ddt import ddt,data,unpack
@ddt
class abtestcase(unittest.TestCase ):
    @classmethod
    def setUpclass(cls):
       print("开始执行")
    @data([1,1,10],[-1,-1,0],[0,0,0])
    @unpack
    def test_sort(self,n,m,expect_value):
        result=sort(n,m)
        self.assertEqual(result,expect_value ,msg=result)
    @classmethod
    def tearDownClass(cls):
        print("结束")
if __name__=='__main__':
    unittest .main(verbosity= 2)