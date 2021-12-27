from ..forms import BaseForm
from wtforms import StringField
from wtforms.validators import regexp, Email, InputRequired
import hashlib


class EmailCaptchaForm(BaseForm):
    salt = 'q3423805gdflvbdfvhsdoa`#$%'
    email = StringField(validators=[Email(message="请输入存在的邮箱")])
    timestamp = StringField(validators=[regexp(r"\d{13}")])
    sign = StringField(validators=[InputRequired()])

    def validate(self):
        result = super(EmailCaptchaForm, self).validate()
        if not result:
            return False
        email = self.email.data
        timestamp = self.timestamp.data
        sign = self.sign.data

        sign2 = hashlib.md5((timestamp+email+self.salt).encode('utf-8')).hexdigest()
        if sign == sign2:
            return True
        else:
            return False
