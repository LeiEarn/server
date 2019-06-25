# -*- coding: utf-8 -*-
import os

from flask import Flask, url_for, redirect
from .modules.loginPersistentSystem import PersistentSystem
from .modules.accessControlSystem import AccessControlSystem

def init_app(app,test_config=None):
    """Create and configure an instance of the Flask application."""

    app = app.app
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # 加载登录持久化中间件
    PersistentSystem(app=app)
    # 加载访问控制中间件
    AccessControlSystem(app=app)
    # ensure the instance folder exists
    
    # 测试数据库链接
    # register the database commands
    from .utils import db
    db.Database.init_db()

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 路由注册
    @app.route("/hello")
    def hello():
        return "Hello, World!"
    
    @app.route('/index')
    def index():
        login_url=url_for('hello')
        return redirect(login_url)

    # apply the blueprints to the app
    from .routers import  img, test

    #app.register_blueprint(auth.bp)
    app.register_blueprint(img.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="index")

    return app