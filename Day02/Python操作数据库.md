## 安装

Python3 MySQL 数据库连接 - PyMySQL 驱动

PyMySQL 是在 Python3.x 版本中用于连接 MySQL 服务器的一个库，Python2中则使用mysqldb。


```
pip3 install PyMySQL
```

## 案例

这里以查询秒杀商品数据为例：

```
#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "seckill")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT * FROM seckill")

# 使用 fetchall() 方法获取s所有数据.
data = cursor.fetchall()

print(data)

# 关闭数据库连接
db.close()
```
