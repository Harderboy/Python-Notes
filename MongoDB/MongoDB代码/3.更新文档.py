from pymongo import MongoClient


# 连接服务器
conn = MongoClient("localhost", 27017)

# 判断数据库是否已存在
dblist = conn.list_database_names()
print(dblist)
print(type(dblist))
if "mydb" in dblist:
    print("数据库已存在！")

# 连接数据库
db = conn.mydb

collist = db.list_collection_names()
# 判断 sites 集合是否存在
if "student" in collist:
    print("集合已存在！")

# 获取集合
collection = db.student

# 更新单个文档
# DeprecationWarning: update is deprecated.
# Use replace_one, update_one or update_many instead.
# collection.update({"name": "tomson"}, {"$set": {"age": 36}})
# update_one() 方法修改文档中的记录。该方法第一个参数为查询的条件，第二个参数为要修改的字段。如果查找到的匹配数据多于一条，则只会修改第一条。
collection.update_one({"name": "tomson"}, {"$set": {"age": 28}})

# 更新多个文档
x = collection.update_many({"name": {"$regex": "^l"}}, {"$set": {"age": 24}})
# x.modified_count
# print(x)
# print(type(x))
print(x.modified_count, "文档被修改")

# 断开
conn.close()
