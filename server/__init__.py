#coding:utf8
import os

from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, logout_user, login_required, LoginManager, current_user
from flask import Flask

import flask_login

app = Flask(__name__)

# 加载配置文件内容
app.config.from_object('server.setting.FlaskSetting')     #模块下的setting文件名，不用加py后缀 



login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.login_message = '请登录'
login_manager.init_app(app)


from server.routers.auth import auth_bp


app.register_blueprint(auth_bp)


app.add_url_rule('/', endpoint='index')

#redirect url to index
@app.route('/index')
def index():
    return 'index'

from server.database import   init_db


from server.models import db
# Create a user to test with
@app.before_first_request
def create_user():
    db.create_all()
    db.session.commit()

