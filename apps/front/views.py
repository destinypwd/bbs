from flask import (
    Blueprint, views, render_template, request, g,session,url_for,abort
)
from ..models import BannerModel, BoardModel, PostModel,CommentModel,HighlightPostModel
import config
from utils import result,safeutils
from .forms import SignupForm,SigninForm,AddPostForm,AddCommentForm
from .models import FrontUser
from exts import db
from .decorators import login_required
from flask_paginate import  Pagination,get_page_parameter
from sqlalchemy import func

bp = Blueprint("front", __name__)


@bp.route('/')
def index():
    board_id = request.args.get('bd',type=int,default=None)
    page = request.args.get(get_page_parameter(), type=int, default=1)
    banners = BannerModel.query.order_by(BannerModel.priority.desc()).limit(4)
    sort = request.args.get("st",type=int,default=1)
    boards = BoardModel.query.all()
    start = (page-1)*config.PER_PAGE
    end = start + config.PER_PAGE
    posts = None
    total = 0

    query_boj = None
    if sort == 1:
        query_boj = PostModel.query.order_by(PostModel.create_time.desc())
    elif sort == 2:
        #按照加精的时间倒叙排序
        query_boj = db.session.query(PostModel).outerjoin(HighlightPostModel).order_by(HighlightPostModel.create_time.desc(),PostModel.create_time.desc())
    elif sort == 3:
        #按照点赞的数量排序
        query_boj = PostModel.query.order_by(PostModel.create_time.desc())
    elif sort == 4:
        #按照评论的数量排序
        query_boj = db.session.query(PostModel).outerjoin(CommentModel).group_by(PostModel.id).order_by(func.count(CommentModel.id).desc(),PostModel.create_time.desc())
    if board_id:
        query_boj = query_boj.filter(PostModel.board_id==board_id)
        posts = query_boj.slice(start,end)
        total = query_boj.count()
    else:
        posts = query_boj.slice(start,end)
        total =query_boj.count()
    pagination = Pagination(page=page,total=total)
    context = {
        'banners':banners,
        'boards': boards,
        'posts':posts,
        'pagination':pagination,
        'current_board':board_id,
        'current_sort':sort
    }
    return render_template('front/front_index.html',**context)


@bp.route('/apost/',methods=['GET','POST'])
@login_required
def apost():
    if request.method == 'GET':
        boards = BoardModel.query.all()
        return render_template('front/front_apost.html',boards=boards)
    else:
        form = AddPostForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            board_id = form.board_id.data
            board = BoardModel.query.get(board_id)
            if not board:
                return result.params_error(message='没有这个板块')
            post = PostModel(title=title,content=content)
            post.board = board
            post.author = g.front_user
            db.session.add(post)
            db.session.commit()
            return result.success()
        else:
            return result.params_error(message=form.get_error())


@bp.route('/p/<post_id>/')
def post_detail(post_id):
    post = PostModel.query.get(post_id)
    comments = CommentModel.query.get
    if not post:
        abort(404)
    return render_template('front/front_pdetail.html',post=post)


@bp.route('/acomment/',methods=['POST'])
@login_required
def add_comment():
    form = AddCommentForm(request.form)
    if form.validate():
        content = form.content.data
        post_id = form.post_id.data
        post = PostModel.query.get(post_id)
        if post:
            comment = CommentModel(content=content)
            comment.post = post
            comment.author = g.front_user
            db.session.add(comment)
            db.session.commit()
            return result.success()
        else:
            return result.params_error('没有这篇帖子')
    else:
        return result.params_error(form.get_error())


class SignupView(views.MethodView):
    def get(self):
        return_to = request.referrer
        if return_to and return_to != request.url and safeutils.is_safe_url(return_to):
            return render_template('front/front_signup.html',return_to=return_to)
        else:
            return render_template('front/front_signup.html')

    def post(self):
        form = SignupForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.user.data
            password = form.password1.data
            user = FrontUser(username=username,password=password,email=email)
            db.session.add(user)
            db.session.commit()
            return result.success()
        else:
            print(form.get_error())
            return result.params_error(form.get_error()) or result.server_error(form.get_error())

class SigninView(views.MethodView):
    def get(self):
        return_to = request.referrer
        if return_to and return_to != request.url and return_to != url_for('front.signup') and safeutils.is_safe_url(return_to):
            return render_template('front/front_signin.html',return_to=return_to)
        else:
            return render_template('front/front_signin.html')
    def post(self):
        form = SigninForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = FrontUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.FRONT_USE_ID]=user.id
                if remember:
                    session.permanent = True
                    return result.success()
                else:
                    return result.params_error(message='邮箱或密码错误！')
            else:
                return result.params_error(message=form.get_error())

bp.add_url_rule('/login/',view_func=SigninView.as_view('login'))
bp.add_url_rule('/signup/', view_func=SignupView.as_view('signup'))
