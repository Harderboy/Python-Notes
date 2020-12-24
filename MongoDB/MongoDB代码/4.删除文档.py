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

# 删除单个文档
# collection.delete_one()
collection.delete_one({"name": "957"})
# 删除多个文档
# collection.delete_many()
# x = collection.delete_many({"name": {"$regex": "^F"}})
# x.deleted_count
# print(x.deleted_count, "个文档已删除")

# delete_many() 方法如果传入的是一个空的查询对象，则会删除集合中的所有文档
# x = mycol.delete_many({})
# print(x.deleted_count, "个文档已删除")

# drop() 方法来删除一个集合。
# 如果删除成功 drop() 返回 true，如果删除失败(集合不存在)则返回 false。

# 断开
conn.close()
