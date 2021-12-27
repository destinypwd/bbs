from .views import bp
import config
from flask import session, g ,render_template
from .models import FrontUser


# 钩子函数，在请求之前获取
@bp.before_request
def before_request():
    if config.FRONT_USE_ID in session:
        user_id = session.get(config.FRONT_USE_ID)
        user = FrontUser.query.get(user_id)
        if user:
            g.front_user = user

@bp.errorhandler
def page_not_found():
    return render_template('front/front_404.html'),404