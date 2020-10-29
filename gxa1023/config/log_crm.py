
import logging
# 创建logger对象
import time

class AutoLog:

    def __init__(self):
        self.logger = logging.getLogger('log')

    def set_mes(self, mess, level):

        try:
            logger = logging.getLogger('log')

            now_data = time.strftime('%Y-%m-%d', time.localtime())
            # 创建文件handle
            fh = logging.FileHandler('../../log_info/auto_' + now_data + '.log')
            # 创建控制台handle
            ch = logging.StreamHandler()
            # 格式化
            fm = logging.Formatter('%(asctime)s %(message)s %(levelname)s')
            # 对文件格式
            fh.setFormatter(fm)
            ##对控制台格式
            ch.setFormatter(fm)
            # 文件句柄加入logger
            self.logger.addHandler(fh)
            # 控制台句柄加入logger
            self.logger.addHandler(ch)
            # 设置打印级别
            self.logger.setLevel(logging.DEBUG)
            # 输出info
            if level == 'debug':
                self.logger.debug(mess)
            elif level == 'info':
                self.logger.info(mess)
            elif level == 'error':
                self.logger.error(mess)
            else:
                self.logger.warning(mess)

            # 移除文件句柄
            logger.removeHandler(fh)
            # 移除控制台句柄
            logger.removeHandler(ch)
            # 关闭文件
            fh.close()
        except:
            print('')
        finally:
            fh.close()

# if __name__ == '__main__':
#     auto = AutoLog()
#     # url = 'www.baidu.com'
#     auto.set_mes('message','info')