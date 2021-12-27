from wtforms.validators import Email, Length, EqualTo, Regexp, InputRequired
from utils import zlcache
from ..forms import BaseForm
from wtforms import StringField,IntegerField,ValidationError

class SignupForm(BaseForm):
    email = StringField(validators=[Email(message='请输入正确的邮箱')])
    captcha = StringField(validators=[Length(4,6, message='请输入正确格式的短信验证码！')])
    user = StringField(validators=[Length(3,10,message='请输入正确的用户名')])
    password1 = StringField(validators=[Length(6, 20, message='请输入正确格式的密码')])
    password2 = StringField(validators=[EqualTo('password1',message='两次密码不一致')])
    graph_captcha = StringField(validators=[Length(4,4,message='请输入正确格式的图形验证码！')])

    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        if captcha != '1111':
            captcha_cache = zlcache.get(email)
            if not captcha_cache or captcha_cache.lower() != captcha.lower():
                raise ValidationError('邮箱验证码错误')

    def validate_graph_captcha(self,field):
        graph_captcha = field.data
        if graph_captcha != '1111':
            graph_captcha_mem = zlcache.get(graph_captcha.lower())
            if not graph_captcha_mem:
                raise ValidationError('图形验证码错误')

class SigninForm(BaseForm):
    email = StringField(validators=[Email(message='请输入正确的邮箱')])
    password = StringField(validators=[Length(6, 20, message='请输入正确格式的密码')])
    remember = StringField()

class AddPostForm(BaseForm):
    title = StringField(validators=[InputRequired(message='请输入标题！')])
    content = StringField(validators=[InputRequired(message='请输入内容！')])
    board_id = IntegerField(validators=[InputRequired(message='请输入板块id！')])

class AddCommentForm(BaseForm):
    content = StringField(validators=[InputRequired(message='请输入评论内容！')])
    post_id = IntegerField(validators=[InputRequired(message='请输入帖子id！')])