# MySQL 使用笔记

参考链接：  
[SQL](https://www.runoob.com/sql/sql-intro.html)  
[MySQL 教程](https://www.runoob.com/mysql/mysql-tutorial.html)  
[MySql数据库脚本规范（可重复执行的sql）](https://www.codeleading.com/article/63982246185/)  
[使 SQL 更易于阅读的几个小技巧](https://segmentfault.com/a/1190000023548293)  
[SQL编程格式的优化建议](https://zhuanlan.zhihu.com/p/27466166)  
[MySQL 规约](https://github.com/bingoohuang/blog/issues/68)  
[MySQL 中的数据类型](https://wiki.jikexueyuan.com/project/mysql-21-minutes/data.html)

## 基本语法

LIMIT 子句可以被用于强制 SELECT 语句返回指定的记录数。LIMIT 接受一个或两个数字参数。参数必须是一个整数常量。如果给定两个参数，第一个参数指定第一个返回记录行的偏移量，第二个参数指定返回记录行的最大数目。初始记录行的偏移量是 0(而不是 1)： 为了与 PostgreSQL 兼容，MySQL 也支持句法： LIMIT # OFFSET #。

```bash
mysql> SELECT * FROM table LIMIT 5,10; // 检索记录行 6-15  
  
//为了检索从某一个偏移量到记录集的结束所有的记录行，可以指定第二个参数为 -1：   
mysql> SELECT * FROM table LIMIT 95,-1; // 检索记录行 96-last.  
  
//如果只给定一个参数，它表示返回最大的记录行数目：   
mysql> SELECT * FROM table LIMIT 5; //检索前 5 个记录行  
  
//换句话说，LIMIT n 等价于 LIMIT 0,n。
```

## SQL INSERT INTO 语句

INSERT INTO 语句可以有两种编写形式。

- 第一种形式无需指定要插入数据的列名，只需提供被插入的值即可：

    ```sql
    INSERT INTO table_name
    VALUES (value1,value2,value3,...);
    ```

    注意：没有指定要插入数据的列名的形式需要列出插入行的每一列数据,insert 这种简写的方式虽然非常简单,但是 Values 后面的值必须和表中的类顺序对应,且类型要保持一致，即使表中某一个列不需要值也必须赋值为 null，比如我们的主键 id 设置的是递增实际上是不用设置值的,但是使用这种方式必须赋值为 null

    参考：[MySQL中插入语句(Insert)的几种使用方式](https://blog.csdn.net/qq_40194399/article/details/102462861)

- 第二种形式需要指定列名及被插入的值（无需指定 id 字段，id 字段会自动更新）：

    ```sql
    INSERT INTO table_name (column1,column2,column3,...)
    VALUES (value1,value2,value3,...);

    INSERT INTO table_name (column2,column3,...)
    VALUES (value2,value3,...);
    <!-- 插入多条数据 -->
    INSERT INTO table_name (column1,column2,column3,...)
    VALUES (value1,value2,value3,...),(value4,value5,value6,...);
    ```

## 关键字

嵌套子查询 in 的用法

`update salaries set salary=1.1*salary where salaries.to_date='9999-01-01' and salaries.emp_no in (select emp_no from emp_bonus);`

## 数据类型

在这些插入的数据中有些数据类型需要加引号，具体总结如下

- 字符串类型和日期类型：需要加引号 ('')
    如 CHAR、VARCHAR、TEXT、DATE、DATETIME、TIMESTAMP、YEAR、TIME 等数据类型的数据需要加引号
- 整数和浮点型的：不需要加
    如 TINYINT、SMALLINT、MEDIUMINT、INT、FLOAT、DOUBLE、DECIMAL 等

## 联表查询（左右连接、UNION 等）

[SQL中条件放在on后与where后的区别](https://www.cnblogs.com/itjeff/p/3524236.html)

## 索引

## 事务

[MySQL 事务](https://www.yiibai.com/mysql/transaction.html)

## 数据库脚本

引号和反引号的使用总结

## 引擎

## 优化

[参考](https://www.cnblogs.com/kex1n/archive/2010/03/26/2286504.html)
