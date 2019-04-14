from server import app
import os
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from flask_security import SQLAlchemyUserDatastore, Security



def init_db():
    from models import  db, User, Role
    # Setup Flask-Security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)
    db.create_all()

admin = user_datastore.create_user(email='admin@4paradigm.com', password='admin')
# 生成普通用户角色和admin用户角色
user_datastore.create_role(name='User', description='Generic user role')
publisher_datastore
admin_role = user_datastore.create_role(name='Admin', description='Admin user role')
# 为admin添加Admin角色
user_datastore.add_role_to_user(admin, admin_role)
db.session.commit()