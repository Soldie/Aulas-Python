## 准备工作


```
# 安装 Web 框架 
pip install Django
# 创建一个项目
python  django-admin.py startproject itstyle
# 切换目录
cd itstyle
 # 创建  App
python manage.py startapp novel
```

一般一个项目有多个app, 当然通用的app也可以在多个项目中使用。然后启动服务：

```
# 默认端口是8000
python manage.py runserver
```

如果提示端口被占用，可以用其它端口：

```
python manage.py runserver 8001
python manage.py runserver 8002
```

## 项目结构

win下使用命令 tree /F > 项目结构图.txt ，如下：


```
│  manage.py
│  
├─novel
│  │  settings.py # 基础配置
│  │  urls.py     # URL映射
│  │  wsgi.py
│  │  __init__.py
│  │  
│          
├─templates # 相关页面
│      novel.html # 章节
│      novel_list.html # 小说首页
│      
├─utils
│  │  dbMysqlConfig.cnf # 数据库配置参数
│  │  encoder.py # 编码类
│  │  mysql_DBUtils.py # 数据库连接池
│          
└─view
    │  index.py   # 后台业务        

```

