import pymysql

# 连接数据库
# pymysql.connect("mysql_ip","username","passwd","database_name")
db = pymysql.connect("localhost", "root", "123456", "a")

# 创建一个游标对象 cursor
cursor = db.cursor()

sql = "select version()"
# 使用 execute() 方法执行 SQL 语句
cursor.execute(sql)

# 使用 fetchone() 方法获取单条数据，返回的数据是元组类型
data = cursor.fetchone()

print(type(data))
print(data)
print("Database version : %s " % data)

# 关闭数据库连接
cursor.close()
db.close()
