import pymysql

# 连接数据库
db = pymysql.connect("localhost", "root", "123456", "a")

cursor = db.cursor()

# 检查表是否存在，存在则删除
# cursor.execute("drop table if exists bandcard")

# 建表
sql = "create table bandcard(id int auto_increment primary key, money int not null, name varchar(20) not null)"
# 使用 execute() 方法执行 SQL 语句
cursor.execute(sql)

# 关闭数据库连接
cursor.close()
db.close()
