from datetime import datetime

from django.db import models

from courses.models import Lesson, Course

# Create your models here.


class ChoiceQuestion(models.Model):
    name = models.CharField(max_length=50, verbose_name="选择题目")
    desc = models.CharField(max_length=120, null=True, blank=True, verbose_name="题库描述")
    students = models.IntegerField(default=0, verbose_name="练习人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    degree_choices = (
        (0, "易"),
        (1, "中"),
        (2, "难"),
    )
    degree = models.SmallIntegerField(choices=degree_choices, verbose_name="难度", default=0)
    pratice_times = models.IntegerField(default=0, verbose_name="建议练习时长(分钟数)")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    image = models.ImageField(upload_to="practice/%Y/%m", verbose_name="封面图", max_length=128)
    course = models.ForeignKey(Course, verbose_name="课程", null=True, blank=True)
    lesson = models.ForeignKey(Lesson, verbose_name="章节")
    analysis = models.TextField(verbose_name="答案解析")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "选择题库"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Choice(models.Model):
    choicequestion = models.ForeignKey(ChoiceQuestion, verbose_name="选择题目")
    choice_name = models.CharField(max_length=50, verbose_name="选项题目")
    choiceA = models.CharField(max_length=50, verbose_name="选项A")
    choiceB = models.CharField(max_length=50, verbose_name="选项B")
    choiceC = models.CharField(max_length=50, verbose_name="选项C")
    choiceD = models.CharField(max_length=50, verbose_name="选项D")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "选项"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.choice_name


class Programming(models.Model):
    name = models.CharField(max_length=50, verbose_name="选择题目")
    desc = models.TextField(verbose_name="题目描述")
    analysis = models.TextField(verbose_name="解题思路")
    students = models.IntegerField(default=0, verbose_name="练习人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    download = models.FileField(upload_to="pracitce/resource/%Y/%m", verbose_name="项目文件", max_length=128)
    image = models.ImageField(upload_to="practice/%Y/%m", verbose_name="封面图", max_length=128)
    lesson = models.ForeignKey(Lesson, verbose_name="章节")
    course = models.ForeignKey(Course, verbose_name="课程", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "编程题库"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
