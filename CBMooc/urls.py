"""CBMooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib import admin
import xadmin
from django.views.static import serve

from users.views import LogoutView, LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView
from CBMooc.settings import MEDIA_ROOT
from users.views import IndexView, OnlineCodeView, OnResultView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    url(r'^modify/$', ModifyPwdView.as_view(), name="modify_pwd"),
    # 在线编程
    url(r'^online/$', OnlineCodeView.as_view(), name="online"),

    # 在线编程结果
    url(r'^on_result/$', OnResultView.as_view(), name="on_result"),


    # 课程url配置
    url(r'^course/', include('courses.urls', namespace="course")),

    # 讲师url配置
    url(r'^teacher/', include('teachers.urls', namespace="teacher")),

    # 练习url配置
    url(r'^practice/', include('practice.urls', namespace="practice")),

    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),


    # url(r'^static/(?P<path>.*)$', serve, {"document_root":STATIC_ROOT}),

    # 用户相关url配置
    url(r'^users/', include('users.urls', namespace="users")),

    # 第三方登陆
    url('', include('social_django.urls', namespace='social'))
]

# 全局404页面配置
handler404 = 'users.views.page_not_found'
# 全局500页面配置
handler500 = 'users.views.page_error'

