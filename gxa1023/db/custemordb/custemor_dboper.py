from gxa1023.db.dboper import Sql_oper


class Custemor_dboper:

    def __init__(self):
        self.dbop = Sql_oper(host = '172.17.4.216', user = 'root', password = '123456',
        database = 'quote', port = 3306, charset = 'utf8')
    #删除数据
    def delete_Custemor(self,sql):
        self.dbop.update_data(sql)

    def add_Custemor(self,sql):
        self.dbop.update_data(sql)

    def update_Custemor(self,sql):
        self.dbop.update_data(sql)

    def search_Custemor(self,sql):
        self.dbop.search_data(sql)






