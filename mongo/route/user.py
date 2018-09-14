# encoding: utf-8
"""
__author__:cjhcw
"""
from flask import Blueprint
from flask import jsonify, make_response, request, json

from database import user_db

user = Blueprint("user", __name__, url_prefix='/user')


@user.route('/register', methods=['POST'])
def register():
    """
    注册用户
    :return:
    """
    username = request.args.get('username')
    password = request.args.get('password')
    result = user_db.register(username, password)
    if result:
        return jsonify({"message": 'success'}), 200
    else:
        return jsonify({"message": 'fail'}), 404

