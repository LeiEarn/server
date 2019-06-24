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
        """test"""
        #wechatresult = code2session(js_code)
        #if 'error' in wechatresult:
        #   return None
        
        wechatresult = {'unionid': '12345', 'openid':1, 'session_key':'12345'}

        unionid =wechatresult.get('unionid')

        if unionid is None:
            return None
        else:
            print(unionid)
            user = User.table.query_user(unionid=unionid)
            print(user)
            if isinstance(user, User.BasicUser):
            
                """
                persistent_info
                openid, unionid, session_key, user
                """
                persistentSystem.save(wechat_server_reply= wechatresult, user = user)
                return user
            else:
                self.register(unionid=unionid)
                return None
        

    def register(self, unionid=None):
        """
            注册模块,小程序启动时，在用户不存在时使用
            先数据库查询用户【用户简单信息】，存在则返回错误
            数据库添加用户id

        Parameters:
            id: unionid登录时获得

        """
        if unionid is None:
            return None
        user = User.table.query_user(unionid=unionid)
        if user is None:
            User.table.create_new_user(unionid=unionid)
            user = User.table.query_user(unionid=unionid)
            return user
        else:
            return user
    
    
    def prove(self, unionid, *args, **kwargs):
        """
            用户发起认证请求
        """
        user = User.table.query_user(unionid=unionid)
        
        if user is None:
            return None
        elif user.isprove is 'P':
            return None
        
        result = User.table.update_detail(unionid = unionid, identity=g.accesscontrol.get('identity'))
        return result
        pass


    """
        获取信息模块
    """
    def get_user_info(self, userid):
        user = User.table.query_user(user_id=userid)
        if isinstance(User.BasicUser):
            return user
        else:
            return None

    def get_user_detail(self, user_id):
        detail = User.table.load_detail_user_id(user_id = user_id)
        return detail
        pass