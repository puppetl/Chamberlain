Chamberlain
===============

A demo for hotel order booking system


Base on
-------

Python: 3.6+

Django: 3.0+

sqlite3

使用Pycharm将demo1导入
------

1. 安装模块

```bash
pip install -r requirements.txt
```

2. 同步数据库

```bash
python manage.py migrate
```

3. run server

```bash
 python manage.py runserver
```

4. 创建 超级用户 使用 **管理登录**, 进行房间/员工 添加, 预约信息查看

```
python manage.py createsuperuser	 
```

