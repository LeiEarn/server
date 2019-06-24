# -*- coding: utf-8 -*-
from flask_mail import Mail, Message



class MailSystem():
    def __init__(self, app):
        # After 'Create app'
        app.config['MAIL_SERVER'] = 'smtp.163.com'
        app.config['MAIL_PORT'] =25
        app.config['MAIL_USE_SSL'] = True
        app.config['MAIL_USERNAME'] = '13231112083@163.com'
        app.config['MAIL_PASSWORD'] = 'nameguyu123'
        self.mail = Mail(app)
    
    def send_register_email(self, id, email):
        msg = Message("Hello",
                  recipients=[email])
        self.mail.send(msg)
