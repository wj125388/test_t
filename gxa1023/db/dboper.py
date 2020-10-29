import pymysql

class Sql_oper:

    def __init__(self,host,user,password,database,port,charset):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset
    #创建连接
    def get_conn(self):
        try:
            conn = pymysql.Connection(host=self.host, user=self.user, password=self.password,
                                      database=self.database, port=self.port, charset=self.charset)
            return conn
        except Exception as e:
            print(e,"连接失败")

    #更新数据
    def update_data(self,sql):
        try:
            conn = self.get_conn()
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            # 通过游标的fetchall方法获取数据
            res = cur.fetchall()
            # 打印数据
            print(res)

        except Exception as e:
            print(e, '执行错误')
            conn.rollback()
        finally:
            cur.close()
            conn.close()
    #查询数据
    def search_data(self,sql):

        try:
            conn = self.get_conn()
            cur = conn.cursor()
            cur.execute(sql)
            #通过游标的fetchall方法获取数据
            res = cur.fetchall()
            #打印数据
            print(res)

        except Exception as e:
            print(e,'执行错误')
            conn.rollback()
        finally:
            cur.close()
            conn.close()
        return res

# if __name__ == '__main__':

    # sql_oper = Sql_oper(host='172.17.4.216', user='root', password='123456',database='quote', port=3306, charset='utf8')
    # print(sql_oper.search_data("select * from tb_user where username='7588'"))
    # sql_oper.update_data("update tb_user set grade='1' where")
    # sql_oper.delete_operation()
    # sql_oper.update_operation()
    # sql_oper.search_all()