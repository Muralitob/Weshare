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
        return jsonify({"code": 201}), 200
    else:
        return jsonify({"code": 202}), 404


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
        return jsonify({"code": 203}), 404


@users.route('/get_user_info', methods=['GET'])
@users_db.requires_auth
def get_user_info():
    """
    获取用户信息
    :return:
    """
    token = request.headers.get('Authorization')
    data = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
    result = users_db.get_user_info(data['uid'])
    if result:
        return jsonify(utility.convert_to_json(result)), 200
    else:
        return jsonify({"code": 204}), 404


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
        return jsonify({"code": 205}), 200
    else:
        return jsonify({"code": 206}), 404


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
        result, length = users_db.get_collections_by_uid(token['uid'], int(page), int(limit))
        return jsonify({"collections": utility.convert_to_json(result), "total": length}), 200
    elif request.method == 'POST':
        data = request.get_json()
        token = request.headers.get('Authorization')
        token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
        article_id = data['_id']
        result = users_db.save_collection(token['uid'], article_id)
        if result:
            return jsonify({"code": 207}), 200
        else:
            return jsonify({"code": 208}), 404
    elif request.method == 'DELETE':
        data = request.get_json()
        token = request.headers.get('Authorization')
        token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
        article_ids = data['article_ids']
        result = users_db.delete_collections(token['uid'], article_ids)
        if result:
            return jsonify({"code": 209}), 200
        else:
            return jsonify({"code": 210}), 404
