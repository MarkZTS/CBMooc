# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 12:24
# @Author  : ZTS
# @Software: PyCharm

from django.conf.urls import url, include

from .views import PraticeListView, PracticeDetailView, PraticeInfoView, NextQuestionView

urlpatterns = [
    # 在线练习列表
    url(r'^list/$', PraticeListView.as_view(), name='practice_list'),

    # 在线练习详情
    url(r'^detail/(?P<choice_id>\d+)/$', PracticeDetailView.as_view(), name='practice_detail'),

    # 在线练习做题详情
    url(r'^info/(?P<choice_id>\d+)/$', PraticeInfoView.as_view(), name='practice_info'),

    # 在线练习下一题
    url(r'^next/$', NextQuestionView.as_view(), name='next_question'),
]