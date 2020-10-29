import time
import unittest

import sys
from HTMLTestRunner import HTMLTestRunner

sys.path.append('E:\\.jenkins\\workspace\\gxa')

from gxa1023.base.broweroperation import BrowerOperation
from gxa1023.base.usebrowser import UseBrower
from gxa1023.webpage.usermanager.loginpage import LoginPage
from gxa1023.util.yaml_oper import Yaml_operation


class LoginTest(unittest.TestCase):

    def setUp(self) -> None:
        self.login= LoginPage()
        self.bo = BrowerOperation(UseBrower.driver)

    #账户和密码都为空
    def test_login_username_password_null(self):
        self.login.login('', '')
        self.assertEqual(self.bo.get_alert(),'- 用户名不能为�?\n- 密码不能为空!\n')
    #用户名为�?
    def test_login_username_null(self):
        self.login.login('', '123456')
        self.assertEqual(self.bo.get_alert(), '- 用户名不能为�?\n')
    #密码为空
    def test_login_password_null(self):
        self.login.login('admin', '')
        self.assertEqual(self.bo.get_alert(), '- 密码不能为空!\n')
    #账户和密码输入正确，登录成功
    def test_login_success(self):
        self.login.login('admin', '123456')
        correct_text = self.login.get_login_success_text('topFrame','/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/div')
        self.assertEqual(correct_text, '当前用户：张�?)

    def tearDown(self) -> None:
        UseBrower.quit()

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    test_case = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    suite.addTests(test_case)
    print(time.localtime())
    # 获取当前时间
    data_now = time.strftime('%Y-%m-%d', time.localtime())
    # 创建html文件
    with open('../../report/report.html', 'wb+')as file:
        runner = HTMLTestRunner(stream=file, verbosity=1, title='自动�?, description='ui自动�?)
        runner.run(suite)


