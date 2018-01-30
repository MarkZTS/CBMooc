# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from teachers.models import Teacher

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name="课程名")
    desc = models.CharField(max_length=300, verbose_name="课程描述")
    detail = models.TextField(verbose_name="课程详情")
    degree_choices = (
        (0, "初级"),
        (1, "中级"),
        (2, "高级"),
    )
    degree = models.SmallIntegerField(choices=degree_choices, verbose_name="难度")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长（分钟数）")
    teacher = models.ForeignKey(Teacher, verbose_name="授课教师", null=True, blank=True)
    students = models.IntegerField(default=0, verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name="封面图", max_length=128)
    is_banner = models.BooleanField(default=False, verbose_name="是否轮播")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    category = models.CharField(max_length=20, verbose_name="课程类别", default="后端开发")
    course_known = models.CharField(max_length=300, verbose_name="课程须知", default="")
    teacher_tell = models.CharField(max_length=300, verbose_name="学习到的技能", default="")
    tag = models.CharField(max_length=10, verbose_name="课程标签", default="")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

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
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BannerCourse(Course):
    class Meta:
        verbose_name = "轮播课程"
        verbose_name_plural = verbose_name
        proxy = True


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程")
    name = models.CharField(max_length=128, verbose_name="章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name

    def get_lesson_video(self):
        '''获取章节视频'''
        return self.video_set.all()

    def __str__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name="章节")
    name = models.CharField(max_length=128, verbose_name="视频名")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长（分钟数）")
    url = models.CharField(max_length=200, default="", verbose_name="访问地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程")
    name = models.CharField(max_length=128, verbose_name="名称")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name="资源文件", max_length=128)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name