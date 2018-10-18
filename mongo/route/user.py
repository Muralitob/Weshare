# encoding: utf-8
"""
__author__:cjhcw
"""
from flask import Blueprint
from flask import jsonify, make_response, request, json
import jwt

from database import user_db

import utility

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
        return jsonify({"code": 201}), 200
    else:
        return jsonify({"code": 202}), 200


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
        return jsonify({"code": 203}), 200


@user.route('/get_user_info', methods=['GET'])
@user_db.requires_auth
def get_user_info():
    """
    获取用户信息
    :return:
    """
    token = request.headers.get('Authorization')
    data = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
    result = user_db.get_user_info(data['uid'])
    if result:
        return jsonify(utility.convert_to_json(result)), 200
    else:
        return jsonify({"code": 204}), 200


@user.route('/edit_user_info', methods=['POST'])
@user_db.requires_auth
def edit_user_info():
    """
    修改用户信息
    :return:
    """
    data = request.get_json()
    token = request.headers.get('Authorization')
    token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
    result = user_db.edit_user_info(int(token['uid']), data)
    if result:
        return jsonify({"code": 205}), 200
    else:
        return jsonify({"code": 206}), 200
