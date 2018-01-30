#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 2018/1/30 13:55
# @Author : ZTS
# @Software: PyCharm

from django.conf.urls import url

from .views import TeacherListView, TeacherDetailView

urlpatterns = [
    url(r'^list/$', TeacherListView.as_view(), name='teacher_list'),
    url(r'^detail/(?P<teacher_id>\d+)/$', TeacherDetailView.as_view(), name='teacher_detail'),

]
