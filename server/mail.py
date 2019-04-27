# At top of file
from flask_mail import Mail

# After 'Create app'
app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] =25
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = '13231112083@163.com'
app.config['MAIL_PASSWORD'] = 'nameguyu123'
mail = Mail(app)
