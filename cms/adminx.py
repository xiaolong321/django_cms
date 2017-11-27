# -*- coding:utf-8 -*-
__author__ = 'John 2017/11/27 10:52'

import xadmin
from xadmin import views

from .models import Category, Article, Comment, Poll, Keep


class ArticleAdmin(object):
    list_display = (
        'category', 'title', 'author', 'content', 'poll_nums', 'comment_nums', 'keep_nums', 'add_time', 'update_time'
    )
    list_filter = (
        'category', 'title', 'author', 'content', 'poll_nums', 'comment_nums', 'keep_nums', 'add_time', 'update_time'
    )
    search_fields = (
        'category', 'title', 'author', 'content', 'poll_nums', 'comment_nums', 'keep_nums', 'add_time'
    )


class CategoryAdmin(object):
    list_display = ('name', 'add_time')
    list_filter = ('name', 'add_time')
    search_fields = ('name', 'add_time')


class CommentAdmin(object):
    list_display = ('comment', 'user', 'article', 'poll_nums', 'add_time')
    list_filter = ('comment', 'user', 'article', 'poll_nums', 'add_time')
    search_fields = ('comment', 'user', 'article', 'poll_nums', 'add_time')


class PollAdmin(object):
    list_display = ('user', 'poll_type', 'add_time')
    list_filter = ('user', 'poll_type', 'add_time')
    search_fields = ('user', 'poll_type', 'add_time')


class KeepAdmin(object):
    list_display = ('user', 'article', 'add_time')
    list_filter = ('user', 'article', 'add_time')
    search_fields = ('user', 'article', 'add_time')


xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Comment, CommentAdmin)
xadmin.site.register(Poll, PollAdmin)
xadmin.site.register(Keep, KeepAdmin)


# class BaseSetting(object):
#     enable_themes = True
#     use_bootswatch = True
#
#
# class GlobalSettings(object):
#     site_title = '后台管理系统'
#     site_footer = 'CMS'
#     menu_style = 'accordion'
#
#
# xadmin.site.register(views.BaseAdminView, BaseSetting)
# xadmin.site.register(views.CommAdminView, GlobalSettings)