import unittest
from HTMLTestRunner import HTMLTestRunner

from gxa1023.base.usebrowser import UseBrower
from gxa1023.webpage.customermanager.customerpage import CustomerPage
from gxa1023.util.excel_oper import Excel_e


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.cp = CustomerPage()

    #添加客户信息，只输入客户姓名
    # def test_customer_add_id(self):
    #     alert_text1 = self.cp.customer_add(name='哈哈哈')
    #     self.cp.lp.ub.assertEqual(alert_text1, self.cp.lp.bo.get_cell(6, 4))

    #添加客户信息，输入客户姓名、Email、出生日期、创建人
    def test_customer_add_correct(self):
        self.cp.customer_add(name='哈哈哈',email="252@sina.com",birth="1998-11-01 20:20:20",addman="加加")

        self.assertEqual(self.cp.get_add_success_alert(), self.cp.lp.ex.get_cell(6, 4))

    #修改客户信息的客户地址
    def test_customer_modify_addr(self):
        self.cp.customer_modify(addr='上海')
        self.assertEqual(self.cp.get_modify_success_alert(),self.cp.lp.ex.get_cell(7, 4))

    def tearDown(self) -> None:
        UseBrower.quit()

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    test_case = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    suite.addTests(test_case)
    #print(time.localtime())
    # 获取当前时间
    #data_now = time.strftime('%Y-%m-%d', time.localtime())
    # 创建html文件
    with open('../../report/report_2.html', 'wb+')as file:
        runner = HTMLTestRunner(stream=file, verbosity=1, title='自动化', description='ui自动化')
        runner.run(suite)
