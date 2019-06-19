
import requests
APP_ID = 'wx2e515a1b9f28a15e'
APP_SECRET = 'ded301bbd914c7a4083d15326be60073'
AUTHORIZATION_CODE = 'authorization_code'
WX_API_URL = 'https://api.weixin.qq.com/sns/jscode2session' 

def code2session(js_code):
    # 不存在js_code的错误处理
    if js_code is None:
        return {'error': 'no js_code'}
    # 存在js_code则向微信服务器发起获取信息请求
    user_info = get_user_info(js_code)
    # js_code无效的处理
    if user_info is None:
        return {'error': 'js_code invalid'}

    # 从返回信息中获取需要的id，需要异常处理++
    try:
        if  'errcode' in user_info :
            return 'jscode or wechat server error\n ' + user_info.get('errmsg')
        else:
            openid = user_info.get('openid')
            unionid = user_info.get('unionid')
            session_key = user_info.get('session_key')

        if unionid is None:
            return {'error': 'no unionid'}

        return {
            'openid': openid,
            'unionid': unionid,
            'session_key': session_key
        }
    except Exception as e :
        print(e)

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
    