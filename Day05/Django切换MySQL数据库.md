## 准备

| 软件 | 版本  | 
| ---- | ----- |
|   Django   | 2.1.3 |   
|   Python   |  3.7.1 |    


默认使用的是sqlite3

```
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
     }
}
```
切换为MySql：

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'book',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'POST': '3306',
    }
}
```

实现步骤：


