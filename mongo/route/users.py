# encoding: utf-8
"""
__author__:cjhcw
"""
from flask import Blueprint
from flask import jsonify, request
import jwt

from database import users_db

import utility

users = Blueprint("user", __name__, url_prefix='/api/user')


@users.route('/register', methods=['POST'])
def register():
    """
    注册用户
    :parameter
    account
    password
    nickname
    :return:
    """
    data = request.get_json()
    result = users_db.register(data)
    if result:
        return jsonify({"message": "注册成功", "code": 201}), 200
    else:
        return jsonify({"message": "注册失败", "code": 202}), 404


@users.route('/login', methods=['POST'])
def login():
    """
    登录(支持用户名、学号、邮箱登录)
    :parameter
    account
    password
    :return:
    """
    data = request.get_json()
    result = users_db.login(data)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({"message": "登录失败", "code": 203}), 404


@users.route('/get_user_info', methods=['GET'])
@users_db.requires_auth
def get_user_info():
    """
    获取用户信息
    :return:
    """
    token = request.headers.get('Authorization')
    data = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
    result = users_db.get_user_info(int(data['uid']))
    if result:
        return jsonify(utility.convert_to_json(result)), 200
    else:
        return jsonify({"message": "获取用户信息失败", "code": 204}), 404


@users.route('/edit_user_info', methods=['POST'])
@users_db.requires_auth
def edit_user_info():
    """
    修改用户信息
    :return:
    """
    data = request.get_json()
    token = request.headers.get('Authorization')
    token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
    result = users_db.edit_user_info(int(token['uid']), data)
    if result:
        return jsonify({"message": "修改用户信息成功", "code": 205}), 200
    else:
        return jsonify({"message": "修改用户信息失败", "code": 206}), 404


# restful-API
# 别人也可以看到自己收藏的文章
@users.route('/collections', methods=['POST', 'DELETE', 'GET'])
@users_db.requires_auth
def collections_functions():
    """
    POST收藏文章,
    DELETE批量删除收藏的文章,
    GET获取uid下的collections收藏
    :return:
    """
    if request.method == 'GET':
        token = request.headers.get('Authorization')
        token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
        page = request.args.get('page')
        limit = request.args.get('limit')
        result, length = users_db.get_collections_by_uid(int(token['uid']), int(page), int(limit))
        return jsonify({"collections": utility.convert_to_json(result), "total": length}), 200
    elif request.method == 'POST':
        data = request.get_json()
        token = request.headers.get('Authorization')
        token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
        article_id = data['_id']
        result = users_db.save_collection(int(token['uid']), article_id)
        if result:
            return jsonify({"message": "收藏文章成功", "code": 207}), 200
        else:
            return jsonify({"message": "收藏文章失败", "code": 208}), 404
    elif request.method == 'DELETE':
        data = request.get_json()
        token = request.headers.get('Authorization')
        token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
        article_ids = data['article_ids']
        result = users_db.delete_collections(int(token['uid']), article_ids)
        if result:
            return jsonify({"message": "删除收藏成功", "code": 209}), 200
        else:
            return jsonify({"message": "删除收藏失败", "code": 210}), 404
