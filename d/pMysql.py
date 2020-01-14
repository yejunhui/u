#数据库操作
import pymysql

class pMysql:
    def __init__(self):
        conn = pymysql.connect(host='localhost',port=3306,user='user',password='123456',db='d')

        try:
            self.cursor = conn.cursor()
        except:
            print('连接数据库遇到了问题！')

    def ex(self,s):
        try:
            self.cursor.execute(s)
            # 获取所有记录列表
            return self.cursor.fetchall()
        except:
            print('执行SQL遇到了问题！')