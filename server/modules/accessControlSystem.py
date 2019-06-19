from flask import session, g
import threading
import functools

class AccessControlSystem(object):
    _instance_lock = threading.Lock()
    app =None
    def __new__(cls, *args, **kwargs):
        if not hasattr(AccessControlSystem, "_instance"):
            with AccessControlSystem._instance_lock:
                if not hasattr(AccessControlSystem, "_instance"):
                    AccessControlSystem._instance = object.__new__(cls)  
        return AccessControlSystem._instance

    def __init__(self, app):
        if not self.app  is None:
            return 
        self.app = app
        self.add_func(app)
    

    def add_func(self, app):
        
        # 获取身份
        @app.before_request
        def get_identity():
            user = g.get('user')
            if user is not None:
                g.identity = user

    # 登录需求装饰器
    @classmethod
    def login_required(view):
        @functools.wraps(view)
        def wrapped_view(**kwargs):
            if g.get('user') is None:
                return 'redirect to login'
            return view(**kwargs)
        return wrapped_view
    
    # 身份需求装饰器
    @classmethod
    def identity_required(view, identity):
        @functools.wraps(view)
        def wrapped_view(**kwargs):
            user = g.get('user')
            if user is None:
                return 'redirect to login'
            elif isinstance(user, identity):
                return view(**kwargs)
            else:
                return 'error'
        return wrapped_view
