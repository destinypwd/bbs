import os
import random
import re
import string
import pathlib
from flask import (
    Blueprint, render_template, views, request, session, redirect, url_for, g,
    jsonify
)
from .forms import LoginForm, RetpwdForm, ResetEmailForm, AddBannersForm, UpdateBannersForm, AddBoardForm, \
    UpdateBoardForm
from .models import CMSUser, CMSPersmission
from ..models import BannerModel, BoardModel,PostModel,HighlightPostModel,CommentModel
from ..front.models import FrontUser
from .decorators import login_required, permission_required
import config
from exts import db, mail
from flask_mail import Message
from utils import result, zlcache
from werkzeug.utils import secure_filename
from tasks import send_mail

bp = Blueprint("cms", __name__, url_prefix='/cms/')


@bp.route('/')
@login_required
def index():
    return render_template('cms/cms_index.html')


@bp.route('/profile/')
@login_required
def profile():
    return render_template('cms/cms_profile.html')


@bp.route('/logout/')
@login_required
def logout():
    del session[config.CMS_USE_ID]
    return redirect(url_for('cms.login'))


@bp.route('/email_captcha/')
def email_captcha():
    email = request.args.get('email')
    if not email:
        return result.params_error('请输入邮箱')
    source = list(string.ascii_letters)
    source.extend(map(lambda x: str(x), range(0, 10)))
    captcha = "".join(random.sample(source, 6))
    # email = g.cms_user.email
    # 给这个邮箱发邮件
    # message = Message('论坛邮箱验证码', recipients=[email], body='您的验证码是：%s' % captcha)
    # try:
    #     mail.send(message)
    # except:
    #     return result.server_error()
    send_mail.delay('论坛邮箱验证码',[email], '您的验证码是：%s' % captcha) #  celery === 多线程
    zlcache.set(email, captcha)
    return result.success()


@bp.route('/posts/')
@login_required
@permission_required(CMSPersmission.POSTER)
def posts():
    context = {
        'posts':PostModel.query.all()
    }
    return render_template('cms/cms_posts.html',**context)


@bp.route('/hpost/',methods=['POST'])
@login_required
@permission_required(CMSPersmission.POSTER)
def hpost():
    post_id = request.form.get("post_id")
    if not post_id:
        return result.params_error('请传入帖子id')
    post = PostModel.query.get(post_id)
    if not post:
        return result.params_error('没有这篇帖子')
    highlight = HighlightPostModel()
    highlight.post = post
    db.session.add(highlight)
    db.session.commit()
    return result.success()


@bp.route('/uhpost/',methods=['POST'])
@login_required
@permission_required(CMSPersmission.POSTER)
def uhpost():
    post_id = request.form.get("post_id")
    if not post_id:
        return result.params_error('请传入帖子id')
    post = PostModel.query.get(post_id)
    if not post:
        return result.params_error('没有这篇帖子')
    highlight = post.highlight
    db.session.delete(highlight[0])
    db.session.commit()
    return result.success()


@bp.route('/comments/')
@login_required
@permission_required(CMSPersmission.COMMENTER)
def comments():
    context = {
        'posts':CommentModel.query.all()
    }
    return render_template('cms/cms_comments.html',**context)


@bp.route('/dcomments/',methods=['POST'])
@login_required
@permission_required(CMSPersmission.COMMENTER)
def dcomments():
    comments_id = request.form.get("comments_id")
    if not comments_id:
        return result.params_error('请传入留言id')
    comment = CommentModel.query.get(comments_id)
    if not comment:
        return result.params_error(message='没有这条留言')
    db.session.delete(comment)
    db.session.commit()
    return result.success()


@bp.route('/boards/')
@login_required
@permission_required(CMSPersmission.BOARDER)
def boards():
    board_models = BoardModel.query.all()
    context = {
        'boards': board_models
    }
    return render_template('cms/cms_boards.html', **context)


@bp.route('/aboard/', methods=['POST'])
@login_required
@permission_required(CMSPersmission.BOARDER)
def aboard():
    form = AddBoardForm(request.form)
    if form.validate():
        name = form.name.data
        print(name)
        board = BoardModel(name=name)
        db.session.add(board)
        db.session.commit()
        return result.success()
    else:
        return result.params_error(message=form.get_error())


@bp.route('/uboard/', methods=['POST'])
@login_required
@permission_required(CMSPersmission.BOARDER)
def uboard():
    form = UpdateBoardForm(request.form)
    if form.validate():
        board_id = form.board_id.data
        name = form.name.data
        board = BoardModel.query.get(board_id)
        if board:
            board.name = name
            db.session.commit()
            return result.success()
        else:
            return result.params_error(message='没有这个板块')
    else:
        return result.params_error(form.get_error())


@bp.route('/dboard/', methods=['POST'])
@login_required
@permission_required(CMSPersmission.BOARDER)
def dboard():
    board_id = request.form.get("board_id")
    if not board_id:
        return result.params_error('请传入板块id')
    board = BoardModel.query.get(board_id)
    if not board:
        return result.params_error(message='没有这个板块')
    db.session.delete(board)
    db.session.commit()
    return result.success()


@bp.route('/fusers/')
@login_required
@permission_required(CMSPersmission.FRONTUSER)
def fusers():
    front_user = FrontUser.query.all()
    context = {
        'front_user':front_user
    }
    return render_template('cms/cms_fusers.html',**context)


