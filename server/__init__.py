import os
from flask_sqlalchemy import SQLAlchemy
from flask_security import SQLAlchemySessionUserDatastore, Security
from flask import Flask
from database import  db, init_db
from models import User, Role

from server.routers.auth import auth_bp

app = Flask(__name__)
app.register_blueprint(auth_bp)

app.add_url_rule('/', endpoint='index')

#redirect url to index
@app.route('/index')
def index():
    return 'index'

user_datastore = SQLAlchemySessionUserDatastore(db,
                                                User, Role)
security = Security(app, user_datastore)


from models import db, user_datastore
# Create a user to test with
@app.before_first_request
def create_user():
    db.create_all()
    user_datastore.create_user(email='matt@nobien.net', password='password')
    db.session.commit()

