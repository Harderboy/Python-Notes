import pymysql


class MySqlClass():
    def __init__(self, host, username, passwd, dbName):
        self.host = host
        self.username = username
        self.passwd = passwd
        self.dbName = dbName

    def connect(self):
        self.db = pymysql.connect(self.host, self.username, self.passwd,
                                  self.dbName)
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def get_one(self, sql):
        res = None
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            self.close()
        except:
            print("查询失败！")
        return res

    def get_all(self, sql):
        res = ()
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close()
        except:
            print("查询失败！")
        return res

    def insert(self, sql):
        return self.__edit(sql)

    def update(self, sql):
        return self.__edit(sql)

    def delete(self, sql):
        return self.__edit(sql)

    def __edit(self, sql):
        count = 0
        try:
            self.connect()
            # 返回execute()方法影响的行数
            count = self.cursor.execute(sql)
            # 事务
            self.db.commit()
            self.close()
        except:
            print("事务提交失败")
            # 提交失败，回滚到上次操作
            self.db.rollback()
        return count
