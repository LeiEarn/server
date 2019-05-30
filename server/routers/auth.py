import functools
import flask_login
import requests
import json
import uuid
from flask import (
    Blueprint, flash, redirect, request, session, g, url_for
)
from server.model import *
from server.UserManagement import UserManagement

APP_ID = 'wx2e515a1b9f28a15e'
APP_SECRET = 'ded301bbd914c7a4083d15326be60073'
AUTHORIZATION_CODE = 'authorization_code'
WX_API_URL = 'https://api.weixin.qq.com/sns/jscode2session' 


bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

user_manager = UserManagement()

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return 'redirect to login'
        return view(**kwargs)
    return wrapped_view

#######################################
#   小程序注册过程
#       1. 用户填写信息发送至小程序服务器, 需要附加js_code
#       2. 验证用户信息，以及js_code信息
#       3. 若信息无误，发送邮件认证
@bp.route('/register', methods=('GET', 'POST'))
def register():
    # 从request中获取js_code
    js_code = request.args.get('js_code')
    # 不存在js_code的错误处理
    if js_code == None:
        return "error, no jscode"

    # 存在js_code则向微信服务器发起获取信息请求
    user_info = get_user_info(js_code)
    # js_code无效的处理
    if user_info == None:
        return "error, no user_info"

    # 从返回信息中获取需要的id，需要异常处理++
    openid = user_info['openid']
    unionid = user_info['unionid']
    session_key = user_info['session_key']

    # 验证
    # 微信账号是否已被绑定
    # 学号，邮箱是否重复
    #  判断账号是否已被绑定
    user = User.query.filter_by(unionid=unionid).first()
    # 判断是否有关键字段与已注册账号重复
    
    # 用户存在则注册失败， 返回信息
    #  不存在冲突用户则发邮件验证
    if user: 
        pass
    else:
        pass

#######################################
#   小程序登录过程
#       1. 登录时用户端调用login，从微信服务器获取到jscode，
#       2. 用户端将jscode发送给小程序服务器
#       3. 小程序服务器用jscode 从微信服务器处获取到union等标识信息
#       4. 小程序服务器用union唯一认知用户是否存在
#       5. 当用户存在则登录成功，服务器生成uuid, 临时存储并返回uuid给用户端，
#               用户端用uuid发起其他请求标志处于session期间
#               
#       6. 用户不存在则转向注册界面
#   登录备注：
#       1. 是否处于session期间，需要重新登录由小程序服务器根据uuid判断，
#               正常情况下小程序不发起登录请求，直接用本地存储的uuid进行其他操作
#               在收到服务器端登录过期或者uuid错误的情况下才发起登录
#       2. 账号只能与一个小程序id绑定，即不可在第二个微信上登录
#######################################
@bp.route('/login', methods=('GET', 'POST'))
def login():
    # 不进行是否在session期间的判断
    # 从request中获取js_code
    js_code = request.args.get('js_code')
    # 不存在js_code的错误处理
    if js_code is None:
        return "error, no jscode"
    else:
        print(js_code)
    # 存在js_code则向微信服务器发起获取信息请求
    user_info = get_user_info(js_code)
    # js_code无效的处理
    if user_info is None:
        return "error, no user_info"
    else:
        print(user_info)
    # 从返回信息中获取需要的id，需要异常处理++
    try:
        if  'errcode' in user_info :
            return 'jscode or wechat server error\n ' + user_info.get('errmsg')
        else:
            openid = user_info.get('openid')
            print(openid)
            unionid = user_info.get('unionid')
            session_key = user_info.get('session_key')

            return  openid
    except Exception as e :
        print(e)
    
    # 验证是否存在该用户
    #user = User.query.filter_by(unionid=unionid).first()
    
    
    # 用户存在则登录成功， 返回信息，uuid uuid作为用户凭证
    # 不成功则提示未成功， 转到注册页面
    if user: 
        user_uuid = str(uuid.uuid4()) # 暴露给小程序端的用户标示
        pass
        # 登录成功
        # return user, uuid
    else:
        pass
        # 重定向到注册页面
        return 'redirect to register'



@bp.route('/logout')
@login_required
def logout():
    return 'logout'

# 利用js_code向微信服务器端发起请求获取用户信息
#  返回json格式
def get_user_info(js_code):
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