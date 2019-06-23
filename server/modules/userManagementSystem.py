from ..model.User import User as User
from flask import g, session
from ..utils import code2session

from .loginPersistentSystem import PersistentSystem as persistentSystem

class ManagementSystem:

    def __init__(self):
        pass
    

    def login(self, js_code):
        """
            登录模块， 小程序启动即刻调用
            数据库获取【用户简单信息】，并返回
            session保存登录状态
            不存在则返回错误
        
        Parameters:
            js_code: 小程序端发来的token,用于从微信服务器获取unionid
        
        Returns:
            用户信息 or None

        """
        wechatresult = code2session(js_code)
        if 'error' in wechatresult:
            return None
        
        unionid =wechatresult.get('unionid')
        if id is None:
            return None
        user = User.table.query_user_unionid(unionid=unionid)
        if isinstance(user, User.BasicUser):
            
            """
            persistent_info
            openid, unionid, session_key, user
            """
            persistentSystem.save(wechat_server_reply= wechatresult, user = user)
            return user
        else:
            return None
        

    def register(self, unionid=None):
        """
            注册模块,小程序启动时，在用户不存在时使用
            先数据库查询用户【用户简单信息】，存在则返回错误
            数据库添加用户id

        Parameters:
            id: unionid登录时获得

        """
        user = User.table.query_user_unionid(unionid=unionid)
        if user is None:
            user = User.table.create_new_user(id)
            return user
        else:
            return user
    
    
    def prove(self, unionid, *args, **kwargs):
        """
            用户发起认证请求
        """
        user = User.table.query_user_unionid(unionid=unionid)
        
        if user is None:
            return None
        elif user.isprove is 'P':
            return None
        
        result = User.table.update_detail(unionid = unionid)
        return result
        pass


    """
        获取信息模块
    """
    def get_user_info(self, userid):
        user = User.table.query_user_userid(userid=userid)
        if isinstance(User.BasicUser):
            return user
        else:
            return None

    def get_user_detail(self, userid):
        detail = User.table.load_detail_userid(userid = userid)
        return detail
        pass