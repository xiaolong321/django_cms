from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='昵称')
    desc = models.CharField(max_length=100, verbose_name='简介', null=True, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nick_name


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='文章分类')

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey('Category', verbose_name='分类', null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name='标题')
    author = models.ForeignKey('UserProfile', verbose_name='作者')
    content = models.TextField(verbose_name='内容')
    poll_nums = models.IntegerField(default=0, verbose_name='点赞数')
    comment_nums = models.IntegerField(default=0, verbose_name='评论数')
    keep_nums = models.IntegerField(default=0, verbose_name='收藏数')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name


class Comment(models.Model):
    comment = models.TextField(verbose_name='评论内容')
    user = models.ForeignKey('UserProfile', verbose_name='评论人')
    article = models.ForeignKey('Article', verbose_name='评论文章')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    poll_nums = models.IntegerField(default=0, verbose_name='点赞数')

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name


class Poll(models.Model):
    user = models.ForeignKey('UserProfile', verbose_name='点赞人')
    poll_type = models.IntegerField(choices=((1, '文章'), (2, '评论')), default=0, verbose_name='点赞类型')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='点赞时间')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = '点赞'
        verbose_name_plural = verbose_name


class Keep(models.Model):
    user = models.ForeignKey('UserProfile', verbose_name='收藏人')
    article = models.ForeignKey('Article', verbose_name='收藏文章')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='收藏时间')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = '收藏'
        verbose_name_plural = verbose_name