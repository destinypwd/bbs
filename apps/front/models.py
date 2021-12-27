from datetime import datetime
from exts import db
import shortuuid
from werkzeug.security import generate_password_hash, check_password_hash
import enum

class GenderEnum(enum.Enum):
    MALE = 1
    FEMALE = 2
    SECRET = 3
    UNKNOW = 4

class FrontUser(db.Model):
    __tablename__ = 'front_user'
    id = db.Column(db.String(100),primary_key=True,default=shortuuid.uuid)
    username = db.Column(db.String(50),nullable=False)
    _password = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(50),unique=True)
    realnama = db.Column(db.String(50))
    avatar = db.Column(db.String(100))
    signature = db.Column(db.String(100))
    gender = db.Column(db.Enum(GenderEnum),default=GenderEnum.UNKNOW)
    join_time = db.Column(db.DateTime,default=datetime.now)

    def __init__(self, *args,**kwargs):
        if "password" in kwargs:
            self.password = kwargs.get('password')
            kwargs.pop("password")
        super(FrontUser, self).__init__(*args,**kwargs)

    @property  # 这个装饰器是把方法变成一个属性
    def password(self):
        return self._password

    @password.setter  # 每当设置password的时候就会执行下面的操作
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        return  check_password_hash(self._password, raw_password)
