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
from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):<!--继承AbstractUer类，拓展字段。需要在setting.py中声明AUTH_USER_MODEL = 'cms.UserProfile'-->
    ...
    
class Category(models.Model):
    ...

class Article(models.Model):
	...

class Comment(models.Model):
    ...

class Poll(models.Model):
    ...

class Keep(models.Model):
    ...
```
```
manage.py@django_cms > makemigrations<!--makemigration让django确定该如何修改数据库，记录并输出一个迁移文件-->
manage.py@django_cms > migrate<!--真正的操作数据库文件，生产对应的表-->
```
## 5、后台管理
django的admin模块可以方便我们管理数据库，实现类似数据库客户端的功能，对数据进行增删改查。我们还可以使用xadmin来替换admin，xadmin具有更友好，更强大的管理功能。[xadmin](https://github.com/sshwsfc/xadmin)
### xadmin安装方法
1、`pip install xadmin`or`pip install git+git://github.com/sshwsfc/xadmin.git`
2、源码安装，从github上下载源码下来放进项目中，并安装目录下有一个`requirements.txt`文件
源码安装方便后期拓展插件，所以本项目使用源码安装。
### 安装
在项目的根目录下创建一个文件夹extra_apps，将xadmin源码包中的'xadmin'文件夹复制到刚才的extra_apps中，把extra_apps Mark as Sources文件夹，在settings.py中添加`sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))`
取出`requirements.txt`文档
执行`(cms) E:\PycharmProjects\django_cms\extra_apps\xadmin>pip install -r requirements.txt`
在APPS中添加
```
INSTALLED_APPS = [
    ...
    'xadmin',
    'crispy_forms',
    'reversion',
]
```
中文支持
```
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_TZ = False
```
### 配置
在`urls.py`配置中替换
```
import xadmin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
]
```