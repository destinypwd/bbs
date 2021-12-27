from flask import jsonify


class HttpCode(object):
    ok = 200
    unautherror = 401
    paramserror = 400
    servererrror = 500


def result(code, message, data):
    return jsonify({"code": code, "message": message, "data": data or {}})


def success(message='', data=None):
    return result(code=HttpCode.ok, message=message, data=data)


def unauth_error(message=''):
    return result(code=HttpCode.unautherror, message=message, data=None)


def params_error(message=''):
    return result(code=HttpCode.paramserror, message=message, data=None)


def server_error(message=''):
    return result(code=HttpCode.servererrror, message=message or '服务器内部错误', data=None)
