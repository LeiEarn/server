from server import app
import os
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from flask_security import SQLAlchemyUserDatastore, Security



def init_db():
    from models import  Student,   Orgnization
    db.create_all()

    
    db.session.commit()