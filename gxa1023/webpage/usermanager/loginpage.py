import time

from gxa1023.base.broweroperation import BrowerOperation
from gxa1023.base.usebrowser import UseBrower
from gxa1023.util.excel_oper import Excel_e
from gxa1023.util.yaml_oper import Yaml_operation
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from gxa1023.config.log_crm import AutoLog
from gxa1023.util.yaml_oper import Yaml_operation

class LoginPage:

    def __init__(self):

        self.ub = UseBrower()
        self.bo = BrowerOperation(UseBrower.driver)
        self.bo.open_url('http://172.17.4.216:8080/crm')
        self.yp = Yaml_operation('../../config/locator.yaml')
        self.ex = Excel_e('../../config/exl_test.xlsx','用例参数')
        self.log = AutoLog()


    def login(self,username='',password=''):

        self.log.set_mes('登录功能开始', 'info')
        self.ub.driver.find_element_by_name(self.yp.get_locator('LoginPage', 'username')).send_keys(username)
        self.log.set_mes('输入用户名', 'info')
        self.ub.driver.find_element_by_name(self.yp.get_locator('LoginPage', 'password')).send_keys(password)
        self.log.set_mes('输入密码', 'info')
        self.ub.driver.find_element_by_id(self.yp.get_locator('LoginPage', 'submit')).click()
        self.log.set_mes('点击登录', 'info')

    def get_login_success_text(self,frame_name,xpath):
        self.bo.change_frame(frame_name)
        return self.bo.get_text(xpath)




# if __name__ == '__main__':
#     lp = LoginPage()
#     lp.login('admin','123456')
#     time.sleep(3)
#     UseBrower.quit()

