# MySQL
##  一、数据库简介。

## 二、数据类型和约束。

## 三、sql语句。
### 数据库的操作
 - 链接数据库。
   - mysql -uroot -pxc121538
   - mysql -uroot -p
 - sql语句最后需要以分号；结尾
 - 显示数据库版本。
   - select version();
 - 显示时间。
   - select now();
 - 查看所有数据库。
   - show databases;
 
 - 创建数据库。
   - create database name;
   - create database name charset=utf8; 
  
 - 查看创建出的数据库
   - show create database name;
   
 - 删除数据库。
   - drop database name;
 - 退出数据库。
   - exit
   - quit
   - ctrl + d
 - 查看正使用的数据库。
   - select database();
 - 使用数据库。
   - use 数据库名
### 数据表的操作
 - 查看数据库中所有的数据表。
  - show tables
  
 - 创建数据表。
  - create table 数据表的名字（字段 类型 约束 [，字段 类型 约束]）；
  - demo
  create table students(
  id int unsigned not null auto_increment primary key,
  name varchar(30),
  age tinyint unsigned default 0,
  high decimal(5,2),
  gender enum("男","女"，"保密") default "保密",
  cls_id int unsigned
  );
 - 查看表的结构。
  - desc 表的名字；
   - desc students;
 
 - 查询创建的表的语句。
   - show create table students;
  
 - 修改表--添加字段。
   - alter table 表名 add 列名 类型；
  
 - 修改表--修改字段--不重名版。
   - alter table 表名 modify 列名 类型 ；
   
 - 修改表--修改字段--重名版。
   - alter table 表名 change 原名 新名 类型及约束；
   
 - 修改表--删除字段
   - alter table 表名 drop 列名；
  
 - 删除表
   - drop table 表名;
    
    
 - 数据的增删改查（curd）
   - 插入数据
     - insert into 表名 values(值1，值2，····);
   - 部分插入数据
     - insert into 表名(列1···) values(值1····)；
   - 多行插入数据
    - insert into 表名（列1···） values(值1···),(值2···)；

   - 修改数据
     - update 表名 set 列1=值1，列2=值2···where 条件;
     
     
   - 查询数据
     - 查询所有列
       - select * from 表名；
     - 指定条件查询
       - 比较运算符（><=)、逻辑运算符(and.or.not)、模糊查询、范围查询
       - 比较运算符
         - select * from 表名 where 条件;
       - 模糊查询
         - like
         - % 替换1个或者多个。
         - _替换1个
         - select name from students where name like '小%';
         
         - rlike 正则
         - select name from students where name rlike '^周.*';
       - 范围查询
         - in(12,18,34)非连续性的范围内
         - not in   不在非连续性的范围内的
         - between...and...  表示连续性的范围
         - not between...and... 表示不在连续范围内的
         - 错误 not (between...and...) 语法错误
         - 空判断
           - 判断空 is null
           - 判断非空 is not null
           
       - 排序查询
         - order by 字段
         - asc 从小到大，即升序。
           - select * from students where age<18 order by age asc;
         - desc 从大到小，即降序。
           - select * from students where age<18 order by age desc;
         - order by 多个字段
           - select * from students where age<18 order by age desc，id desc;
       - 聚合
         - 总数计算 count
           - select count(*) from students where gender='women';
         - 求最大值 max
           - select max(age) from students where gender='women';
         - 求最小值 min
           - select min(age) from students where gender='women';
         - 求和 sum
           - select sum(age) from students where gender='women';
         - 求平均值 avg
           - select avg(age) from students where gender='women';
         - 四舍五入 round
           - select round(avg(age)) from students where gender='women';
           - 错误语法select name,round(avg(age)) from students where gender='women';
           
       - 分组
         - group by 字段    通常分组要和聚合配合使用
         - select age,count(*) from students group by age;
         - group_concat() 显示具体的内容。
         - select age,group_concat(age) from students where gender='woman' group by age;
         - select gender,group_concat(name,age,id) from heros where gender='women' group by gender;
         
         - having 对分组进行条件判断，对查询结果进行判断。where是对原表进行判断。
           - select avg(age),gender,group_concat(name,age,id) from heros group by gender having avg(age)<28;
       - 分页
         - limit start count
         - limit (第N页-1)*每页的个数，每页的个数
         - limit 始终在语句的最后。
         
       - 链接查询
         - 内链接（交集）
         - inner join...on 条件
         - select ...from 表A inner join 表B；
         - select name,gender,age,cls_name  from heros as h inner join class as c on h.class=c.cls_name order by cls_name;
         
         - 左链接 left join...on条件
         - 以left左边的表作为基准去对应另外的表。
         
     - 查询指定列
       - select 列名1，列名2··· from 表名；
     - 可以使用as为列和表取别名
       - select name as '姓名',age as ‘年龄’ from students;
     - 字段的顺序
      - select age as ‘年龄’,name as '姓名', from students;
     - 消除重复行
       - distinct 字段
       - select distinct age from students

   - 删除数据
     - 物理删除
     - delete from 表名 where 条件;
     
     - 逻辑删除
     - 用一个字段来表示这个字段是否已经不能再使用了
     - 给students表添加一个字段is_delete 类型bit
     - alter table students add is_delete bit default 0;
     - update students set is_delete=1 where id=6;


- 外键
  - 对数据的有效性进行验证。
  - 关键字 foreign key
  - alter table goods add foreign key (cate_id) reference goods_cate(id);
  - 在实际开发中，尽量少使用外键。
  - 删除外键约束
  - alter table goods drop foreign key 外键名称；
  
