# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 15:18
# @Author  : ZTS
# @Software: PyCharm
import xadmin

from .models import UserAsk, UserCourse, UserMessage, CourseComment, UserFavorite, UserTeacher, TeacherUpload


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user__username', 'course__name', 'add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class CourseCommentAdmin(object):
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user__username', 'course__name', 'comments', 'add_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user__username', 'fav_id', 'fav_type', 'add_time']


class UserTeacherAdmin(object):
    # list_display = ['user', 'teacher', 'add_time']
    # search_fields = ['user', 'teacher']
    # list_filter = ['user__username', 'teacher__name', 'add_time']
    pass


class TeacherUploadAdmin(object):
    list_display = ['upload_url', 'user', 'course', 'lesson', 'is_adopt', 'add_time']
    search_fields = ['upload_url', 'user', 'course', 'lesson', 'is_adopt']
    list_filter = ['upload_url', 'user', 'course', 'lesson', 'is_adopt', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(CourseComment, CourseCommentAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserTeacher)
xadmin.site.register(TeacherUpload, TeacherUploadAdmin)