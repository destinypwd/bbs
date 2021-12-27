import os

# SECRET_KEY = os.urandom(24)
SECRET_KEY = 'asdddadasd'
DEBUG = True

DB_URI = "mysql+pymysql://root:root@localhost:3308/icbc?charset=utf8"

SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False


CMS_USE_ID = 'a'
FRONT_USE_ID = 'a'

# 发送者邮箱的服务器地址
# MAIL_USE_TLS 端口号587
# MAIL_USE_SSL 端口号465
#qq邮箱不支持非加密方式发送邮件
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = '587'
MAIL_USE_TLS =True
MAIL_USERNAME =''
MAIL_PASSWORD =''
MAIL_DEFAULT_SENDER = ''

# 上传设置
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static/picture')
ALLOWD_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# 上传文件Ueditor的相关配置

UEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'images')

# flask-paginate的相关配置

PER_PAGE =10

# celery相关的配置
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"


#REDIS
REDIS_HOST = '127.0.0.1'
REDIS_PORT = '6379'
REDIS_DB = '5'
REDIS_PASSWORD = None
REDIS_CONNECT_TIME= None

