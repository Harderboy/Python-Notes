import pymysql
'''
fetchone() ：获取下一个查询结果集，结果集是一个对象，元组类型

fetchall()：接受全部返回的行，元组类型

rowcount：是一个只读属性，返回execute()方法影响的行数

'''

# 连接数据库
db = pymysql.connect("localhost", "root", "123456", "a")

cursor = db.cursor()

# 建表
sql = "select * from bandcard where money>2000 "
# 使用 execute() 方法执行 SQL 语句
try:
    cursor.execute(sql)
    # 不对数据进行更改，无需commit
    # db.commit()
    resultTuple = cursor.fetchall()
    print(type(resultTuple))
    print(resultTuple)
    for row in resultTuple:
        print("%d -- %d" % (row[0], row[1]))
except:
    # 提交失败，回滚到上次操作
    db.rollback()

# 关闭数据库连接
cursor.close()
db.close()
