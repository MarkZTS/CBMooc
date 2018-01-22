#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 2018/1/22 21:45
# @Author : ZTS
# @Software: PyCharm

from django.conf.urls import url

from .views import UserInfoView

urlpatterns = [
    # 用户信息
    url(r'^info/$', UserInfoView.as_view(), name="user_info"),
]