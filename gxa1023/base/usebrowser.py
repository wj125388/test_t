import time

from selenium import webdriver

class UseBrower:

    driver = None

    def __init__(self):
        self.driver = webdriver.Chrome('../../chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        UseBrower.driver = self.driver


    @classmethod
    def quit(self):
        UseBrower.driver.quit()

# if __name__ == '__main__':
#     ub = UseBrower()
#     time.sleep(5)
#     UseBrower.quit()
