# django-cms 使用django搭建的内容管理系统
## Tools:
IDE: Pycharm
数据库：MySQL5.7 管理工具：SQLyog

操作系统：windows10
Python版本：3.6
django版本：1.11
版本管理工具: virtualenv

## 1、使用virtualenv搭建Python开发虚拟环境
```
E:\pylenv>virtualenv cms
Using base prefix 'e:\\anaconda3'
New python executable in E:\pylenv\cms\Scripts\python.exe
Installing setuptools, pip, wheel...done.
```
## 2、启动该虚拟环境并安装django
```
E:\pylenv\cms\Scripts>activate.bat

(cms) E:\pylenv\cms\Scripts>pip install django
Collecting django
  Downloading Django-1.11.7-py2.py3-none-any.whl (6.9MB)
    100% |████████████████████████████████| 7.0MB 11kB/s
Collecting pytz (from django)
  Using cached pytz-2017.3-py2.py3-none-any.whl
Installing collected packages: pytz, django
Successfully installed django-1.11.7 pytz-2017.3
若下载缓慢，可换安装源
(cms) E:\pylenv\cms\Scripts>pip install -i https://pypi.tuna.tsinghua.edu.cn/simple django
https://pypi.tuna.tsinghua.edu.cn/simple清华大学的pip源
```
## 3、使用Pycharm创建django项目
![](gitpic/01.png)
使用Tools-Run manage.py Task ——>输入`startapp cms`创建APP
![](gitpic/02.png)
在setting注册APP
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cms',
]
```
创建CMS数据库并在setting.py中配置Mysql
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cms',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```
Python3.X连接MySQL需要安装pymysql包：
```
(cms) E:\PycharmProjects\django_cms>pip install pymysql
Collecting pymysql
  Using cached PyMySQL-0.7.11-py2.py3-none-any.whl
Installing collected packages: pymysql
Successfully installed pymysql-0.7.11
```
在`django_cms/__init__.py`中配置pymysql
```
import pymysql
pymysql.install_as_MySQLdb()
```
## 4、项目分析与建立数据模型
### 4.1、项目分析
在构建数据模型前需要先分析项目需求。
cms(Content Management System内容管理系统) 这个项目主要功能：
1>,文章的呈现：包括标题，内容，作者，评论，赞同数，收藏数。
2>,注册用户信息：昵称，邮箱，密码，简介，收藏了的文章，赞同了的文章，评论了的文章。
我们允许用户对一篇文章多次评论；但点赞和收藏的操作一篇文章只能进行一次，为了实现这一点，需要知道每篇文章和每个用户的对应关系(是否已点赞，是否已收藏)。
我们创建用户和文章，评论三个数据模型，让用户和文章关联成多对多的关系，从而判断用户是否已经收藏了某篇文章，另外创建一个点赞的数据模型，来判断用户是否已经赞同过某篇文章。
### 4.2、建立数据模型
在cms/models.py中完成模型字段的设计，并完成数据库的生成。
```
manage.py@django_cms > makemigrations<!--makemigration让django确定该如何修改数据库，记录并输出一个迁移文件-->
manage.py@django_cms > migrate<!--真正的操作数据库文件，生产对应的表-->
```