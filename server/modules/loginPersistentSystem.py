#encoding=utf-8
import threading

import uuid
import json
from flask.sessions import SessionInterface
from flask.sessions import SessionMixin
from itsdangerous import Signer, BadSignature, want_bytes


class MySession(dict, SessionMixin):
    def __init__(self, initial=None, sid=None):
        self.sid = sid
        self.initial = initial
        super(MySession, self).__init__(initial or ())
    def __setitem__(self, key, value):
        super(MySession, self).__setitem__(key, value)
    def __getitem__(self, item):
        return super(MySession, self).__getitem__(item)
    def __delitem__(self, key):
        super(MySession, self).__delitem__(key)


class MySessionInterface(SessionInterface):
    session_class = MySession
    container = {}
    def __init__(self):
        import redis
        self.redis = redis.Redis()
    def _generate_sid(self):
        return str(uuid.uuid4())
    def _get_signer(self, app):
        if not app.secret_key:
            return None
        return Signer(app.secret_key, salt='flask-session',
                      key_derivation='hmac')
    def open_session(self, app, request):
        """
        程序刚启动时执行，需要返回一个session对象
        """
        sid = request.cookies.get(app.session_cookie_name)
        if not sid:
            sid = self._generate_sid()
            return self.session_class(sid=sid)
        signer = self._get_signer(app)
        try:
            sid_as_bytes = signer.unsign(sid)
            sid = sid_as_bytes.decode()
        except BadSignature:
            sid = self._generate_sid()
            return self.session_class(sid=sid)
        # session保存在redis中
        # val = self.redis.get(sid)
        # session保存在内存中
        val = self.container.get(sid)
        if val is not None:
            try:
                data = json.loads(val)
                return self.session_class(data, sid=sid)
            except Exception as e:
                return self.session_class(sid=sid)
        return self.session_class(sid=sid)
    def save_session(self, app, session, response):
        """
        程序结束前执行，可以保存session中所有的值
        如：
            保存到resit
            写入到用户cookie
        """
        domain = self.get_cookie_domain(app)
        path = self.get_cookie_path(app)
        httponly = self.get_cookie_httponly(app)
        secure = self.get_cookie_secure(app)
        expires = self.get_expiration_time(app, session)
        val = json.dumps(dict(session))
        # session保存在redis中
        # self.redis.setex(name=session.sid, value=val, time=app.permanent_session_lifetime)
        # session保存在内存中
        self.container.setdefault(session.sid, val)
        session_id = self._get_signer(app).sign(want_bytes(session.sid))
        response.set_cookie(app.session_cookie_name, session_id,
                            expires=expires, httponly=httponly,
                            domain=domain, path=path, secure=secure)

from flask_session import Session
from redis import Redis




import os
from flask import session, g, current_app
from ..model import   User

class Md(object):
    def __init__(self, old_wsgi_app):
        self.old_wsgi_app = old_wsgi_app

    def __call__(self, environ, start_response):
        print("开始之前")
        ret = self.old_wsgi_app(environ, start_response)
        print("结束之后")
        return ret
class PersistentSystem(object):
    _instance_lock = threading.Lock()
    app =None
    def __new__(cls, *args, **kwargs):
        if not hasattr(PersistentSystem, "_instance"):
            with PersistentSystem._instance_lock:
                if not hasattr(PersistentSystem, "_instance"):
                    PersistentSystem._instance = object.__new__(cls)  
        return PersistentSystem._instance

    def __init__(self, app=None):
        if not self.app  is None:
            return 
        self.app = app
        app.config['SESSION_TYPE'] = 'redis'   #session存储格式为redis
        app.config['SESSION_REDIS'] = Redis(    #redis的服务器参数
            host='localhost',                 #服务器地址
            port=6379)                           #服务器端口

        app.config['SESSION_USE_SIGNER'] = True   #是否强制加盐，混淆session
        app.config['SECRET_KEY'] = os.urandom(24)  #如果加盐，那么必须设置的安全码，盐
        app.config['SESSION_PERMANENT'] = False  #sessons是否长期有效，false，则关闭浏览器，session失效
        app.config['PERMANENT_SESSION_LIFETIME'] = 3600   #session长期有效，则设定session生命周期，整数秒，默认大概不到3小时。
        Session(app)
        self.add_func(app)

    @classmethod
    def add_func(cls,app):
        @app.before_request
        def load_user(*args, **kwargs):
            print('load_user')
            # if g.get('user') is not None:
            #    return None
            # persistent_info = PersistentSystem.query()
            """
            加载用户信息， 可提取模块后用flask_cache另写加速
            —— 考虑认证系统则易出现冲突
            ———暂时每次请求都刷新
            ————可以另起刷新队列
            """
            cls.flash_user_type()
            persistent_info = PersistentSystem.query()
            g.persistent = persistent_info
            return None

    @classmethod
    def save(cls,wechat_server_reply, user):
        """
        persistent_info
            openid, unionid, session_key, user_type, user_id
        """
        if wechat_server_reply is None:
            return None
        persistent_info = wechat_server_reply.copy()
        persistent_info['user_type'] = user.get_type()
        persistent_info['user_id'] = user.user_id
        session['persistent_info'] = persistent_info

    @classmethod
    def query(cls):
        persistent_info = session.get('persistent_info')
        if persistent_info is None:
            return None
        sess = {
            'openid': persistent_info.get('openid'),
            'unionid': persistent_info.get('unionid'),
            'session_key': persistent_info.get('session_key'),
            'user_id': persistent_info.get('user_id'),
            'user_type': persistent_info.get('user_type')
        }
        return  sess
    
    #用来刷新用户的状态
    @classmethod
    def flash_user_type(cls):
        persistent_info = session.get('persistent_info')
        if persistent_info is not None:
            unionid =  persistent_info.get('unionid')
            persistent_info['user_type'] = User.table.query_user(unionid= unionid)
            session['persistent_info'] = persistent_info
    
    def get_user(self):
        if session.get('unionid') is not None:
            return User.table.query_user(unionid = session['unionid'])


