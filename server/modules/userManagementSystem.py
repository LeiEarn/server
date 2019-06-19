from ..model.User import BasicUser as User
from flask import g, session
from ..utils import code2session

from .loginPersistentSystem import PersistentSystem as persistentSystem

class ManagementSystem:

    def __init__(self):
        pass
    
    """
        登录模块
        数据库获取【用户简单信息】，并返回
        session保存登录状态
        不存在则返回错误
    """
    def login(self, js_code):
        result = code2session(js_code)
        if 'error' in result:
            return None
        
        id =result.get('unionId')
        if id is None:
            return None
        user = User.table.query_user(id=id)
        if isinstance(user, User):
            result['identity'] = user.identity
            
            """
            persistent_info
            openid, unionid, session_key, user_type
            """
            persistentSystem.save(result)
            return user
        else:
            return None
        
    """
        注册模块
        先数据库查询用户【用户简单信息】，存在则返回错误
        数据库添加用户id

    """
    def register(self, id=id):
        user = User.table.query_user(id=id)
        if user is None:
            User.table.insert
            return None
        else:
            return user
    
    """
        获取信息模块
        ——可能包括详细信息
    """
    def get_user_info(self, id):
        user = User.table.query_user(id=id)
        if isinstance(User):
            return user
        else:
            return None

    def get_user_detail(self, id):
        pass