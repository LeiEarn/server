# _*_ coding: utf-8 _*_

from redis import Redis
import os
DEBUG = True
UPLOAD_FOLDER = 'upload'
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
UPLOADED_PHOTOS_DEST = './images/'  # 相对路径下的文件夹images
UPLOADED_PHOTO_ALLOW = IMAGES		# 限制只能够上传图片

#邮箱配置
MAIL_SERVER = 'smtp.163.com'
MAIL_PORT =25
MAIL_USE_SSL = True
MAIL_USERNAME = '13231112083@163.com'
MAIL_PASSWORD = 'nameguyu123'

#redis

SESSION_TYPE = 'redis'   #session存储格式为redis
SESSION_REDIS = Redis(    #redis的服务器参数
    host='redis',                 #服务器地址
    port=6379)                           #服务器端口
SESSION_USE_SIGNER = True   #是否强制加盐，混淆session
SECRET_KEY = os.urandom(24)  #如果加盐，那么必须设置的安全码，盐
SESSION_PERMANENT = False  #sessons是否长期有效，false，则关闭浏览器，session失效
PERMANENT_SESSION_LIFETIME = 3600   #session长期有效，则设定session生命周期，整数秒，默认大概不到3小时。

class CONST:
    # remote
    HOST = 'www.zhengxianqian.club'
    USER = 'yunquan'
    PASSWD = '12345678'

    PORT=3306
    DB = 'ZXQ'
