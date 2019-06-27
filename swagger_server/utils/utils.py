# -*- coding: utf-8 -*-
import requests
import urllib3
import uuid
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
APP_ID = 'wx72ce1b28ca748994'
APP_SECRET = '733540bdf3bf7aef48fa1e1ccd157db9'
AUTHORIZATION_CODE = 'authorization_code'
WX_API_URL = 'https://api.weixin.qq.com/sns/jscode2session' 


def dump_data(file):
    file_name =str(uuid.uuid4())
    with open("./static/{file_name}.json".format(file_name=file_name),"w") as f:
        json.dump(file,f)
        return file_name
    return None
def load_data(file_name):
    with open("./static/{file_name}.json".format(file_name=file_name),"r") as f:
        data = json.load(f)
        return data
    return None




def code2session(js_code, app_id, app_secret):
    # 不存在js_code的错误处理
    if js_code is None:
        return {'error': 'no js_code'}
    # 存在js_code则向微信服务器发起获取信息请求
    user_info = get_user_info(js_code,app_id, app_secret)
    # js_code无效的处理
    if user_info is None:
        return {'error': 'js_code invalid'}

    # 从返回信息中获取需要的id，需要异常处理++
    try:
        print(user_info)
        if  'errcode' in user_info :
            return 'jscode or wechat server error\n ' + user_info.get('errmsg')
        else:
            openid = user_info.get('openid')
            unionid = user_info.get('unionid')
            session_key = user_info.get('session_key')

        if openid is None:
            return {'error': 'no unionid'}

        return {
            'openid': openid,
            'unionid': openid,
            'session_key': session_key
        }
    except Exception as e :
        print(e)

# 利用js_code向微信服务器端发起请求获取用户信息
#  返回json格式
def get_user_info(js_code, app_id, app_secret ):
    req_params = {
        "appid": APP_ID,  # 小程序的 ID
        "secret": APP_SECRET,  # 小程序的 secret
        "js_code": js_code,
        "grant_type": AUTHORIZATION_CODE
    }
    req_result = requests.get(
        WX_API_URL, 
        params=req_params, 
        timeout=3, 
        verify=False)
    return req_result.json()
    