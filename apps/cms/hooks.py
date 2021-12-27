from .views import bp
import config
from flask import session, g
from .models import CMSUser,CMSPersmission


# 钩子函数，在请求之前获取
@bp.before_request
def before_request():
    if config.CMS_USE_ID in session:
        user_id = session.get(config.CMS_USE_ID)
        user = CMSUser.query.get(user_id)
        if user:
            g.cms_user = user
@bp.context_processor
def cms_context_processor():
    return {'CMSPermission':CMSPersmission}