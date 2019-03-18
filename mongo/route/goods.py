# encoding: utf-8
"""
__author__:cjhcw
"""
import hashlib
import jwt
import bson.binary
import bson.errors
import bson.objectid
from pymongo import errors

from flask import Blueprint, request, jsonify, make_response, abort

from core_manager.mongo_manager import mongo_manager
from database.users_db import requires_auth
from database import goods_db

from utility import convert_to_json, get_this_time

goods = Blueprint("goods", __name__, url_prefix='/api/goods')


def save_file_base64(base64_f):
    sha1 = hashlib.sha1(base64_f).hexdigest()
    c = dict(
        content=base64_f,
        mime="png",
        time=get_this_time(),
        sha1=sha1,
    )
    try:
        mongo_manager.save('files', c)
    except errors.DuplicateKeyError:
        pass
    return sha1


@goods.route('/send_goods', methods=['POST', 'DELETE', 'PUT'])
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
        if token:
            token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
            uid = token['uid']
        else:
            uid = request.cookies.get('uid')
        result = goods_db.add_send_good(int(uid), data)
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


@goods.route('/get_goods', methods=["GET"])
def get_goods():
    """
    获取商品列表
    :return:
    """
    page = request.args.get("page")
    limit = request.args.get("limit")
    keyword = request.args.get("keyword")
    good_type = request.args.get("type")
    degree = request.args.get("degree")
    goods_list, length = goods_db.get_goods(keyword, good_type, degree, page, limit)
    return jsonify({"goods": convert_to_json(goods_list), "total": length}), 200


@goods.route('/get_goods_by_uid', methods=["GET"])
@requires_auth
def get_goods_by_uid():
    """
    获取用户自己的商品列表
    :return:
    """
    page = request.args.get("page")
    limit = request.args.get("limit")
    keyword = request.args.get("keyword")
    good_type = request.args.get("type")
    degree = request.args.get("degree")
    uid = request.args.get("uid")
    if not uid:
        token = request.headers.get('Authorization')
        if token:
            token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
            uid = token['uid']
        else:
            uid = request.cookies.get('uid')
            if not uid:
                uid = None
    goods_list, length = goods_db.get_goods_by_uid(int(uid), keyword, good_type, degree, page, limit)
    return jsonify({"goods": convert_to_json(goods_list), "total": length}), 200


@goods.route('/save_good_photo', methods=['POST'])
@requires_auth
def save_good_photo():
    """
    保存商品图片
    :return:
    """
    image_file = request.files.get("file")
    # 校验参数
    if image_file is None:
        # 表示用户没有上传商品照片
        return make_response(jsonify({"message": "未上传商品照片", "code": 407}), 404)

    import base64
    # 将文件名信息保存到数据库中
    bs4 = base64.b64encode(image_file.read())
    sha1 = save_file_base64(bs4)
    return make_response(jsonify({"message": "图片信息", "code": 408, "good_base64": bs4, "sha1": sha1}), 200)


@goods.route('/get_good_by_id', methods=["GET"])
def get_good_by_id():
    """
    通过id返回商品信息
    :return:
    """
    good_id = request.args.get("good_id")
    result = goods_db.get_good_by_id(good_id)
    return make_response(jsonify({"good": convert_to_json(result)}), 200)


@goods.route('/f_base64/<sha1>', methods=['GET'])
def serve_file_base64(sha1):
    try:
        f = mongo_manager.find_one('files', {'sha1': sha1})
        return make_response(jsonify({'response': f["content"]}), 200)
    except bson.errors.InvalidId:
        abort(404)
