# from selenium import webdriver
#from quote.base.usebrowser import UseBrower
from selenium.webdriver.common.alert import Alert


class BrowerOperation:

    def __init__(self,driver):
        self.driver = driver
        # self.driver = webdriver.Chrome

    def open_url(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(e,'地址错误')

    def send_ks(self,xpath,content):
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(content)
        except Exception as e:
            print(e,'没有找到该元素')

    def clear_c(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath).clear()
        except Exception as e:
            print(e,'没有找到该元素')

    def click_ele(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except Exception as e:
            print(e,'没有找到该元素')

    def get_text(self,xpath):
        try:
            text = self.driver.find_element_by_xpath(xpath).text
        except Exception as e:
            print(e, '没有找到该元素')
        return text

    def get_alert(self):
        return Alert(self.driver).text

    def change_frame(self,frame_name):
        self.driver.switch_to.parent_frame()
        self.driver.switch_to_frame(frame_name)

    def change_window(self,window_name):
        for window_hd in self.driver.window_handles:
            self.driver.switch_to_window(window_hd)
            if self.driver.title == window_name:
                break


# if __name__ == '__main__':
#     ub = UseBrower()
#     bo = BrowerOperation(UseBrower.driver)
#     bo.open_url('http://172.17.4.216:8080/crm')
#     bo.send_keys('/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/input','admin')
#     bo.send_keys('/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/div/input','123456')
#     bo.click_element('//*[@id="in1"]')
#     UseBrower.quit()