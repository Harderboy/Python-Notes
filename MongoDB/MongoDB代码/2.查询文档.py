# import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

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

# 查询部分文档
# find_one() 方法来查询集合中的一条数据。
# "$gt" 注意书写规范
# 读取 name 字段中第一个字母 ASCII 值大于 "H" 的数据，大于的修饰符条件为 {"$gt": "H"}
# res = collection.find({"age": {"$gt": 22}})
# for row in res:
#     print(row)
#     print(type(row))
# 使用正则表达式查询 用于读取 name 字段中第一个字母为 "R" 的数据，正则表达式修饰符条件为：{"$regex": "^R"}
# find() 方法来查询指定字段的数据，将要返回的字段对应值设置为 1。
#       db.集合名.find(query, {<key>:1, <key>:1})
# res = collection.find({}, {"_id": 0, "name": 1, "age": 1})
res = collection.find({}, {"name": 0})
for raw in res:
    print(raw)

# 除了 _id 你不能在一个对象中同时指定 0 和 1，如果你设置了一个字段为 0，则其他都为 1，
# collection.find({}, {"_id": 0, "name": 1, "age":1})  正确
# collection.find({}, {"name": 0})  正确 除了name字段其他都返回
# collection.find({}, {"name": 0, "age":1})  报错

# 查询所有文档
# res = collection.find()
# for row in res:
#     print(row)
#     print(type(row))

# 统计查询
# count() 方法 已被弃用
# DeprecationWarning: count is deprecated.
# Use Collection.count_documents instead.
# count = collection.find({"age": {"$gt": 22}}).count()
# print(count)

# count_documents() 方法
count2 = collection.count_documents({"age": {"$gt": 22}})
# print(count2)

# 根据_id进行查询
res1 = collection.find({"_id": ObjectId("5fe05a1671588808f57f89aa")})
# print(res1)

# 排序
# sort() 方法第一个参数为要排序的字段，第二个字段指定排序规则，1 为升序，-1 为降序，默认为升序。

# 升序 注意sort()方法的写法
res2 = collection.find().sort("age")
# for row in res2:
#     print(row)

# 降序
# import pymongo
# res3 = collection.find().sort("age", pymongo.DESCENDING)
res3 = collection.find().sort("age", -1)
# for row in res3:
#     print(row)

# 分页查询
res4 = collection.find().skip(3).limit(5)
# for row in res4:
#     print(row)

# 断开
conn.close()
