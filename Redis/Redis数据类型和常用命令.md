# Redis 数据类型和常用命令

Redis 是速度非常快的非关系型（NoSQL）内存键值数据库，可以存储键和五种不同类型的值之间的映射。

键的类型只能为字符串，值支持五种数据类型：字符串 string 、列表 list、集合 set、散列表 hash（哈希）、有序集合 zset（sorted set：有序集合）。

## string

string 是 redis 最基本的类型，你可以理解成与 Memcached 一模一样的类型，一个 key 对应一个 value。

string 类型是二进制安全的。意思是 redis 的 string 可以存储任何数据。比如jpg图片或者序列化的对象。

string 类型是 Redis 最基本的数据类型，string 类型的值最大能存储 512MB。

1. 设置
    - 设置键值  
    `set key value`
    - 指定的 key 设置值及其过期时间，以秒为单位。如果 key 已经存在， SETEX 命令将会替换旧的值。  
    `setex key seconds value`
    - 设置多个键值对  
    `MSET key value [key value ...]`

2. 获取
    - 获取指定 key 的值。如果 key 不存在，返回Null/0/nil 。如果key 储存的值不是字符串类型，返回一个错误。  
    `GET key`
    - 所有(一个或多个)给定 key 的值。 如果给定的 key 里面，有某个 key 不存在，那么这个 key 返回特殊值 nil  
    `MGET key1 [key2..]`

3. 运算
  要求：值为字符串类型的数字
    - 将 key 中储存的数字值增一，如果 key 不存在，那么 key 的值会先被初始化为 0 ，然后再执行 INCR 操作  
    `INCR key`
    - 将 key 中储存的数字值减一，如果 key 不存在，那么 key 的值会先被初始化为 0 ，然后再执行 INCR 操作  
    `DECR key`
    - 将 key 所储存的值加上给定的增量值（increment）,如果 key 不存在，那么 key 的值会先被初始化为 0 ，然后再执行 INCRBY 命令。  
    `INCRBY key increment`
    - key 所储存的值减去给定的减量值（decrement）,如果 key 不存在，那么 key 的值会先被初始化为 0 ，然后再执行 INCRBY 命令  
    `DECRBY key decrement`

4. 其他
    - 如果 key 已经存在并且是一个字符串， APPEND 命令将指定的 value 追加到该 key 原来值（value）的末尾。  
    `APPEND key value`
    - 返回 key 所储存的字符串值的长度  
    `STRLEN key`

## key

用于管理 redis 的键

- 查找所有符合给定模式( pattern)的 key 。  
`KEYS pattern`

- 检查给定 key 是否存在。返回值：若 key 存在返回 1 ，否则返回 0  
`EXISTS key`

- 返回 key 所储存的值的类型  
`TYPE key`

- 在 key 存在时删除 key，不存在的 key 会被忽略。返回值：被删除 key 的数量。  
`DEL key[key ...]`

- 为给定 key 设置过期时间，以秒计。  
`EXPIRE key seconds`

- 以秒为单位，返回给定 key 的剩余生存时间(TTL, time to live)  
`TTL key`

## hash

hash 是一个键值(key=>value)对集合

hash 是一个 **string 类型** 的 field（字段） 和 value（值） 的映射表，hash 特别适合用于存储对象。

```json
{
    name:"tom",
    age:18
}
```

Redis 中每个 hash 可以存储 232 - 1 键值对（40多亿）。

1. 设置
    - 将哈希表 key 中的字段 field 的值设为 value  
    `HSET key field value`
    `HSET KEY_NAME FIELD VALUE`

    - 同时将多个 field-value (域-值)对设置到哈希表 key 中。  
    `HMSET key field1 value1 [field2 value2 ]`

2. 获取
    - 获取存储在哈希表中指定字段的值。  
    `HGET key field`
    - 获取所有给定字段的值  
    `HMGET key field1 [field2]`
    - 获取在哈希表中指定 key 的所有字段和值  
    `hgetall key`
    - 获取所有哈希表中的字段  
    `HKEYS key`
    - 获取哈希表中所有值  
    `HVALS key`
    - 获取哈希表中字段的数量  
    `HLEN key`

3. 其他
    - 查看哈希表 key 中，指定的字段是否存在。如果哈希表含有给定字段，返回 1 。 如果哈希表不含有给定字段，或 key 不存在，返回 0 。  
    `HEXISTS key field`
    - 删除一个或多个哈希表字段  
    `HDEL key field1 [field2]`

## list

