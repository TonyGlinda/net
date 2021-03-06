# Mysql 高级
## 视图
- 视图是什么？
通俗的讲，视图就是一条select语句执行后返回的结果集。所以我们在创建视图的时候，
主要的工作就落在创建这条SQL查询语句上。
视图是对若干张基本表的引用，一张虚表，查询语句执行的结果，不存储具体的数据（基本
表数据发生了该表，视图也会跟着该表）；
方便操作，特别是查询操作，减少复杂的SQL语句，增强可读性。
- 定义视图
  - 建议以v开头 
  - create view 视图名称 as select语句；
- 查看视图
  - show tables；
- 使用视图
  - select * from 视图名称;
- 删除视图
  - drop view 视图名称;
- 视图的作用
  - 提高了重用性，就像函数。
  - 对数据库重构，却不影响程序的运行。
  - 提高了安全性，可以对不同的用户。
  - 让数据更加清晰。

 ## 事务
 - 什么是事务
 所谓事务，它是一个操作序列，这些操作要么都执行，要么都不执行，它是一个不可分割的
 工作单位。例如，银行转账。
 - 事务的四大特性（简称ACID）
 原子性（Atomicity）
 一致性（Consistency）
 隔离性（Isolation）
 持久性（Durability）
 - 事务的命令。
 表的引擎类型必须是Inodb类型才可以使用事务
  - start transaction; 或者 begin;   开始事务
  - commit; 确认上面的操作，提交事务。
  - rollback 撤销所有的修改，回滚事务。

## 索引
- 什么是索引
 - 索引是一种特殊的文件，他们包含着对数据表里所有记录的引用指针。
 更通俗的说，数据库索引好比是一本书前面的目录，能加快数据库的查询速度。
- 开启运行时间监测
 - set profiling=1;
 - demo: 查询第10000条数据。
 - show profiles; 查询执行的时间。
- 为表的某列创建索引：
 - create index 索引名 on 表名（字段()）
- 执行查询语句：
 - select * from 索引名 where 条件；
- 注意：
 - 建立太多的索引将会影响更新和插入的速度，因为它需要更新每个索引文件。


## 账户管理
## Mysql主从
