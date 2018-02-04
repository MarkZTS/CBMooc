#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 2018/1/22 21:45
# @Author : ZTS
# @Software: PyCharm

from django.conf.urls import url

from .views import UserInfoView, UploadImageView, UpdatePwdView, SendEmailCodeView
from .views import UpdateEmailView, MyCourseView, MyFavTeacherView, MyFavCourseView, MymessageView
from .views import MyworkView, MyuploadView, AlreadyUploadView, AdoptUrlView

urlpatterns = [
    # 用户信息
    url(r'^info/$', UserInfoView.as_view(), name="user_info"),
    # 用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),
    # 用户中心个人修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),
    # 发送邮箱验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name="sendemail_code"),
    # 修改邮箱
    url(r'^update_email/$', UpdateEmailView.as_view(), name="update_email"),
    # 我的课程
    url(r'^mycourse/$', MyCourseView.as_view(), name="mycourse"),
    # 收藏的授课讲师
    url(r'^myfav/teacher/$', MyFavTeacherView.as_view(), name="myfav_teacher"),
    # 收藏的课程
    url(r'^myfav/course/$', MyFavCourseView.as_view(), name="myfav_course"),
    # 我的消息
    url(r'^mymessage/$', MymessageView.as_view(), name="mymessage"),
    # 我的作业
    url(r'^mywork/$', MyworkView.as_view(), name="mywork"),
    # 上传视频
    url(r'^myupload/url/$', MyuploadView.as_view(), name="myupload"),
    # 我的上传视频
    url(r'^already/url/$', AlreadyUploadView.as_view(), name="already_upload"),
    # 我通过上传视频
    url(r'^adopt/url/$', AdoptUrlView.as_view(), name="adopt_url"),

]