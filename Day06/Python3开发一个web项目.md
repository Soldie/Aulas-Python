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

