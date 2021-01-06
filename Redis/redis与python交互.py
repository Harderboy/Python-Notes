import redis

# 连接
r = redis.StrictRedis(host="localhost", port=6379, password="liuheng")


# 写法1：根据数据类型的不同，调用相应的方法

# 拿字符串类型举例

# 写
# r.set("p1", "good")

# 读
# 先判断是否存在
# print(r.get("p1"))

# 其他方式参考redis命令

# 方法2：pipeline
# 缓冲多条命令，然后依次执行，减少服务器和客户端之间的TCP数据包
# 一次请求发起多条命令
pipe = r.pipeline()
pipe.set("p2", "nice")
pipe.set("p3", "better")
pipe.set("p4", "handsome")
pipe.execute()
