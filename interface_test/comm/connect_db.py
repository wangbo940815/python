import pymysql
from comm.read_conf import Read_conf

class Connect_db:
    '''数据库连接类，用于数据库连接和执行sql语句（pymysql只支持mysql）'''

    def __init__(self):
        db_info=Read_conf()
        '''重配置文件中读取数据库连接的相关信息'''
        ip=db_info.get("database","ip")
        username=db_info.get("database","username")
        password=db_info.get("database","password")
        dbname=db_info.get("database","dbname")
        #cursorclass=pymysql.cursors.DictCursor
        self.db = pymysql.connect(ip,username,password,dbname,charset="utf8")
        self.cursor = self.db.cursor()
        
        

    def Execu_sql(self,*sql):
        for i in sql:
            self.cursor.execute(i)
        """关闭连接"""
        data = self.cursor.fetchall()
        return  data  
    def get_one(self,sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        return data
    def commit(self):
        self.db.commit()
    def close(self):
        self.cursor.close()
        self.db.close()
if __name__ == '__main__':
    mobilephone="13550848523"
    b="select Id from member where mobilephone='"+mobilephone+"' "     
    a=Connect_db()
    print(a.get_one(b)[0])
