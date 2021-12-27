from functools import wraps
from flask import session, redirect, url_for, g
import config


def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if config.FRONT_USE_ID in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('front.login'))
    return inner
