# _*_ coding: utf-8 _*_
DEBUG = True
UPLOAD_FOLDER = 'upload'
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
UPLOADED_PHOTOS_DEST = './images/'  # 相对路径下的文件夹images
UPLOADED_PHOTO_ALLOW = IMAGES		# 限制只能够上传图片
UPLOADS_DEFAULT_URL = 'http://127.0.0.1:9000/'
