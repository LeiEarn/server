import os

from flask import Flask

app = Flask(__name__)
'''
from server import db
    db.init_app(app)
app.config.from_mapping(
    # a default secret that should be overridden by instance config
    SECRET_KEY='dev',
    # store the database in the instance folder
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)

'''
from server import  auth
app.register_blueprint(auth.auth)

app.add_url_rule('/', endpoint='index')
@app.route('/index')
def index():
    return 'index'