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
            identity = g.get('user_type')
            if identity is not None:
                g.identity = identity

    # 登录需求装饰器
    @classmethod
    def login_required(view, redirect_to_login):
        """
        
        """
        @functools.wraps(view)
        def wrapped_view(**kwargs):
            if g.get('identity') is None:
                return redirect_to_login
            return view(**kwargs)
        return wrapped_view
    
    # 身份需求装饰器
    @classmethod
    def identity_required(view, identity_required = set('U'), identity_error='needprove'):
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
