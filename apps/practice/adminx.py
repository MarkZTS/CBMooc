# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 13:14
# @Author  : ZTS
# @Software: PyCharm

import xadmin

from .models import ChoiceQuestion, Programming, Choice

class ChoiceQuestionAdmin(object):
    list_display = ['name', 'students', 'fav_nums', 'pratice_times', 'click_nums', 'image',
                    'lesson', 'course',  'analysis', 'add_time']
    search_fields = ['name', 'students', 'fav_nums', 'pratice_times', 'click_nums', 'image',
                    'lesson', 'course', 'analysis']
    list_filter = ['name', 'students', 'fav_nums', 'pratice_times', 'click_nums', 'image',
                    'lesson__name', 'course__name', 'analysis', 'add_time']


class ChoiceAdmin(object):
    list_display = ['choicequestion', 'choice_name', 'choiceA', 'choiceB', 'choiceC', 'choiceD', 'add_time']
    search_fields = ['choicequestion', 'choice_name', 'choiceA', 'choiceB', 'choiceC', 'choiceD']
    list_filter = ['choicequestion', 'choice_name', 'choiceA', 'choiceB', 'choiceC', 'choiceD', 'add_time']


class ProgrammingAdmin(object):
    list_display = ['name', 'desc', 'analysis', 'students', 'fav_nums', 'click_nums', 'download',
                    'image', 'lesson', 'course', 'add_time']
    search_fields = ['name', 'desc', 'analysis', 'students', 'fav_nums', 'click_nums', 'download',
                    'image', 'lesson', 'course']
    list_filter = ['name', 'desc', 'analysis', 'students', 'fav_nums', 'click_nums', 'download',
                    'image', 'lesson__name', 'course__name', 'add_time']


xadmin.site.register(ChoiceQuestion, ChoiceQuestionAdmin)
xadmin.site.register(Choice, ChoiceAdmin)
xadmin.site.register(Programming, ProgrammingAdmin)