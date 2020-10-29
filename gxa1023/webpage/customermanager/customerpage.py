import time
import unittest
from HTMLTestRunner import HTMLTestRunner

import sys

from gxa1023.db.custemordb.custemor_dboper import Custemor_dboper

sys.path.append('C:\\Users\\Administrator\\PycharmProjects\\pythonProject1')
from gxa1023.webpage.usermanager.loginpage import LoginPage
from gxa1023.util.excel_oper import Excel_e

from gxa1023.webpage.usermanager.loginpage import LoginPage
from gxa1023.base.broweroperation import BrowerOperation
from gxa1023.config.log_crm import AutoLog



class CustomerPage:

    def __init__(self):
        self.lp = LoginPage()
        #self.lp.login('admin','123456')
        self.co = Custemor_dboper()

    # 添加客户信息
    def customer_add(self,name="",email="",birth="",addman=""):
        #self.co.delete_Custemor("delete from tb_user where username ='4654654'")
        self.lp.login(self.lp.ex.get_cell(6, 2), self.lp.ex.get_cell(6, 3))
        self.lp.bo.change_frame(self.lp.yp.get_locator('CustomerPage', 'topFrame'))
        time.sleep(5)
        self.lp.bo.click_ele(self.lp.yp.get_locator('CustomerPage', 'CustomerInfo'))
        time.sleep(5)
        self.lp.bo.driver.switch_to.default_content()
        time.sleep(5)
        self.lp.bo.driver.execute_script("document.getElementsByTagName('frameset')[1]")
        time.sleep(5)
        self.lp.bo.change_frame(self.lp.yp.get_locator('CustomerPage', 'mainFrame'))
        time.sleep(5)
        # 点击添加
        self.lp.bo.click_ele(self.lp.yp.get_locator('CustomerPage', 'add_button'))
        # 输入客户姓名
        self.lp.bo.send_ks(self.lp.yp.get_locator('CustomerPage', 'name'),name)
        self.lp.log.set_mes('输入客户姓名', 'info')
        # self.log.set_mes('用户姓名:' + '王进', 'info')
        # 输入Email
        self.lp.bo.send_ks(self.lp.yp.get_locator('CustomerPage', 'e-mail'),email)
        self.lp.log.set_mes('输入Email', 'info')
        # self.log.set_mes('Email:' + '1402488826@qq.com', 'info')
        # 输入出生日期
        self.lp.ub.driver.execute_script("document.getElementById('customerBirthday').readOnly=false")
        self.lp.bo.send_ks(self.lp.yp.get_locator('CustomerPage', 'birthday'),birth)
        self.lp.log.set_mes('输入出生日期', 'info')
        # self.log.set_mes('出生日期:' + '2020-02-02 22:22:22', 'info')
        # 输入创建人
        self.lp.bo.send_ks(self.lp.yp.get_locator('CustomerPage', 'addman'),addman)
        self.lp.log.set_mes('输入创建人', 'info')
        # self.log.set_mes('创建人:' + '马云', 'info')
        # 点击添加
        self.lp.bo.click_ele(self.lp.yp.get_locator('CustomerPage', 'add_submit'))

        # self.login.log('获取弹出框内容','info')

    def get_add_success_alert(self):

        return self.lp.bo.get_alert()

    def customer_modify(self,addr=""):
        self.lp.login(self.lp.ex.get_cell(6, 2), self.lp.ex.get_cell(6, 3))
        time.sleep(5)
        self.lp.bo.change_frame(self.lp.yp.get_locator('CustomerPage', 'topFrame'))
        self.lp.bo.click_ele(self.lp.yp.get_locator('CustomerPage', 'CustomerInfo'))
        self.lp.bo.driver.switch_to.default_content()
        self.lp.bo.driver.execute_script("document.getElementsByTagName('frameset')[1]")
        self.lp.bo.change_frame(self.lp.yp.get_locator('CustomerPage', 'mainFrame'))
        #点击编辑
        self.lp.bo.click_ele(self.lp.yp.get_locator('CustomerPage', 'modify_button'))
        # 修改客户地址
        self.lp.bo.clear_c(self.lp.yp.get_locator('CustomerPage', 'addr'))
        self.lp.bo.send_ks(self.lp.yp.get_locator('CustomerPage', 'addr'),addr)
        self.lp.log.set_mes('修改客户地址', 'info')
        #点击提交
        self.lp.bo.click_ele(self.lp.yp.get_locator('CustomerPage', 'modify_submit'))

    def get_modify_success_alert(self):

        return self.lp.bo.get_alert()


# if __name__ == '__main__':
#     cp = CustomerPage()
#     cp.customer_add(id='1001',name='吴志伟')




