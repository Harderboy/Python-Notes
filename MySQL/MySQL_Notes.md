# MySQL 使用笔记

参考链接：  
[SQL](https://www.runoob.com/sql/sql-intro.html)  
[MySQL 教程](https://www.runoob.com/mysql/mysql-tutorial.html)  
[MySql数据库脚本规范（可重复执行的sql）](https://www.codeleading.com/article/63982246185/)  
[使 SQL 更易于阅读的几个小技巧](https://segmentfault.com/a/1190000023548293)  
[SQL编程格式的优化建议](https://zhuanlan.zhihu.com/p/27466166)  
[MySQL 规约](https://github.com/bingoohuang/blog/issues/68)  
[MySQL 中的数据类型](https://wiki.jikexueyuan.com/project/mysql-21-minutes/data.html)

## SQL INSERT INTO 语句

INSERT INTO 语句可以有两种编写形式。

- 第一种形式无需指定要插入数据的列名，只需提供被插入的值即可：

    ```sql
    INSERT INTO table_name
    VALUES (value1,value2,value3,...);
    ```

    注意：没有指定要插入数据的列名的形式需要列出插入行的每一列数据（是否包含id字段？）。

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

## 数据类型

在这些插入的数据中有些数据类型需要加引号，具体总结如下

- 字符串类型和日期类型：需要加引号 ('')
    如 CHAR、VARCHAR、TEXT、DATE、DATETIME、TIMESTAMP、YEAR、TIME 等数据类型的数据需要加引号
- 整数和浮点型的：不需要加
    如 TINYINT、SMALLINT、MEDIUMINT、INT、FLOAT、DOUBLE、DECIMAL 等

## 联表查询（左右连接、UNION 等）

## 索引

## 事务

[MySQL 事务](https://www.yiibai.com/mysql/transaction.html)

## 数据库脚本

引号和反引号的使用总结

## 引擎

## 优化

[参考](https://www.cnblogs.com/kex1n/archive/2010/03/26/2286504.html)
