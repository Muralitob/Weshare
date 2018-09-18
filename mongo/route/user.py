# encoding: utf-8
"""
__author__:cjhcw
"""
from flask import Blueprint
from flask import jsonify, make_response, request, json

from database import user_db

user = Blueprint("user", __name__, url_prefix='/api/user')


@user.route('/register', methods=['POST'])
def register():
    """
    注册用户
    :parameter
    account
    password
    :return:
    """
    data = request.get_json()
    result = user_db.register(data)
    if result:
        return jsonify({"message": 'register success', "code": 200}), 200
    else:
        return jsonify({"message": 'register fail', "code": 404}), 404


@user.route('/login', methods=['POST'])
def login():
    """
    登录(支持用户名、学号、邮箱登录)
    :parameter
    account
    password
    :return:
    """
    data = request.get_json()
    result = user_db.login(data)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({"status": 'login fail', "code": 404}), 404
