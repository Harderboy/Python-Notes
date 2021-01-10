import mySqlClass

db = mySqlClass.MySqlClass("localhost", "root", "123456", "a")
sql1 = "select * from bandcard"
res1 = db.get_one(sql1)
print(type(res1))
print(res1)

sql2 = "update bandcard set money = 0 where id = 6"
res2 = db.update(sql2)
print(res2)
