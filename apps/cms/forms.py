from wtforms import StringField,IntegerField
from wtforms.validators import Email,Length,EqualTo,InputRequired
from ..forms import BaseForm
from utils import zlcache
from wtforms import ValidationError
from flask import g

class LoginForm(BaseForm):
    email = StringField(validators=[Email(message="请输入存在的邮箱")])
    password = StringField(validators=[Length(6,20,message='请输入正确格式的密码')])
    remember = IntegerField()

class RetpwdForm(BaseForm):
    oldpwd = StringField(validators=[Length(6,20,message='请输入正确格式的旧密码')])
    newpwd = StringField(validators=[Length(6,20,message='请输入正确格式的新密码')])
    newpwd2 = StringField(validators=[EqualTo("newpwd")])

class ResetEmailForm(BaseForm):
    email = StringField(validators=[Email(message='请输入正确的邮箱')])
    captcha = StringField(validators=[Length(min=6,max=6,message='请输入正确的验证码')])

    def validate_email(self,field):
        email = field.data
        user = g.cms_user
        if user.email == email:
            raise ValidationError('不能修改为相同的邮箱')

    def validate_captcha(self,field):
        captcha = field.data
        email = self.email.data
        captcha_cache = zlcache.get(email)
        if not captcha_cache or captcha.lower() != captcha_cache.lower():
            raise  ValidationError('邮箱验证码错误')

class AddBannersForm(BaseForm):
    name = StringField(validators=[InputRequired('请输入轮播图名称')])
    image_url = StringField(validators=[InputRequired('请输入图片的地址')])
    link_url = StringField(validators=[InputRequired('请输入图片跳转链接')])
    priority = IntegerField(validators=[InputRequired('请输入轮播图优先级')])

class UpdateBannersForm(AddBannersForm):
    banner_id = IntegerField(validators=[InputRequired(message='请输入要修改的id！')])


class AddBoardForm(BaseForm):
    name = StringField(validators=[InputRequired(message='请输入板块名称')])


class UpdateBoardForm(AddBoardForm):
    board_id = IntegerField(validators=[InputRequired(message='请输入板块id')])