# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=64, verbose_name='昵称', default="")
    birthday = models.DateField(null=True, blank=True, verbose_name="生日")
    gender_choices = (
        (0, "男"),
        (1, "女"),
    )
    gender = models.SmallIntegerField(choices=gender_choices, default=0, verbose_name="性别")
    address = models.CharField(max_length=128, default="", verbose_name="地址")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name="手机号")
    avatar = models.ImageField(max_length=128, upload_to="image/%Y/%m", default="image/default.png", verbose_name="用户头像")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name="验证码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type_choices = (
        (0, "注册"),
        (1, "找回密码"),
        (2, "修改邮箱"),
    )
    send_type = models.CharField(choices=send_type_choices, max_length=10, verbose_name="发送类型")
    send_time = models.DateTimeField(default=datetime.now, verbose_name="发送时间") # 去掉now括号，根据实例化的时间生成，不然就是根据数据库生成的时间生成

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=128, verbose_name="标题")
    image = models.ImageField(upload_to="banner/%Y/%m", max_length=128, verbose_name="轮播图")
    url = models.URLField(max_length=200, verbose_name="访问地址")
    index = models.IntegerField(default=100, verbose_name="顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")# datetime.now()不去掉括号就是根据Banner这个model编译的时间生成时间，去掉括号datetime.noe就是根据class实例化的时间生成

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name