@bp.route('/dfusers/',methods=['POST'])
@login_required
@permission_required(CMSPersmission.FRONTUSER)
def dfusers():
    user_id = request.form.get('user_id')
    if not user_id:
        return result.params_error("没有传入用户id")
    comment = PostModel.query.get(user_id)
    user = FrontUser.query.get(user_id)
    if not user:
        return result.params_error(message="没有这个用户")
    # db.session.delete(comment)
    db.session.delete(user)
    db.session.commit()
    return result.success()

@bp.route('/cusers/')
@login_required
@permission_required(CMSPersmission.CMSUSER)
def cusers():
    cms_user = CMSUser.query.all()
    context = {
        'user': cms_user
    }
    return render_template('cms/cms_cusers.html',**context)

@bp.route('/dcusers/',methods=['POST'])
@login_required
@permission_required(CMSPersmission.FRONTUSER)
def dcusers():
    user_id = request.form.get('user_id')
    if not user_id:
        return result.params_error("没有传入用户id")
    user = CMSUser.query.get(user_id)
    if not user:
        return result.params_error(message="没有这个用户")
    # db.session.delete(comment)
    db.session.delete(user)
    db.session.commit()
    return result.success()

@bp.route('/croles/')
@login_required
@permission_required(CMSPersmission.ALL_PERMISSION)
def croles():
    return render_template('cms/cms_croles.html')


@bp.route('/banners/')
@login_required
def banners():
    banners = BannerModel.query.order_by(BannerModel.priority.desc()).all()
    return render_template('cms/cms_banners.html', banners=banners)


@bp.route('/abanners/', methods=['POST'])
def abanners():
    form = AddBannersForm(request.form)
    if form.validate():
        name = form.name.data
        image_url = form.image_url.data
        link_url = form.link_url.data
        priority = form.priority.data
        banner = BannerModel(name=name, image_url=image_url, link_url=link_url, priority=priority)
        db.session.add(banner)
        db.session.commit()
        return result.success()
    else:
        return result.params_error(form.get_error())


@bp.route('/ubanners/', methods=['POST'])
def ubanners():
    form = UpdateBannersForm(request.form)
    if form.validate():
        banner_id = form.banner_id.data
        name = form.name.data
        image_url = form.image_url.data
        link_url = form.link_url.data
        priority = form.priority.data
        banner = BannerModel.query.get(banner_id)
        if banner:
            banner.name = name
            banner.image_url = image_url
            banner.link_url = link_url
            banner.priority = priority
            db.session.commit()
            return result.success()
        else:
            return result.params_error(message='没有这个轮播图!')
    else:
        return result.params_error(message=form.get_error())


@bp.route('/dbanners/', methods=['POST'])
def dbanners():
    banner_id = request.form.get('banner_id')
    if not banner_id:
        return result.params_error(message='请输入轮播图id')
    banner = BannerModel.query.get(banner_id)
    if not banner:
        return result.params_error(message='没有这个轮播图')
    file = str(banner.image_url)
    file = re.split(r"http://127.0.0.1:5000/static/picture/", file)[1]
    file = os.path.join(config.UPLOAD_FOLDER, file)
    print(file)
    os.remove(file)
    db.session.delete(banner)
    db.session.commit()
    return result.success()


@bp.route('/file_uploads/', methods=['POST'])
def file_uploads():
    print(request.files)
    if 'file' not in request.files:
        return result.params_error('请上传正确的图片')
    file = request.files['file']
    if file.filename == '':
        return result.params_error('没有选中文件')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        print(filename, 'secure_filename')
        file_path = pathlib.Path(config.UPLOAD_FOLDER)
        if file_path.is_dir():
            file.save(os.path.join(config.UPLOAD_FOLDER, filename))
            return result.success()
        else:
            os.makedirs(file_path)
            file.save(os.path.join(config.UPLOAD_FOLDER, filename))
            return result.success()


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in config.ALLOWD_EXTENSIONS


class LoginView(views.MethodView):
    def get(self, message=None):
        return render_template('cms/cms_login.html', message=message)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.CMS_USE_ID] = user.id
                if remember:
                    # 如果设置session.permanent = True 那么过期时间是31天
                    session.permanent = True
                return redirect(url_for('cms.index'))
            else:
                return self.get(message="邮箱或密码错误")
        else:
            message = form.get_error()
            return self.get(message=message)


class ResetPwdView(views.MethodView):
    decorators = [login_required]

    def get(self):
        return render_template('cms/cms_resetpwd.html')

    def post(self):
        form = RetpwdForm(request.form)
        if form.validate():
            newpwd = form.newpwd.data
            oldpwd = form.oldpwd.data
            user = g.cms_user
            if user.check_password(oldpwd):
                user.password = newpwd
                db.session.commit()
                # {"code":400/200,message="密码错误"}
                # return jsonify({"code": 200, "message": ''})
                return result.success()
            else:
                return result.params_error('密码错误')
        else:
            return result.params_error(form.get_error())


class ResetEmailView(views.MethodView):
    decorators = [login_required]

    def get(self):
        return render_template('cms/cms_resetemail.html')

    def post(self):
        form = ResetEmailForm(request.form)
        if form.validate():
            email = form.email.data
            g.cms_user.email = email
            db.session.commit()
            return result.success()
        else:
            return result.params_error(form.get_error())


bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
bp.add_url_rule('/resetpwd/', view_func=ResetPwdView.as_view('resetpwd'))
bp.add_url_rule('/resetemail/', view_func=ResetEmailView.as_view('resetemail'))