Redis列表是简单的 **字符串 string 类型** 列表，按照插入顺序排序，元素可以重复。你可以添加一个元素到列表的头部（左边）或者尾部（右边）

一个列表最多可以包含 232 - 1 个元素 (4294967295, 每个列表超过40亿个元素)。

1. 设置
    - 将一个或多个值插入到列表头部（最左边）。 如果 key 不存在，一个空列表会被创建并执行 LPUSH 操作。 当 key 存在但不是列表类型时，返回一个错误。  
    `LPUSH key value1 [value2]`
    - 将一个或多个值插入到列表的尾部(最右边)  
    `RPUSH key value1 [value2]`
    - 在列表的元素前或者后插入元素，将值 value 插入到列表 key 当中，位于值 pivot 之前或之后。（左边为前）  
    `LINSERT key BEFORE|AFTER pivot value`
    - 通过索引设置列表元素的值  
    `LSET key index value`

        注意：索引从0开始，索引值可以为负数，表示偏移量是从list的尾部开始，如-1表示最后一个元素
2. 获取
    - 移出并获取列表的第一个元素  
    `LPOP key`
    - 移除列表的最后一个元素，返回值为移除的元素。  
    `RPOP key`
    - 获取列表指定范围内的元素  
    `LRANGE key start stop`

        注意：start、stop 参考上述索引

3. 其他
    - 对一个列表进行修剪(trim)，就是说，让列表只保留指定区间内的元素，不在指定区间之内的元素都将被删除。  
    `LTRIM key start stop`
    - 获取列表长度  
    `LLEN key`
    - 通过索引获取列表中的元素  
    `LINDEX key index`

## set

Redis 的 Set 是 **string 类型** 的无序集合。集合成员是唯一的，这就意味着集合中不能出现重复的数据。

Redis 中集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是 O(1)。

集合中最大的成员数为 232 - 1 (4294967295, 每个集合可存储40多亿个成员)

1. 设置
    - 向集合添加一个或多个成员  
    `SADD key member1 [member2]`

2. 获取
    - 返回集合中的所有成员  
    `SMEMBERS key`
    - 获取集合的成员数  
    `SCARD key`
    - 移除并返回集合中的一个随机元素  
    `SPOP key`

3. 集合运算
    - 返回给定所有集合的交集  
    `SINTER key1 [key2]`
    - 返回第一个集合与其他集合之间的差异（差集）  
    `SDIFF key1 [key2]`
    - 返回所有给定集合的并集  
    `SUNION key1 [key2]`
    - 返回给定所有集合的差集并存储在 destination 中  
    `SDIFFSTORE destination key1 [key2]`
    - 返回给定所有集合的交集并存储在 destination 中  
    `SINTERSTORE destination key1 [key2]`
    - 所有给定集合的并集存储在 destination 集合中  
    `SUNIONSTORE destination key1 [key2]`
    - 判断 member 元素是否是集合 key 的成员，如果成员元素是集合的成员，返回 1 。 如果成员元素不是集合的成员，或 key 不存在，返回 0 。  
    `SISMEMBER key member`

## zset

Redis 有序集合和集合一样也是 **string 类型**元素的集合，且不允许重复的成员。

不同的是每个元素都会关联一个 double 类型的分数score（表示权重）。redis 正是通过分数来为集合中的成员进行从小到大的排序。

有序集合的成员是唯一的，但分数(score)却可以重复。

集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是 O(1)。 集合中最大的成员数为 2^32^ - 1 (4294967295, 每个集合可存储40多亿个成员)。

1. 设置
    - 向有序集合添加一个或多个成员，或者更新已存在成员的分数  
    `ZADD key score1 member1 [score2 member2]`
2. 获取
    - 通过索引区间返回有序集合指定区间内的成员  
    `ZRANGE key start stop [WITHSCORES]`
    - 获取有序集合的成员数  
    `ZCARD key`
    - 计算在有序集合中指定区间分数的成员数  
    `ZCOUNT key min max`
    - 返回有序集中，成员的分数值  
    `ZSCORE key member`

## 补充

上文中说，集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是O(1)其实不太准确。

其实在redis sorted sets里面当items内容大于64的时候同时使用了hash和skiplist两种设计实现。这也会为了排序和查找性能做的优化。所以如上可知：

- 添加和删除都需要修改skiplist，所以复杂度为O(log(n))。
- 但是如果仅仅是查找元素的话可以直接使用hash，其复杂度为O(1)
- 其他的range操作复杂度一般为O(log(n))
- 当然如果是小于64的时候，因为是采用了ziplist的设计，其时间复杂度为O(n)
