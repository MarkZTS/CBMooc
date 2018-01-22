# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 11:11
# @Author  : ZTS
# @Software: PyCharm

from django.conf.urls import url

from .views import CourseListView, CourseDetailView, AddFavView, CourseInfoView, CommentsView, AddCommentsView

urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),
    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)$', CourseDetailView.as_view(), name="course_detail"),
    # 章节信息页
    url(r'^info/(?P<course_id>\d+)$', CourseInfoView.as_view(), name="course_info"),
    # 课程评论
    url(r'^commment/(?P<course_id>\d+)$', CommentsView.as_view(), name="course_comment"),
    # 添加课程评论
    url(r'^add_comment/$', AddCommentsView.as_view(), name="add_comment"),

    # 课程收藏
    url(r'^add_fav/$', AddFavView.as_view(), name="add_fav"),
]