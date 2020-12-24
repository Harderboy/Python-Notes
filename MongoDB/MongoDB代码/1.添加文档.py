from pymongo import MongoClient

# 连接服务器
conn = MongoClient("localhost", 27017)

# 判断数据库是否已存在
# dblist = myclient.database_names()
dblist = conn.list_database_names()
print(dblist)
print(type(dblist))
if "mydb" in dblist:
    print("数据库已存在！")

# 连接数据库
db = conn.mydb

collist = db.list_collection_names()
# collist = mydb.collection_names()
# 判断 sites 集合是否存在
if "student" in collist:
    print("集合已存在！")

# 获取集合
collection = db.student

# 添加单个文档
# 键都是字符串，要加""
# DeprecationWarning: insert is deprecated. insert()方法被弃用了
# Use insert_one or insert_many instead.
# collection.insert({
#     "name": 'tomy',
#     "age": 23,
#     "gender": 1,
#     "address": '安阳',
#     "isDelete": 0
# })

# 新版本改用这两种方法：db.collection.insert_one() 和 db.collection.insert_many()

# insert_one() 方法返回 InsertOneResult 对象，该对象包含 inserted_id 属性，它是插入文档的 id 值。
# db.collection.insert_one()
# collection.insert_one({
#     "name": '369',
#     "age": 22,
#     "gender": 1,
#     "address": '安阳',
#     "isDelete": 0
# })
# mydict = {
#     "name": 'bin',
#     "age": 20,
#     "gender": 1,
#     "address": '滑县',
#     "isDelete": 0
# }
# x = collection.insert_one(mydict)
# print(x.inserted_id)

# 添加多个文档，以列表形式插入
# collection.insert_many([{},{}])
x = collection.insert_many([{
    "name": '957',
    "age": 22,
    "gender": 1,
    "address": '安阳',
    "isDelete": 0
}, {
    "name": 'lihua',
    "age": 29,
    "gender": 1,
    "address": '安阳',
    "isDelete": 0
}])
print(x.inserted_ids)  # 输出一个_id列表

# 插入指定 _id 的多个文档
# mylist = [
#     {
#         "_id": 1,
#         "name": "RUNOOB",
#         "age": 29,
#         "gender": 1,
#         "address": '安阳',
#         "isDelete": 0
#     },
#     {
#         "_id": 2,
#         "name": "RUNOOB1",
#         "age": 30,
#         "gender": 0,
#         "address": '安阳',
#         "isDelete": 0
#     },
#     {
#         "_id": 3,
#         "name": "RUNOOB2",
#         "age": 31,
#         "gender": 1,
#         "address": '安阳',
#         "isDelete": 0
#     },
# ]
# x = collection.insert_many(mylist)
# 输出插入的所有文档对应的 _id 值
# print(x.inserted_ids)

# 断开
conn.close()
