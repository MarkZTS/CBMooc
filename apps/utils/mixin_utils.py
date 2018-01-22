# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 14:49
# @Author  : ZTS
# @Software: PyCharm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginRequiredMixin(object):

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)