import random
import string
from flask import Blueprint, request,make_response
from flask_mail import Message
from exts import mail
from utils import result,zlcache
from .forms import EmailCaptchaForm
from utils.captcha import Captcha
from io import BytesIO

bp = Blueprint("common", __name__, url_prefix='/common/')


@bp.route('/')
def index():
    return 'common index'

@bp.route('/email_captcha/',methods=['POST'])
def email_captcha():
    form = EmailCaptchaForm(request.form)
    if form.validate():
        email = form.email.data
        source = list(string.ascii_letters)
        source.extend(map(lambda x: str(x), range(0, 10)))
        captcha = "".join(random.sample(source, 6))
        # 给这个邮箱发邮件
        message = Message('论坛邮箱验证码', recipients=[email], body='您的验证码是：%s' % captcha)
        try:
            mail.send(message)
        except:
            return result.server_error()
        zlcache.set(email, captcha)
        return result.success()
    else:
        return result.params_error(message='参数错误')

@bp.route('/captcha/')
def graph_captcha():
    text, image = Captcha.gene_graph_captcha()
    zlcache.set(text.lower(),text.lower())
    out = BytesIO()
    image.save(out, 'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp