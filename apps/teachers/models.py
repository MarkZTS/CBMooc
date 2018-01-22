# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime


from django.db import models

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=64, verbose_name="教师名")
    work_years = models.IntegerField(default=0, verbose_name="工作年限")
    work_company = models.CharField(max_length=64, verbose_name="就职公司")
    work_position = models.CharField(max_length=64, verbose_name="公司职位")
    character = models.CharField(max_length=64, verbose_name="教学特点")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    avatar = models.ImageField(max_length=128, upload_to="teacher/%Y/%m", default="teacher/default.png",verbose_name="用户头像")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name

    # 获取该教师的课程数
    def get_course_nums(self):
        return self.course_set.all().count()

    def __str__(self):
        return self.name