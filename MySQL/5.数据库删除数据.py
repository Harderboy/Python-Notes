import pymysql

# 连接数据库
db = pymysql.connect("localhost", "root", "123456", "a")

cursor = db.cursor()

# 建表
sql = "delete from bandcard where money = 1000"
# 使用 execute() 方法执行 SQL 语句
try:
    cursor.execute(sql)
    # 事务
    db.commit()
except:
    # 提交失败，回滚到上次操作
    db.rollback()

# 关闭数据库连接
cursor.close()
db.close()
