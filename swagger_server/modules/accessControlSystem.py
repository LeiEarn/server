# -*- coding: utf-8 -*-
from flask import session, g
import threading
import functools
"""
访问控制
"""
class AccessControlSystem(object):
    _instance_lock = threading.Lock()
    app =None
    def __new__(cls, *args, **kwargs):
        if not hasattr(AccessControlSystem, "_instance"):
            with AccessControlSystem._instance_lock:
                if not hasattr(AccessControlSystem, "_instance"):
                    AccessControlSystem._instance = object.__new__(cls)  
        return AccessControlSystem._instance

    def __init__(self, app=None):
        if  self.app  is not None or app is  None:
            return 
        self.app = app
        self.add_func(app)
    
    @classmethod
    def add_func(cls, app):
        
        # 获取身份
        @app.before_request
        def get_identity():
            print('get_identity')
            if g.get('persistent') is None:
                return None
            print(g.get('persistent'))
            identity = g.get('persistent').get('user_type')
            if identity is not None:
                accesscontrol = {'identity': identity}
                g.accesscontrol = accesscontrol

    # 登录需求装饰器
    @classmethod
    def login_required(cls, redirect_to_login):
        """
        
        """
        print(redirect_to_login)
        def decp(view):
            def wrapped_view(*args, **kwargs):
                if g.get('accesscontrol') is  None or  g.get('accesscontrol').get('identity') is None:
                    return redirect_to_login
                return view(*args, **kwargs)
            return wrapped_view
        return decp

    # 拥有者身份需求装饰器
    @classmethod
    def owner_required(view, user_args='user_id', identity_error=('error', 'identity error')):
        """
            尚未完成
        """
        def dec(view):
            def wrapped_view(**kwargs):
                if g.user.get('user_id') is None or not str(g.user.user_id) ==  str(kwargs.get(user_args)):
                    return identity_error
                return view(**kwargs)
        return dec
    
    # 身份需求装饰器
    @classmethod
    def identity_required(view, identity_required = set('U'), identity_error=('error', 'identity error')):
        """
        example: identity_required(set('U', 'S'))
        """
        @functools.wraps(view)
        def wrapped_view(**kwargs):
            identity = g.get('identity')
            if 'U' in  identity_required :
                return view(**kwargs)
            elif identity['isprove'] is 'P' and identity['identity'] in identity_required:
                return view(**kwargs)
            
            return identity_error
        return wrapped_view
