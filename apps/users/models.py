# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=64, verbose_name=u'昵称', default=u"")
    birthday = models.DateField(null=True, blank=True, verbose_name=u"生日")
    gender_choices = (
        (0, u"男"),
        (1, u"女"),
    )
    gender = models.SmallIntegerField(choices=gender_choices, default=0, verbose_name=u"性别")
    address = models.CharField(max_length=128, default=u"", verbose_name=u"地址")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u"手机号")
    avatar = models.ImageField(max_length=128, upload_to="image/%Y/%m", default=u"image/default.png", verbose_name=u"用户头像")

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type_choices = (
        (0, u"注册"),
        (1, u"找回密码"),
    )
    send_type = models.CharField(choices=send_type_choices, max_length=10)
    send_time = models.DateTimeField(default=datetime.now) # 去掉now括号，根据实例化的时间生成，不然就是根据数据库生成的时间生成

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=128, verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m", max_length=128, verbose_name=u"轮播图")
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")# datetime.now()不去掉括号就是根据Banner这个model编译的时间生成时间，去掉括号datetime.noe就是根据class实例化的时间生成

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name