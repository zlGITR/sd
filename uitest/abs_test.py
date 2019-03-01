import unittest
from uitest import abs
from ddt import ddt,data,unpack
class test(unittest.TestCase):
    def setUp(self):
        print("开始执行测试")
    def test_abs(self):
        self.assertEqual(abs.test(1),1,"abs(1)应等于1")
    def test_abs1(self):
        self.assertEqual(abs.test(-1),1,"abs(-1)应等于-1")
    def test_abs2(self):
        self.assertEqual(abs.test(0),0,"abs(0)应等于0")
    def tearDown(self):
        print("测试结束")
# @ddt
# class abtestcase(unittest.TestCase ):
#     def setUp(self):
#        print("开始执行")
#     @data([1,1],[-1,1],[0,1])
#     @unpack
#     def test_abs(self,n,expect_value):
#         result=abs.test(n)
#         self.assertEqual(result,expect_value ,msg=result)
#     def tearDown(self):
#         print("结束")
# if __name__=='__main__':
#     unittest .main(verbosity= 2)
