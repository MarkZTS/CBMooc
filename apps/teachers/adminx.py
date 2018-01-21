# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 15:14
# @Author  : ZTS
# @Software: PyCharm
import xadmin

from .models import Teacher


class TeacherAdmin(object):
    list_display = ['name', 'work_years', 'work_company', 'work_position', 'fav_nums', 'add_time']
    search_fields = ['name', 'work_years', 'work_company', 'work_position', 'fav_nums']
    list_filter = ['name', 'work_years', 'work_company', 'work_position', 'fav_nums', 'add_time']

xadmin.site.register(Teacher, TeacherAdmin)
