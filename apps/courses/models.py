# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from teachers.models import Teacher

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"课程名")
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    detail = models.TextField(verbose_name=u"课程详情")
    degree_choices = (
        (0, u"初级"),
        (1, u"中级"),
        (3, u"高级"),
    )
    degree = models.SmallIntegerField(choices=degree_choices, verbose_name=u"难度")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长（分钟数）")
    teacher = models.ForeignKey(Teacher, verbose_name=u"授课教师", null=True, blank=True)
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"封面图", max_length=128)
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    category = models.CharField(max_length=20, verbose_name=u"课程类别", default=u"后端开发")
    course_known = models.CharField(max_length=300, verbose_name=u"课程须知", default=u"")
    teacher_tell = models.CharField(max_length=300, verbose_name=u"学习到的技能", default=u"")
    tag = models.CharField(max_length=10, verbose_name=u"课程标签", default="")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    def get_lesson_nums(self):
        '''获取章节数'''
        return self.lesson_set.all().count()

    def get_learn_users(self):
        '''获取学习用户'''
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        '''获取课程章节数'''
        return self.lesson_set.all()

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=128, verbose_name=u"章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def get_lesson_video(self):
        '''获取章节视频'''
        return self.video_set.all()

    def __unicode__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节")
    name = models.CharField(max_length=128, verbose_name=u"视频名")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长（分钟数）")
    url = models.CharField(max_length=200, default="", verbose_name=u"访问地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=128, verbose_name=u"名称")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u"资源文件", max_length=128)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name