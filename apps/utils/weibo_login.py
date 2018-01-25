# -*- coding: utf-8 -*-
# @Time    : 2018/1/25 11:12
# @Author  : ZTS
# @Software: PyCharm


def get_auth_url():
    weibo_auth_url = "https://api.weibo.com/oauth2/authorize"
    redirect_url = "http://127.0.0.1/complete/weibo"
    auth_url = weibo_auth_url + "?client_id={client_id}&redirect_uri={re_url}".format(client_id=1281568277, re_url=redirect_url)
    print(auth_url)


def get_access_token(code="f8b5ebef567513070eb91a91389d5176"):
    access_token_url = "https://api.weibo.com/oauth2/access_token"
    import requests
    re_dict = requests.post(access_token_url, data={
        "client_id":1281568277,
        "client_secret":"d6d3302f3458753ce628811583eace95",
        "grant_type":"authorization_code",
        "code":code,
        "redirect_uri":"http://127.0.0.1/complete/weibo",
    })

    # b'{"access_token":"2.00rwFfMDF91j5B6a087761b28HkJXB","remind_in":"157679999","expires_in":157679999,"uid":"2935508845","isRealName":"true"}'
    pass


def get_user_info(access_token="", uid=""):
    user_url = "https://api.weibo.com/2/users/show.json?access_token={token}&uid={uid}".format(token=access_token, uid=uid)
    print(user_url)



if __name__ == '__main__':
    # get_auth_url()
    # get_access_token(code="b74cede4902b224a4d5fd6759cc2db15")

    get_user_info(access_token="2.00rwFfMDF91j5B6a087761b28HkJXB", uid="2935508845")