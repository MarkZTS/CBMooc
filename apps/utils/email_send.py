# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 17:02
# @Author  : ZTS
# @Software: PyCharm
import hashlib
import time
from random import Random
from django.core.mail import send_mail
from django.core.cache import cache

from users.models import EmailVerifyRecord
from CBMooc.settings import EMAIL_FROM


def send_register_email(email, send_type=0):
    email_record = EmailVerifyRecord()
    if send_type == 2:
        random_str = generate_random_str(4)
    else:
        random_str = generate_random_str(16)
    email_record.code = random_str
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == 0:# 发送类型为注册
        email_title = "畅编网注册激活链接"
        email_body = "请在一个小时以内点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}".format(random_str)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == 1:# 发送类型为忘记密码
        email_title = "畅编网密码重置链接"
        email_body = "请在一个小时以内点击下面的链接重置你的密码：http://127.0.0.1:8000/reset/{0}".format(random_str)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == 2:# 发送类型为修改邮箱
        email_title = "畅编网邮箱修改验证码"
        email_body = "你的验证码为：{0}".format(random_str)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass


def generate_random_str(randomlength=8):
    str = ''
    chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str