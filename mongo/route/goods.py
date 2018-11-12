# encoding: utf-8
"""
__author__:cjhcw
"""
from flask import Blueprint, request, jsonify

from database.users_db import requires_auth
from database import goods_db
import jwt

goods = Blueprint("goods", __name__, url_prefix='/api/news')


@goods.route('/send_goods', methods=["POST", "DELETE", "PUT"])
@requires_auth
def send_goods():
    """
    POST
    DELETE
    PUT
    :return:
    """
    if request.method == 'POST':
        data = request.get_json()
        token = request.headers.get('Authorization')
        token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
        result = goods_db.add_send_good(int(token['uid']), data)
        if result:
            return jsonify({"message": "添加商品成功", "code": 401}), 200
        else:
            return jsonify({"message": "添加商品失败", "code": 402}), 404
    elif request.method == 'DELETE':
        data = request.get_json()
        goods_list = data['goods_list']
        result = goods_db.delete_send_goods(goods_list)
        if result:
            return jsonify({"message": "删除商品成功", "code": 403}), 200
        else:
            return jsonify({"message": "删除商品失败", "code": 404}), 404
    elif request.method == 'PUT':
        data = request.get_json()
        result = goods_db.edit_send_goods(data)
        if result:
            return jsonify({"message": "编辑商品成功", "code": 405}), 200
        else:
            return jsonify({"message": "编辑商品失败", "code": 406}), 404
