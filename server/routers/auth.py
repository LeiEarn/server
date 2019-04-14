import functools
import flask_login
import requests
import json
from flask import (
    Blueprint, flash, redirect, request, session, g, url_for
)




APP_ID = ''
APP_SECRET = ''
AUTHORIZATION_CODE = ''
WX_API_URL = 'https://api.weixin.qq.com/sns/jscode2session' 


auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth_bp')

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth_bp.login'))
        return view(**kwargs)
    return wrapped_view


@auth_bp.route('/register', methods=('GET', 'POST'))
def register():
    return 'register'


@auth_bp.route('/login', methods=('GET', 'POST'))
def login():
    js_code = request.args.get('js_code')
    user_info = get_user_info(js_code)

    
    return user_info


@auth_bp.route('/logout')
@login_required
def logout():
    return 'logout'


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